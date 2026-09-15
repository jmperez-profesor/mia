Déjame revisar el material de partida https://martinezpenya.es/ModelosIA/UD05/UD05_ES.html y tus convenciones de autoría.Tengo el material de David Martínez. Ahora voy a verificar el estado actual del mercado y, sobre todo, a ejecutar en el sandbox todo el código que vaya a incluir.Perfecto, `experta` funciona con el parche. Ahora construyo y ejecuto el resto del stack.Esa salida contiene un fallo real muy didáctico (dos decisiones contradictorias). Preparo la versión corregida para enseñar el porqué.Ahora el motor de decisión moderno (GoRules ZEN, el que se usa hoy en producción):Todo el stack convive sin conflictos. Escribo ya los apuntes.Verifico que lo que pido en la actividad A2 es realmente factible antes de dejarlo escrito: Última comprobación: valido la sintaxis de todos los bloques de código tal como quedan en el documento.Aquí tienes la unidad completa. Un aviso primero: **el PDF no llegó** (la carpeta de subidas estaba vacía), así que he trabajado sobre la versión web de la UD05 de David Martínez, que está actualizada a agosto de 2026 y cubre lo mismo.

## Qué he hecho

He reescrito los apuntes con un eje distinto al de David. Su UD05 va de *sistemas expertos → controladores inteligentes* (PID, difusa, control de procesos), porque su RA5 lo exige. Como tú pides **sistemas expertos y motores de regla con foco en el mercado actual**, el eje es otro: *sistema experto clásico → motor de decisiones de negocio → híbrido con ML y LLM*. La lógica difusa queda fuera (David ya la trata en UD02/RA2) y entra todo lo que él solo menciona de pasada: BRMS, DMN, tablas de decisión, verificación de bases de reglas y guardarraíles.

Todo el código está ejecutado en sandbox y las salidas pegadas son reales. Los 13 bloques Python los he vuelto a extraer del propio Markdown y a ejecutar uno a uno para verificar que lo que aparece en los apuntes funciona tal cual.

## Estructura (4 sesiones de 2 h)

| Sesión | Contenido |
|---|---|
| 1 | Por qué reglas en 2026, anatomía, ciclo reconocer-actuar, **micro-motor propio en 35 líneas**, encadenamiento hacia atrás |
| 2 | `experta` (con parche), RETE/PHREAK, sensibilidad y umbrales, factores de certeza, `clipspy` |
| 3 | Decision management, tablas de decisión y hit policy, DMN, **GoRules ZEN**, `rule-engine`, verificador de cobertura, benchmark |
| 4 | Reglas extraídas de datos (FIGS), guardarraíles de agentes LLM, neuro-simbólico, AI Act, proyecto integrador |

Hilo conductor único: Pagarium, una pasarela de pagos que decide sobre transacciones. Cada sesión añade una capa sobre el mismo dominio.

## Tres decisiones de diseño que conviene que revises

**El motor casero falla a propósito.** En el apartado 7 el motor emite dos decisiones contradictorias sobre el mismo pago. No es un error de transcripción: es la salida real, y la uso como puerta de entrada al razonamiento no monótono y a la estratificación por salience. Es el mejor momento didáctico de la unidad.

**`experta` se enseña, pero no se recomienda.** Está sin mantener desde 2019 y necesita el parche de `collections.Mapping`. Presento `clipspy` (CLIPS 6.4, mantenido) como lo que llevarías a producción, y `zen-engine` como lo que realmente se usa hoy en fintech. El benchmark lo respalda con números medidos: 190 µs/pago en `experta`, 96 en CLIPS, 54 en ZEN y 0,1 en un `if/else`. Esa última cifra está ahí para que los alumnos no salgan pensando que un motor de reglas siempre es la respuesta.

**FIGS redescubre la política latente.** Genero 4.000 pagos con una regla oculta (`importe > 1000 y antigüedad < 6`, o `n_intentos >= 4`) más 3 % de ruido, y FIGS la recupera casi literal: `importe > 997.45`, `antiguedad <= 5.5`, `n_intentos > 3.5`. Funciona muy bien para explicar la relación entre extracción de reglas y sesión con negocio.

Sobre el AI Act he verificado el calendario, porque cambió hace poco: el Ómnibus Digital (Reglamento UE 2026/1744) aplazó las obligaciones de alto riesgo del Anexo III a diciembre de 2027, pero transparencia y alfabetización siguen vigentes desde agosto de 2026.

Las actividades suman 10: A1 (1,5), A2 (2), A3 (3) y proyecto (3,5). Antes de dejar A2 escrita comprobé que `not` en CLIPS, `watch rules` y `self.retract()` en `experta` hacen lo que pido.

Ojo, el módulo está planificado para sesiones de 2 horas presenciales, en el anexo 26 está la repartición alternativa.