# UD00 · Ejercicios de autoevaluación

!!! note "Cómo se trabajan"
    Resuélvelos en tu cuaderno o en un documento Markdown, a tu ritmo. Si te atascas en alguno,
    pregunta en clase o por Moodle: el profesor te da la solución. (El **notebook** de la unidad
    es un entregable aparte, con su propia entrega — ver [Recursos](UD00_ES.md#16-recursos).)

## A. Sobre el módulo y la evaluación

1. Cita los **7 RA** del módulo y asocia cada uno con su número.
2. ¿Cuántas horas tiene el módulo? ¿Cuántas semanas y a qué ritmo semanal?
3. Explica cómo se calcula la nota final del módulo (pesos de RA1-RA6 y RA7).
4. ¿Es el RA7 un caso especial a la hora de superar el módulo? Razona tu respuesta.
5. ¿Por qué el contenido del módulo debe **finalizar a finales de abril**?
6. Indica cuándo se hacen las **evaluaciones parciales** y qué RAs cubren cada una.
7. ¿Qué herramientas usaremos como entorno de trabajo durante el curso? Describe brevemente cada una.

## B. Conceptos de Docker

8. Diferencia **imagen** y **contenedor** con un ejemplo.
9. Explica el papel del **daemon**, del **cliente** y de los **registros** en la arquitectura de Docker.
10. Enumera dos ventajas de los contenedores frente a las máquinas virtuales y una situación en la que convenga usar ambas.
11. ¿Qué hace exactamente `docker run` cuando la imagen aún no está descargada? Describe los pasos.
12. ¿Qué ocurre con los datos de un contenedor cuando lo eliminas? ¿Cómo los conservas?
13. ¿Cuál es la diferencia entre `docker stop`, `docker rm` y `docker rmi`?
14. Explica con tus palabras qué ocurre al ejecutar `docker run hello-world` la primera vez.

## C. Dockerfile

15. ¿Por qué un Dockerfile debe empezar por `FROM`?
16. Diferencia `RUN`, `CMD` y `ENTRYPOINT`.
17. Escribe un `Dockerfile` que parta de `python:3.12-slim`, copie `requirements.txt` y `app.py`, instale las dependencias y ejecute la app.
18. ¿Por qué se recomienda copiar `requirements.txt` antes que el resto del código? ¿Qué relación tiene con las capas?
19. ¿Qué es un `.dockerignore` y para qué sirve?
20. Dado el `Dockerfile` anterior, escribe los comandos para **construir** la imagen y para **ejecutarla** publicando el puerto 8000.

## D. Docker Compose

21. ¿Qué ventaja aporta `docker-compose.yml` frente a varios `docker run`?
22. Escribe un `compose.yaml` con un servicio `jupyter` que publique el puerto `8888`, monte la carpeta `./practicas` y use el token `cursoia`.
23. Explica la diferencia entre `docker compose up -d`, `docker compose down` y `docker compose down -v`.
24. ¿Para qué sirven los comandos `docker compose config`, `docker compose logs -f` y `docker compose exec`?
25. ¿Cómo se ordena el arranque de servicios en Compose? ¿Qué papel juegan los **healthchecks**?
26. ¿Cómo se conservan los datos con Compose? ¿Qué hace la clave `volumes` de nivel superior?

## E. Prácticos

27. Levanta un contenedor `python:3.12` interactivo y escribe un programa que imprima
    `Hola desde Docker`. ¿Qué comando usas para entrar y para salir?
28. Levanta `nginx` en segundo plano en el puerto `8080` y comprueba en tu navegador que responde. ¿Cómo lo detienes y lo eliminas?
29. Crea una carpeta `practicas`, monta esa carpeta en un contenedor `python:3.12` y ejecuta desde dentro un archivo `app.py` que hayas escrito en el host.
30. Escribe el `docker-compose.yml` del taller 2, levanta Jupyter y abre la URL en el navegador.

## F. Instalación, versiones y mantenimiento

31. Tras ejecutar `sudo usermod -aG docker $USER`, ¿por qué hay que **cerrar y volver a abrir la
    sesión**? ¿Qué mensaje de error aparece si no lo haces?
32. El mismo `pip install experta` funciona en `python:3.9-slim` y falla al **importar** en
    `python:3.12-slim`. Explica la causa, qué hace el parche de tres líneas y por qué el problema
    no aparece al instalar sino al importar.
33. Diferencia `docker save`/`docker load` de `docker export`/`docker import`. ¿Cuál conserva el
    historial de capas de la imagen y por qué importa?
34. Tienes 12 GB ocupados en imágenes. Explica qué hace `docker image prune -a`, en qué se
    diferencia de borrar por identificador y qué riesgo tiene ejecutarlo sin mirar.

## Soluciones

!!! note "Soluciones"
    Las soluciones no se publican: se corrigen y comentan en clase.

---
[Volver a la UD00](UD00_ES.md) · [Taller 1](UD00_T01_Verificacion_entorno_ES.md) · [Taller 2](UD00_T02_Contenedor_practicas_ES.md)
