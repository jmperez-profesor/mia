# UD02 · Taller 1 — Documentar con Markdown

!!! important "Entrega · hecho / no hecho"
    Se entrega en Moodle y se califica como **hecho / no hecho**: no lleva nota ni ítem en el
    libro de calificaciones, pero **es requisito**. La memoria de [`T04` Robocode](UD02_T04_Robocode_ES.md) se
    escribe y documenta más rápido si dominas Markdown, y es el lenguaje en el que están escritos
    estos mismos apuntes.

**Objetivo**: aprender la sintaxis de Markdown lo bastante a fondo como para documentar cualquier
proyecto — texto, listas, tablas, enlaces, imágenes y código — y escribir un documento propio de
principio a fin.

!!! note "Qué es y para qué sirve"
    **Markdown** es un lenguaje de marcado ligero creado en 2004 por John Gruber para convertir
    texto plano en HTML de forma sencilla y legible incluso sin procesar. Se usa hoy en foros
    (Stack Overflow), gestores de tareas (Trello), documentación técnica (GitHub, estos apuntes) y
    apps de notas — es **transportable**: el mismo `.md` se lee y edita en cualquier plataforma sin
    depender de un procesador de textos propietario. Editores habituales: **Typora**, VS Code (con
    previsualización integrada) o directamente el editor web de GitHub.

### Fase 1 — Texto básico: párrafos, énfasis y encabezados

Un párrafo nuevo se crea con una línea en blanco entre dos bloques de texto — Markdown, como HTML,
**colapsa las líneas en blanco dobles** en una sola. Para forzar un salto de línea dentro del mismo
párrafo, termina la línea con dos espacios.

```markdown
Este texto es en **negrita**.
Este texto es en *cursiva*.
Este texto está ~~tachado~~.
Este texto es en ambos ***negrita y cursiva***.
```

Los encabezados usan `#` — uno por nivel, del `#` (H1) al `######` (H6):

```markdown
# Encabezado 1
## Encabezado 2
### Encabezado 3
```

### Fase 2 — Listas, tablas, enlaces e imágenes

**Listas** ordenadas (`1.`), no ordenadas (`-`, `*` o `+`, sin mezclar dentro de la misma lista) y
de tareas:

```markdown
1. Primer paso
2. Segundo paso

- Elemento A
- Elemento B

- [x] Tarea completada
- [ ] Tarea pendiente
```

**Tablas**, con `|` para columnas y `---` para separar el encabezado:

```markdown
| Columna 1 | Columna 2 |
|---|---|
| dato 1.1 | dato 1.2 |
```

**Enlaces** e **imágenes** comparten sintaxis; la imagen añade `!` delante:

```markdown
[texto del enlace](https://ejemplo.com)
![texto alternativo](ruta/imagen.png)
```

### Fase 3 — Código, citas y separadores

Para código **en línea**, una comilla invertida a cada lado: `` `código` ``. Para un **bloque**, tres
comillas invertidas con el nombre del lenguaje:

````markdown
```python
print("Hola, mundo")
```
````

Las citas empiezan por `>`:

```markdown
> No hay que ir para atrás, ni para darse impulso. — Lao Tsé.
```

!!! important "En estos apuntes, las citas `>` no se usan para notas"
    Es una convención de este curso: toda nota, aviso o definición destacada va en una
    **admonición** (`!!! tip`, `!!! note`, `!!! warning`...), como las de esta misma página — no en
    una cita `>`. Reserva `>` para citar literalmente a alguien, como en el ejemplo de Lao Tsé.

Una línea horizontal de separación se crea con tres guiones en su propia línea: `---`.

!!! caution "Diagramas: `flow`/`sequence` frente a Mermaid"
    Algunos editores de Markdown (Typora entre ellos) admiten bloques ` ```flow ` o
    ` ```sequence ` para diagramas de flujo y de secuencia con su propia sintaxis. **El sitio de
    esta asignatura no los renderiza**: usa **Mermaid** (` ```mermaid `), que sí verás en la teoría
    de cada unidad. Si trabajas en Typora para tus propios apuntes puedes usar cualquiera de los
    dos; para lo que entregues en este curso, usa Mermaid.

### Fase 4 — Practica: documento sobre ti mismo

Con tu editor favorito, crea un documento Markdown que:

1. Tenga un título y, si tu editor lo soporta, un índice (`[TOC]`).
2. Incluya **4 encabezados principales** — por ejemplo *Datos*, *Currículum*, *Aficiones* y *Otros
   datos de interés* (no hace falta que sea información real; puedes inventarla).
3. Use al menos: negrita, cursiva, una lista ordenada, una lista no ordenada, un enlace, una
   imagen, una cita y un bloque de código.
4. *Opcional, para nota extra*: un diagrama Mermaid con los pasos de una mañana de sábado.

Exporta el resultado a PDF (la mayoría de editores Markdown lo hacen con un clic, o usa
`pandoc documento.md -o documento.pdf`).

### Entrega del Taller 1

| Fase | Evidencia mínima |
|---|---|
| 1-3 | El documento `.md` usa correctamente encabezados, énfasis, listas, tabla, enlace, imagen, cita y bloque de código |
| 4 | El documento tiene 4 encabezados principales con contenido propio |
| Extra | Diagrama Mermaid incluido (no obligatorio) |

Sube a Moodle el documento **`.md`** original y su exportación a **`.pdf`**.

!!! note "Soluciones"
    No aplica: es un documento de creación libre, se comenta en clase con ejemplos del alumnado.

---
[Volver a la UD02](UD02_ES.md) · [Taller 2](UD02_T02_GitHub_ES.md) · [Ejercicios](UD02_Ejercicios.md)
