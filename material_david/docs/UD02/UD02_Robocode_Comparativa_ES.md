# UD02 · Comparativa Java vs Python para Robocode

Robocode Tank Royale (RCTR) ofrece API oficial para múltiples lenguajes. En esta unidad podéis elegir entre **Java (JVM)** y **Python**. A continuación se detallan las diferencias, ventajas e inconvenientes de cada opción.

## ¿Por qué dos lenguajes?

RCTR v0.34.0 introdujo la API multilingüe. El proyecto Robocode nació en Java, pero la comunidad y la evolución del software han traído soporte para Python, .NET y TypeScript. Esto permite elegir el lenguaje que mejor se adapte a vuestro perfil y a los objetivos del curso.

## Tabla comparativa

| Aspecto | Java | Python |
|---|---|---|
| **Entorno requerido** | JDK 11-23 + IntelliJ IDEA + Maven | Python 3.10+ + VS Code + pip |
| **Dependencias** | `pom.xml` (Maven) o JAR manual | `pip install robocode-tank-royale` |
| **Sintaxis API** | `camelCase()` — `setTurnLeft()`, `onScannedBot()` | `snake_case()` — `set_turn_left()`, `on_scanned_bot()` |
| **Tipado** | Estático (obligatorio) | Dinámico (opcional, con type hints) |
| **Proyecto starter** | ZIP preempaquetado (`IABDBotMaven.zip`) | Manual: 4 ficheros (`.py` + `.json` + `.cmd` + `.sh`) |
| **Conf. servidor** | Variables de entorno en configuración de ejecución de IntelliJ | Variables de entorno `SERVER_SECRET` y `SERVER_URL` en terminal |
| **Curva aprendizaje** | Más pronunciada (JDK, Maven, IDE pesado) | Más suave (pip, editor ligero) |
| **Rendimiento batalla** | Compilado JIT (mayor velocidad) | Interpretado (suficiente para RCTR, pero menor rendimiento) |
| **Ecosistema IA/ML** | Limitado para IA aplicada | Rico: scikit-learn, PyTorch, TensorFlow, etc. |
| **Documentación comunitaria** | RoboWiki mayoritariamente en Java | RoboWiki en Java (traducción a Python necesaria) |
| **Uso en CE IA&BD** | Transversal (programación genérica) | **Alineado** (Python es el lenguaje de referencia en IA) |
| **API RCTR** | Madura (existe desde el origen) | Estable (v0.34.0+, en evolución) |

## Ejemplos de código comparativos

### Clase Bot e imports

=== "Java"
    ```java
    import dev.robocode.tankroyale.botapi.*;
    import dev.robocode.tankroyale.botapi.events.*;

    public class MiBot extends Bot {
        MiBot() {
            super(BotInfo.fromFile(getConfigPath()));
        }
    
        private static String getConfigPath() {
            String configPath = "src/main/java/MiBot.json";
            java.io.File configFile = new java.io.File(configPath);
            if (!configFile.exists()) {
                configPath = "MiBot.json";
            }
            return configPath;
        }
    }
    ```

=== "Python"
    ```python
    from robocode_tank_royale.bot_api import Bot, BotInfo

    class MiBot(Bot):
        def __init__(self):
            super().__init__(BotInfo.from_file("MiBot.json"))
    ```

### Método `run()` y bucle principal

=== "Java"
    ```java
    public void run() {
        setAdjustRadarForBodyTurn(true);
        setAdjustGunForBodyTurn(true);
        setAdjustRadarForGunTurn(true);

        while (isRunning()) {
            setTurnRadarLeft(Double.POSITIVE_INFINITY);
            forward(100);
            turnGunLeft(360);
            back(100);
            turnGunLeft(360);
        }
    }
    ```

=== "Python"
    ```python
    def run(self):
        self.set_adjust_radar_for_body_turn(True)
        self.set_adjust_gun_for_body_turn(True)
        self.set_adjust_radar_for_gun_turn(True)

        while self.is_running:  # type: ignore[attr-defined]  # pylint: disable=no-member
            self.set_turn_radar_left(float("inf"))
            self.forward(100)
            self.turn_gun_left(360)
            self.back(100)
            self.turn_gun_left(360)
    ```

### Event handler `onScannedBot`

=== "Java"
    ```java
    public void onScannedBot(ScannedBotEvent e) {
        fire(1);
    }
    ```

=== "Python"
    ```python
    def on_scanned_bot(self, scanned_bot_event: ScannedBotEvent):
        del scanned_bot_event
        self.fire(1)
    ```

### Disparo predictivo (trigonométrico)

=== "Java"
    ```java
    public void onScannedBot(ScannedBotEvent e) {
        double enemyDistance = distanceTo(e.getX(), e.getY());
        double firePower = Math.min(500 / enemyDistance, 3);
        double bulletSpeed = 20 - firePower * 3;
        long time = (long) (enemyDistance / bulletSpeed);

        double enemyVelocity = e.getSpeed();
        double enemyDirection = e.getDirection();
        double deltaX = enemyVelocity * Math.cos(Math.toRadians(enemyDirection));
        double deltaY = enemyVelocity * Math.sin(Math.toRadians(enemyDirection));
        double futureX = e.getX() + (deltaX * time);
        double futureY = e.getY() + (deltaY * time);
    
        setTurnGunLeft(gunBearingTo(futureX, futureY));
        if (getGunTurnRemaining() <= 0 && getGunHeat() == 0) {
            fire(firePower);
        }
    }
    ```

=== "Python"
    ```python
    def on_scanned_bot(self, e: ScannedBotEvent):
        enemy_distance = self.distance_to(e.x, e.y)
        fire_power = min(500 / enemy_distance, 3)
        bullet_speed = 20 - fire_power * 3
        time = int(enemy_distance / bullet_speed)

        enemy_velocity = e.speed
        enemy_direction = e.direction
        delta_x = enemy_velocity * math.cos(math.radians(enemy_direction))
        delta_y = enemy_velocity * math.sin(math.radians(enemy_direction))
        future_x = e.x + (delta_x * time)
        future_y = e.y + (delta_y * time)
    
        self.set_turn_gun_left(self.gun_bearing_to(future_x, future_y))
        if self.gun_turn_remaining <= 0 and self.gun_heat == 0:
            self.fire(fire_power)
    ```

## Ventajas e inconvenientes

### Java

**Ventajas:**

  - Documentación histórica amplia (RoboWiki, ejemplos clásicos)
  - Proyecto starter preempaquetado (descomprimir y abrir en IntelliJ)
  - Rendimiento compilado mayor en cálculos intensivos
  - API muy madura y estable

**Inconvenientes:**

  - Requerimientos de entorno pesados (JDK + IntelliJ)
  - Curva de aprendizaje mayor si no se conoce Java/Maven
  - Menos alineado con el ecosistema de IA y Big Data del curso
  - Configuración de ejecución dependiente del IDE

### Python

**Ventajas:**

  - Instalación sencilla (`pip install`)
  - Editor ligero (VS Code) y rápido de configurar
  - Sintaxis limpia y legible
  - Alineado con el resto del curso (ecosistema IA/BD)
  - Mejor integración con librerías de IA si se quiere ampliar el bot
  - Variables de entorno simples (terminal o script)

**Inconvenientes:**

  - Documentación histórica en Java (hay que traducir conceptualmente)
  - Proyecto starter manual (4 ficheros) en lugar de ZIP preempaquetado
  - Rendimiento interpretado (normalmente no perceptible en RCTR)

## Recomendación

Para la naturaleza de este curso de especialización en **Inteligencia Artificial y Big Data**, se recomienda el uso de **Python** como lenguaje principal. Python es la herramienta estándar de la industria en IA/ML, y su sintaxis clara permite centrarse en las estrategias del bot en lugar de la infraestructura del lenguaje.

La opción Java queda disponible para alumnado con experiencia previa en Java o interés particular, pero la vía Python será la que reciba soporte preferente por parte del profesorado.

!!! tip "Elegid vuestro camino"
    - **Noveles en programación o provenientes de Python** → seguid la guía Python
    - **Experiencia previa en Java o interés en JVM** → seguid la guía Java
    - **Dudas** → consultad al profesorado
