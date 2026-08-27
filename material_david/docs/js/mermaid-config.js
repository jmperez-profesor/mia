// Los diagramas Mermaid del sitio (no del PDF, que usa mmdc por separado, ver hooks.py)
// se calculan a partir del tamaño de letra: Material inicializa Mermaid con el fontSize
// por defecto (16px), y cada diagrama sencillo (pocos nodos) queda con un tamaño natural
// pequeño que `max-width:100%` no agranda, solo evita que desborde el contenedor.
// Subir el fontSize un 50% (16 -> 24) agranda proporcionalmente cajas y espaciado de
// cualquier diagrama; los que ya llenaban el ancho del contenedor se quedan igual,
// porque siguen topando con ese mismo `max-width:100%`.
(function () {
    function bumpMermaidFontSize() {
        if (typeof mermaid === "undefined") {
            setTimeout(bumpMermaidFontSize, 50);
            return;
        }
        mermaid.initialize({
            fontSize: 24,
            sequence: {
                actorFontSize: "24px",
                messageFontSize: "24px",
                noteFontSize: "24px"
            }
        });
    }

    if (typeof document$ !== "undefined") {
        document$.subscribe(bumpMermaidFontSize);
    } else {
        document.addEventListener("DOMContentLoaded", bumpMermaidFontSize);
    }
})();
