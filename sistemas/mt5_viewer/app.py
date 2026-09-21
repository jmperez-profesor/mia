"""
Aplicación principal MT5 Viewer - Interfaz gráfica con tkinter.
Visualización de cuentas de fondeo, posiciones, órdenes e historial.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from typing import Optional

from mt5_connector import MT5Connector, AccountInfo, TradeEvent, ConnectionState
from notifier import TradeNotifier, NotifLevel
from config import ConfigManager, LogManager, SavedAccount


class AccountCard(tk.Frame):
    """Tarjeta visual para una cuenta MT5."""

    def __init__(self, parent, account: AccountInfo, color: str, connector: MT5Connector, on_click=None, **kwargs):
        super().__init__(parent, bg="#1e1e2e", relief="flat", **kwargs)
        self.account = account
        self.color = color
        self.connector = connector
        self.on_click = on_click
        self.configure(bd=0, highlightbackground=color, highlightthickness=1)
        self._build_ui()

    def _build_ui(self):
        frame = tk.Frame(self, bg=self.color, height=4)
        frame.pack(fill="x")
        frame.pack_propagate(False)

        header = tk.Frame(self, bg="#1e1e2e", padx=15, pady=10)
        header.pack(fill="x")

        tk.Label(header, text=f"🔹 {self.account.nombre}", font=("Segoe UI", 14, "bold"),
                 bg=self.color, fg="white").pack(anchor="w")
        tk.Label(header, text=f"Servidor: {self.account.servidor} | Login: {self.account.login}",
                 font=("Segoe UI", 9), bg=self.color, fg="#8888aa").pack(anchor="w")

        body = tk.Frame(self, bg="#28283e", padx=15, pady=15)
        body.pack(fill="both")

        metrics = [
            ("Balance", f"${self.account.balance:,.2f}", "#00ff88"),
            ("Equity", f"${self.account.equity:,.2f}", "#00ccff"),
            ("Margen Libre", f"${self.account.margin_free:,.2f}", "#ffcc00"),
            ("P&L", f"${self.account.profit:+,.2f}", "#00ff88" if self.account.profit >= 0 else "#ff4444"),
            ("Margen Nivel", f"{self.account.margin_level:.1f}%", "#aa66ff"),
            ("Posiciones", f"{len(self.connector.posiciones_abiertas)}", "#ff8844"),
        ]

        for i, (label, value, color) in enumerate(metrics):
            col = i % 3
            row = i // 3
            cell = tk.Frame(body, bg="#28283e")
            cell.grid(row=row, column=col, padx=10, pady=5, sticky="nsew")
            body.grid_columnconfigure(col, weight=1)
            tk.Label(cell, text=value, font=("Segoe UI", 16, "bold"), bg="#28283e", fg=color).pack(anchor="w")
            tk.Label(cell, text=label.upper(), font=("Segoe UI", 8), bg="#28283e", fg="#666688").pack(anchor="w")

        status_text = self.account.estado or "Activa"
        status_color = "#00ff88" if status_text == "Active" else "#ffcc00"
        tk.Label(self, text=f"● {status_text}", font=("Segoe UI", 9),
                 bg=self.color, fg=status_color, anchor="e").pack(fill="x", padx=15, pady=(0, 8))

        if self.on_click:
            self.bind("<Button-1>", lambda e: self.on_click(self))
            self.configure(cursor="hand2")


class MT5ViewerApp:
    """Aplicación principal MT5 Viewer."""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("MT5 Viewer — Monitor de Cuentas de Fondeo")
        self.root.geometry("1200x750")
        self.root.configure(bg="#111122")
        self.root.minsize(1000, 600)

        self.connector = MT5Connector()
        self.notifier = TradeNotifier(title_prefix="MT5 Monitor")
        self.config = ConfigManager()
        self.log_manager = LogManager()
        self._connectors: dict = {}
        self._account_colors: dict = {}
        self._monitoring = False

        self._setup_styles()
        self._build_ui()
        self._setup_protocols()
        self._register_callbacks()
        self._load_saved_accounts()

    def _setup_styles(self):
        self.style = ttk.Style(self.root)
        self.style.theme_use("clam")
        self.style.configure("TNotebook", background="#111122")
        self.style.configure("TNotebook.Tab", background="#1e1e2e", foreground="white", padding=[15, 8])
        self.style.configure("Treeview", background="#1e1e2e", foreground="white", fieldbackground="#1e1e2e", font=("Segoe UI", 10))
        self.style.configure("Treeview.Heading", background="#28283e", foreground="#00ff88", font=("Segoe UI", 9, "bold"))
        self.style.configure("TButton", background="#333355", foreground="white", padding=8, font=("Segoe UI", 9))
        self.style.map("TButton", background=[("active", "#444477")])

    def _build_ui(self):
        self._build_toolbar()
        self._build_main_area()
        self._build_status_bar()

    def _build_toolbar(self):
        toolbar = tk.Frame(self.root, bg="#1a1a2e", padx=10, pady=8)
        toolbar.pack(fill="x")
        tk.Label(toolbar, text="MT5 MONITOR", font=("Segoe UI", 18, "bold"), bg="#1a1a2e", fg="#00ff88").pack(side="left")
        btn_frame = tk.Frame(toolbar, bg="#1a1a2e")
        btn_frame.pack(side="right")

        tk.Button(btn_frame, text="+ Añadir Cuenta", bg="#00ff88", fg="#111122", font=("Segoe UI", 9, "bold"),
                  command=self._add_account_dialog, relief="flat", padx=15, pady=5, cursor="hand2").pack(side="left", padx=5)
        tk.Button(btn_frame, text="⟳ Refrescar", bg="#333355", fg="white", command=self._refresh_all,
                  relief="flat", padx=12, pady=5).pack(side="left", padx=5)
        self.monitor_btn = tk.Button(btn_frame, text="▶ Monitor", bg="#0088ff", fg="white", font=("Segoe UI", 9, "bold"),
                                     command=self._toggle_monitoring, relief="flat", padx=12, pady=5, cursor="hand2")
        self.monitor_btn.pack(side="left", padx=5)
        tk.Button(btn_frame, text="✕ Cerrar", bg="#ff4444", fg="white", command=self._on_close,
                  relief="flat", padx=12, pady=5).pack(side="left", padx=5)

    def _build_main_area(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=5)

        self.tab_accounts = tk.Frame(self.notebook, bg="#111122")
        self.tab_positions = tk.Frame(self.notebook, bg="#111122")
        self.tab_orders = tk.Frame(self.notebook, bg="#111122")
        self.tab_history = tk.Frame(self.notebook, bg="#111122")
        self.tab_logs = tk.Frame(self.notebook, bg="#111122")

        self.notebook.add(self.tab_accounts, text="  💰 Cuentas  ")
        self.notebook.add(self.tab_positions, text="  📊 Posiciones  ")
        self.notebook.add(self.tab_orders, text="  📋 Órdenes  ")
        self.notebook.add(self.tab_history, text="  📜 Historial  ")
        self.notebook.add(self.tab_logs, text="  📝 Logs  ")

        self._build_accounts_tab()
        self._build_positions_tab()
        self._build_orders_tab()
        self._build_history_tab()
        self._build_logs_tab()

    def _build_accounts_tab(self):
        canvas = tk.Canvas(self.tab_accounts, bg="#111122", highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.tab_accounts, orient="vertical", command=canvas.yview)
        self.accounts_container = tk.Frame(canvas, bg="#111122")
        self.accounts_container.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=self.accounts_container, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        canvas.bind("<MouseWheel>", lambda e: canvas.yview_scroll(int(-e.delta / 120), "units"))
        tk.Label(self.accounts_container, text="Añade tus cuentas MT5 con modo investor (lectura). Presiona '+' para añadir.",
                 font=("Segoe UI", 11), bg="#111122", fg="#555577").pack(pady=20)

    def _build_positions_tab(self):
        self.positions_tree = ttk.Treeview(self.tab_positions,
            columns=("simbolo", "tipo", "volumen", "precio", "sl", "tp", "profit"), show="headings", height=20)
        cols = [("simbolo", "Símbolo", 140), ("tipo", "Tipo", 120), ("volumen", "Volumen", 100),
                ("precio", "Precio", 120), ("sl", "Stop Loss", 110), ("tp", "Take Profit", 110),
                ("profit", "P&L", 100)]
        for col_id, col_text, col_w in cols:
            self.positions_tree.heading(col_id, text=col_text)
            self.positions_tree.column(col_id, width=col_w, anchor="center")
        style = ttk.Style()
        style.configure("Treeview", background="#1e1e2e", foreground="white", fieldbackground="#1e1e2e", font=("Segoe UI", 10))
        style.configure("Treeview.Heading", background="#28283e", foreground="#00ff88", font=("Segoe UI", 9, "bold"))
        self.positions_tree.pack(fill="both", expand=True, padx=10, pady=10)
        tk.Button(self.tab_positions, text="Limpiar", bg="#333355", fg="white",
                  command=lambda: self.positions_tree.delete(*self.positions_tree.get_children()),
                  relief="flat", font=("Segoe UI", 9)).pack(pady=5)

    def _build_orders_tab(self):
        self.orders_tree = ttk.Treeview(self.tab_orders,
            columns=("simbolo", "tipo", "volumen", "precio", "sl", "tp"), show="headings", height=20)
        cols = [("simbolo", "Símbolo", 140), ("tipo", "Tipo", 140), ("volumen", "Volumen", 100),
                ("precio", "Precio", 120), ("sl", "Stop Loss", 110), ("tp", "Take Profit", 110)]
        for col_id, col_text, col_w in cols:
            self.orders_tree.heading(col_id, text=col_text)
            self.orders_tree.column(col_id, width=col_w, anchor="center")
        style = ttk.Style()
        style.configure("Treeview", background="#1e1e2e", foreground="white", fieldbackground="#1e1e2e", font=("Segoe UI", 10))
        style.configure("Treeview.Heading", background="#28283e", foreground="#00ff88", font=("Segoe UI", 9, "bold"))
        self.orders_tree.pack(fill="both", expand=True, padx=10, pady=10)

    def _build_history_tab(self):
        self.history_tree = ttk.Treeview(self.tab_history,
            columns=("simbolo", "tipo", "volumen", "precio", "profit", "comentario"), show="headings", height=20)
        cols = [("simbolo", "Símbolo", 130), ("tipo", "Tipo", 120), ("volumen", "Volumen", 100),
                ("precio", "Precio", 120), ("profit", "P&L", 100), ("comentario", "Comentario", 130)]
        for col_id, col_text, col_w in cols:
            self.history_tree.heading(col_id, text=col_text)
            self.history_tree.column(col_id, width=col_w, anchor="center")
        style = ttk.Style()
        style.configure("Treeview", background="#1e1e2e", foreground="white", fieldbackground="#1e1e2e", font=("Segoe UI", 10))
        style.configure("Treeview.Heading", background="#28283e", foreground="#00ff88", font=("Segoe UI", 9, "bold"))
        self.history_tree.pack(fill="both", expand=True, padx=10, pady=10)

    def _build_logs_tab(self):
        self.log_text = tk.Text(self.tab_logs, bg="#0d0d1a", fg="#00ff88", font=("Consolas", 10), relief="flat", padx=10, pady=10)
        self.log_text.pack(fill="both", expand=True, padx=10, pady=10)
        ts = datetime.now().strftime("%H:%M:%S")
        self.log_text.insert("1.0", f"[{ts}] MT5 Viewer iniciado.\n")
        self.log_text.insert("1.0", f"[{ts}] Esperando cuentas...\n")
        tk.Button(self.tab_logs, text="Limpiar Logs", bg="#333355", fg="white",
                  command=lambda: self.log_text.delete("1.0", "end"), relief="flat", font=("Segoe UI", 9)).pack(pady=5)

    def _build_status_bar(self):
        self.status_bar = tk.Frame(self.root, bg="#1a1a2e", height=28)
        self.status_bar.pack(fill="x", side="bottom")
        self.status_bar.pack_propagate(False)
        self.status_label = tk.Label(self.status_bar, text="⚫ Sin conexión", font=("Segoe UI", 9), bg="#1a1a2e", fg="#888888")
        self.status_label.pack(side="left", padx=15)
        self.time_label = tk.Label(self.status_bar, text="", font=("Segoe UI", 9), bg="#1a1a2e", fg="#555577")
        self.time_label.pack(side="right", padx=15)
        self._update_time()

    def _update_time(self):
        self.time_label.config(text=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.root.after(1000, self._update_time)

    def _setup_protocols(self):
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

    def _register_callbacks(self):
        self.connector.on("connected", lambda: self._on_connected())
        self.connector.on("disconnected", lambda: self._on_disconnected())
        self.connector.on("error", lambda e: self._on_error(e))
        self.connector.on("event", lambda e: self._on_trade_event(e))
        self.connector.on("new_events", lambda e: self._on_new_events(e))

    def _load_saved_accounts(self):
        if self.config.accounts:
            colors = self.config.get_colors()
            for i, account in enumerate(self.config.accounts):
                self._add_account_card(account, colors[i % len(colors)])
            self.log_manager.add_entry("info", f"Cargadas {len(self.config.accounts)} cuenta(s)")

    def _add_account_dialog(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Añadir Cuenta MT5")
        dialog.geometry("400x420")
        dialog.configure(bg="#1e1e2e")
        dialog.transient(self.root)
        dialog.grab_set()
        fields = {}
        for label_text, var in [
            ("Nombre de Cuenta", tk.StringVar()),
            ("Login", tk.StringVar()),
            ("Contraseña (Investor)", tk.StringVar()),
            ("Servidor", tk.StringVar())
        ]:
            tk.Label(dialog, text=label_text, bg="#1e1e2e", fg="white", font=("Segoe UI", 10)).pack(pady=(12, 1), anchor="w", padx=20)
            entry = tk.Entry(dialog, textvariable=var, bg="#28283e", fg="white", font=("Segoe UI", 11), relief="flat")
            entry.pack(fill="x", padx=20, pady=(0, 8))
            fields[label_text] = var

        def on_add():
            nombre = fields["Nombre de Cuenta"].get().strip()
            login_str = fields["Login"].get().strip()
            password = fields["Contraseña (Investor)"].get().strip()
            servidor = fields["Servidor"].get().strip()
            if not all([nombre, login_str, password, servidor]):
                messagebox.showwarning("Campos incompletos", "Rellena todos los campos.")
                return
            try:
                login_int = int(login_str)
            except ValueError:
                messagebox.showwarning("Login inválido", "El login debe ser un número.")
                return
            account = self.config.add_account(nombre, login_int, password, servidor)
            color = self.config.get_colors()[len(self.config.accounts) - 1]
            self._add_account_card(account, color)
            self.log_manager.add_entry("add", f"Cuenta '{nombre}' añadida")
            dialog.destroy()
            self.notifier.notify(NotifLevel.INFO, "Cuenta Añadida", f"'{nombre}' agregada correctamente", timeout=5)

        tk.Button(dialog, text="Añadir Cuenta", bg="#00ff88", fg="#111122", font=("Segoe UI", 11, "bold"),
                  command=on_add, relief="flat", padx=30, pady=8, cursor="hand2").pack(pady=10)

    def _edit_account_dialog(self, account: SavedAccount, frame: tk.Frame):
        dialog = tk.Toplevel(self.root)
        dialog.title("Editar Cuenta MT5")
        dialog.geometry("400x420")
        dialog.configure(bg="#1e1e2e")
        dialog.transient(self.root)
        dialog.grab_set()
        fields = {}
        for label_text, var, val in [
            ("Nombre de Cuenta", tk.StringVar(value=account.nombre), account.nombre),
            ("Login", tk.StringVar(value=str(account.login)), str(account.login)),
            ("Contraseña (Investor)", tk.StringVar(value=account.password), account.password),
            ("Servidor", tk.StringVar(value=account.servidor), account.servidor)
        ]:
            tk.Label(dialog, text=label_text, bg="#1e1e2e", fg="white", font=("Segoe UI", 10)).pack(pady=(12, 1), anchor="w", padx=20)
            entry = tk.Entry(dialog, textvariable=var, bg="#28283e", fg="white", font=("Segoe UI", 11), relief="flat")
            entry.pack(fill="x", padx=20, pady=(0, 8))
            fields[label_text] = var

        color_var = tk.StringVar(value=account.color)
        tk.Label(dialog, text="Color", bg="#1e1e2e", fg="white", font=("Segoe UI", 10)).pack(anchor="w", padx=20)
        color_frame = tk.Frame(dialog, bg="#1e1e2e")
        color_frame.pack(fill="x", padx=20, pady=(0, 10))
        color_options = self.config.get_colors()
        color_menu = ttk.Combobox(color_frame, textvariable=color_var, values=color_options,
                                   state="readonly", font=("Segoe UI", 10), width=15)
        color_menu.pack(side="left")
        swatch = tk.Label(color_frame, bg=account.color, width=3, height=1, relief="solid", bd=1)
        swatch.pack(side="left", padx=10)
        color_var.trace_add("write", lambda *args: swatch.configure(bg=color_var.get()))

        index = None
        for i, acc in enumerate(self.config.accounts):
            if acc.login == account.login:
                index = i
                break

        def on_edit():
            nombre = fields["Nombre de Cuenta"].get().strip()
            login_str = fields["Login"].get().strip()
            password = fields["Contraseña (Investor)"].get().strip()
            servidor = fields["Servidor"].get().strip()
            if not all([nombre, login_str, password, servidor]):
                messagebox.showwarning("Campos incompletos", "Rellena todos los campos.")
                return
            try:
                login_int = int(login_str)
            except ValueError:
                messagebox.showwarning("Login inválido", "El login debe ser un número.")
                return
            color = color_var.get()
            if self.config.update_account(index, nombre, login_int, password, servidor, color):
                self._account_colors.pop(account.login, None)
                self._account_colors[login_int] = color
                self._connectors.pop(account.login, None)
                self._add_account_card(self.config.get_account(index), color)
                frame.destroy()
                self.log_manager.add_entry("edit", f"Cuenta '{nombre}' (login {login_int}) modificada")
                self.notifier.notify(NotifLevel.INFO, "Cuenta Editada", f"'{nombre}' actualizada", timeout=5)
                dialog.destroy()

        tk.Button(dialog, text="Guardar Cambios", bg="#ffcc00", fg="#111122", font=("Segoe UI", 11, "bold"),
                  command=on_edit, relief="flat", padx=30, pady=8, cursor="hand2").pack(pady=10)

    def _add_account_card(self, account: SavedAccount, color: str):
        frame = tk.Frame(self.accounts_container, bg="#111122")
        frame.pack(fill="x", padx=10, pady=8)
        connector = MT5Connector()
        self._connectors[account.login] = connector
        self._account_colors[account.login] = color
        account_info = AccountInfo(
            login=account.login, nombre=account.nombre, servidor=account.servidor,
            compania="MT5", saldo=0.0, equity=0.0, margin=0.0, margin_free=0.0,
            margin_level=0.0, profit=0.0, gross_profit=0.0, gross_loss=0.0,
            commission=0.0, swap=0.0, leverage=100, balance=0.0, credito=0.0
        )
        card = AccountCard(frame, account_info, color, connector, on_click=self._on_card_click)
        card.pack(fill="x", expand=True)
        card.connector = connector

        btn_frame = tk.Frame(frame, bg="#111122")
        btn_frame.pack(side="right", fill="y", padx=5, pady=5)

        edit_btn = tk.Button(btn_frame, text="✎ Editar", bg="#0088ff", fg="white",
                              font=("Segoe UI", 9, "bold"),
                              command=lambda a=account, c=frame: self._edit_account_dialog(a, c),
                              relief="flat", padx=10, pady=4, cursor="hand2")
        edit_btn.pack(side="left", padx=2)

        remove_btn = tk.Button(btn_frame, text="🗑", bg="#ff4444", fg="white", font=("Segoe UI", 9),
                                command=lambda: self._remove_account(account.login, frame),
                                relief="flat", padx=8, pady=4, cursor="hand2")
        remove_btn.pack(side="left", padx=2)

        connect_btn = tk.Button(btn_frame, text="🔌", bg="#00ff88" if connector.state != ConnectionState.CONNECTED else "#ff8800",
                                 fg="#111122", font=("Segoe UI", 9, "bold"),
                                 command=lambda a=account: self._connect_account_with_info(a),
                                 relief="flat", padx=8, pady=4, cursor="hand2")
        connect_btn.pack(side="left", padx=2)
        self._connectors[account.login] = connector

    def _on_card_click(self, card):
        pass

    def _connect_account_with_info(self, account: SavedAccount):
        login = account.login
        connector = self._connectors.get(login)
        if connector and connector.state == ConnectionState.CONNECTED:
            connector.disconnect()
            self._update_status("⚫ Desconectado", "#888888")
            self.monitor_btn.config(text="▶ Monitor", bg="#0088ff")
            self._monitoring = False
            return
        if connector is None:
            connector = MT5Connector()
            self._connectors[login] = connector
        success = connector.connect(login, account.password, account.servidor)
        if success:
            self._update_status(f"🟢 {account.nombre}", "#00ff88")
            self._update_tabs(connector)
            self.log_manager.add_entry("connect", f"Conectado a {account.nombre}")
            self.notifier.on_connection_change("connected")
        else:
            self._update_status(f"🔴 Error: {account.nombre}", "#ff4444")
            self.log_manager.add_entry("error", f"Error conexión {account.nombre}")
            self.notifier.on_connection_change("error")

    def _update_tabs(self, connector: MT5Connector):
        self._populate_positions(connector)
        self._populate_orders(connector)
        self._populate_history(connector)
        summary = connector.get_summary()
        summary["nombre"] = ""
        self.log_manager.add_entry("data", f"Datos actualizados | Equity: ${summary['equity']:.2f} | P&L: ${summary['profit']:.2f}")

    def _update_account_card(self, login: int, summary: dict):
        pass

    def _refresh_all(self):
        for login, connector in self._connectors.items():
            if connector.state == ConnectionState.CONNECTED:
                connector.refresh_data()
                self._update_tabs(connector)
        self._update_status("⟳ Refrescado", "#00ccff")
        self.log_manager.add_entry("refresh", "Refresco de datos completo")
        self.notifier.on_account_update({k: v for k, v in self._connectors[list(self._connectors.keys())[0]].get_summary().items()} if self._connectors else {})

    def _toggle_monitoring(self):
        if self._monitoring:
            self._stop_monitoring()
        else:
            self._start_monitoring()

    def _start_monitoring(self):
        self._monitoring = True
        for connector in self._connectors.values():
            if connector.state == ConnectionState.CONNECTED:
                connector.start_polling(interval=5)
        self.monitor_btn.config(text="■ Detener", bg="#ff4444")
        self._update_status("📡 Monitor activo", "#ffcc00")
        self.log_manager.add_entry("monitor", "Monitor iniciado")
        self.notifier.notify(NotifLevel.INFO, "Monitor Activado", "Detección de eventos iniciada", timeout=5)

    def _stop_monitoring(self):
        self._monitoring = False
        for connector in self._connectors.values():
            connector.stop_polling()
        self.monitor_btn.config(text="▶ Monitor", bg="#0088ff")
        self._update_status("⚫ Monitor detenido", "#888888")
        self.log_manager.add_entry("monitor", "Monitor detenido")

    def _update_status(self, text: str, color: str):
        self.status_label.config(text=text, fg=color)

    def _on_connected(self):
        self._update_status("🟢 Conectado", "#00ff88")
        self.log_manager.add_entry("connected", "Conexión establecida")

    def _on_disconnected(self):
        self._update_status("⚫ Desconectado", "#888888")
        self.log_manager.add_entry("disconnected", "Conexión cerrada")

    def _on_error(self, error: str):
        self._update_status(f"🔴 Error", "#ff4444")
        self.log_manager.add_entry("error", error)

    def _on_trade_event(self, events):
        if isinstance(events, list):
            for evt in events:
                self.log_manager.add_entry("trade", f"{evt.simbolo}: {evt.tipo_operacion} {evt.estado}", {"ticket": evt.ticket, "profit": evt.profit})
                if evt.estado == "CLOSED":
                    self.notifier.on_close_position({"simbolo": evt.simbolo, "ticket": evt.ticket}, evt.profit)
                elif evt.estado == "OPEN":
                    self.notifier.on_new_position({"simbolo": evt.simbolo, "tipo": evt.tipo_operacion, "volumen": evt.volumen, "precio": evt.precio, "ticket": evt.ticket})
        for login, connector in self._connectors.items():
            if connector.state == ConnectionState.CONNECTED:
                self._update_tabs(connector)

    def _on_new_events(self, events):
        if events:
            self.log_manager.add_entry("events", f"{len(events)} nuevo(s) evento(s) detectado(s)")

    def _populate_positions(self, connector: MT5Connector):
        for item in self.positions_tree.get_children():
            self.positions_tree.delete(item)
        for pos in connector.posiciones_abiertas:
            profit_color = "#00ff88" if pos.profit >= 0 else "#ff4444"
            self.positions_tree.insert("", "end", values=(pos.simbolo, pos.tipo_operacion, pos.volumen, f"{pos.precio:.5f}", f"{pos.stop_loss:.5f}", f"{pos.take_profit:.5f}", f"{pos.profit:+.2f}"))

    def _populate_orders(self, connector: MT5Connector):
        for item in self.orders_tree.get_children():
            self.orders_tree.delete(item)
        for order in connector.ordenes_pendientes:
            self.orders_tree.insert("", "end", values=(order.simbolo, order.tipo_operacion, order.volumen, f"{order.precio:.5f}", f"{order.stop_loss:.5f}", f"{order.take_profit:.5f}"))

    def _populate_history(self, connector: MT5Connector):
        for item in self.history_tree.get_children():
            self.history_tree.delete(item)
        for hist in sorted(connector.historico, key=lambda x: x.timestamp, reverse=True)[:50]:
            self.history_tree.insert("", "end", values=(hist.simbolo, hist.tipo_operacion, hist.volumen, f"{hist.precio:.5f}", f"{hist.profit:+.2f}", hist.comentario))

    def _remove_account(self, login: int, frame: tk.Frame):
        if not messagebox.askyesno("Confirmar eliminación", "¿Seguro que deseas eliminar esta cuenta?"):
            return
        index = None
        for i, acc in enumerate(self.config.accounts):
            if acc.login == login:
                index = i
                break
        if index is not None:
            self.config.remove_account(index)
        connector = self._connectors.pop(login, None)
        if connector and connector.state == ConnectionState.CONNECTED:
            connector.disconnect()
        frame.destroy()
        self._update_status("Cuenta eliminada", "#ffcc00")
        self.log_manager.add_entry("remove", f"Cuenta con login {login} eliminada")
        self.notifier.notify(NotifLevel.WARNING, "Cuenta Eliminada", f"Cuenta {login} borrada", timeout=5)

    def _on_close(self):
        for connector in self._connectors.values():
            connector.disconnect()
        self.root.destroy()

    def run(self):
        self.root.mainloop()


def main():
    app = MT5ViewerApp()
    app.run()


if __name__ == "__main__":
    main()