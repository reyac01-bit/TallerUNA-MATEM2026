# Prompt de Seis R completado — Modelo D (ejemplo para la Guía del E4)

Este es el prompt tal como se pega en ChatGPT, Claude o Gemini, seguido del contenido de estilo_matia.py.

---

ROL
Actuá como especialista en educación matemática de secundaria y programador experto en Manim Community Edition (v0.19 o superior) con manim-voiceover. Trabajás para la serie de videos "MatIA" de MATEM-UNA Precálculo 2026, que ya tiene una identidad visual y de voz definida en el archivo estilo_matia.py (no debés modificarla ni redefinirla).

RESULTADO
Entregá únicamente un archivo Python llamado video_inversa_reflexion.py que defina UNA clase InversaReflexion(VideoMatIA) con el método construct, que produzca un video narrado de entre 60 y 120 segundos sobre:

   La gráfica de la función inversa es la reflexión de la gráfica de f respecto a la recta y = x, porque cada par (a, b) de f se convierte en (b, a) de f⁻¹; esa reflexión solo es una función cuando f es inyectiva.

Estructura obligatoria en 4 a 6 ESCENAS (cada escena = un estado de pantalla que se limpia antes de la siguiente): self.portada(...) → definición o situación inicial con una PREGUNTA DE PREDICCIÓN antes del primer movimiento → 2 o 3 ejemplos (incluido al menos un contraejemplo o caso que rompa la idea ingenua; un solo parámetro cambia a la vez) → self.cierre([...]). Cada escena lleva de 1 a 3 bloques de narración.

RECEPTOR
Estudiantes de MATEM-Precálculo, bloque II (funciones; exponencial y logarítmica), que ya conocen la noción de función, lectura de pares ordenados en una gráfica, la recta y = x y la definición de inyectividad, y que suelen cometer el error de creer que basta con "voltear la gráfica" para obtener la inversa, sin preguntarse si el resultado es una función, y de olvidar que el dominio del logaritmo viene del ámbito de la exponencial. Lenguaje en español de Costa Rica, voseo moderado, sin jerga innecesaria.

RESTRICCIONES
- Empezá con: from manim import * / from estilo_matia import *
- Usá solo la API de estilo_matia: self.narrar(texto) como context manager, self.portada, self.cierre, self.ejes, self.formula, self.panel, self.limpiar, y los colores C_FUNCION, C_FUNCION2, C_FUNCION3, C_ENFASIS, C_OK, C_ALERTA. No crees Axes, colores ni servicios de voz propios.
- Los ejes deben ser cuadrados (x_length = y_length) para que y = x se vea a 45°, y la recta y = x debe estar dibujada en todas las escenas con gráfica.
- Cada idea va dentro de un bloque "with self.narrar(...)": la narración debe decir exactamente lo que se ve, en el mismo orden; nunca anuncies algo que aún no está en pantalla.
- Entre 8 y 14 bloques de narración; cada uno de 1 a 3 oraciones.
- Usá MathTex/Tex para toda expresión matemática; Text solo para títulos.
- Sin archivos externos, sin imágenes, sin bibliotecas adicionales, sin LaTeX exótico (solo amsmath).
- Evitá textos superpuestos: llamá self.limpiar() antes de cambiar de escena; el panel de fórmulas va arriba a la izquierda y los ejes a la derecha.
- Matemática exacta: los valores que se dibujan (puntos marcados y sus reflejos) deben coincidir con los que se dicen.
- Entregá solo el código, sin markdown, sin explicación fuera de comentarios.

RECURSOS
- Solución matemática de referencia (resuelta por mí, usala tal cual, no la cambies):
  f(x) = 2x + 1 → f⁻¹(x) = (x − 1)/2. Pares: (0,1)→(1,0); (1,3)→(3,1); (2,5)→(5,2).
  g(x) = x² → su reflejo x = y² NO es función: a x = 4 le corresponden y = 2 y y = −2; g(2) = g(−2) = 4. Restringida a x ≥ 0, la inversa es √x: (2,4)→(4,2).
  h(x) = 2ˣ → h⁻¹(x) = log₂x. Pares: (0,1)→(1,0); (1,2)→(2,1); (2,4)→(4,2). log₂4 = 2 porque 2² = 4. Dominio de log₂x: x > 0, heredado del ámbito de 2ˣ.
- Programa MATEM-Precálculo 2026, núcleo: Funciones; función exponencial; función logarítmica (II parcial).
- Ejemplo modelo del formato: video_puntos_criticos.py (misma serie).

REVISIÓN
Antes de entregar, verificá y declará al final del archivo, como comentario, el STORYBOARD: una fila por escena con (1) número y nombre, (2) estado de pantalla, (3) qué se mueve o aparece, (4) texto de la narración, (5) valor de control que debe verificarse cuadro a cuadro y su justificación con la solución de referencia; más la duración estimada total.

[A continuación se pega el contenido completo de estilo_matia.py]

---

# Prompt de ITERACIÓN (ejemplo de corrección documentada, criterio 3 de la rúbrica)

Se usa en el mismo chat, después de ver el primer render en -ql. Un problema por mensaje; cada mensaje queda registrado como iteración.

Revisé el render de video_inversa_reflexion.py con la lista de cotejo y encontré estos problemas. Corregí SOLO esto y devolvé el archivo completo, sin cambiar la narración de las demás escenas ni tocar estilo_matia.py:

1. [Error de valor] En la escena 3 el punto reflejado de (2,5) aparece en (5,3). Según la solución de referencia debe ser (5,2). Revisá cómo construís pts_inv.
2. [Sincronía] En la escena 4 la voz dice "la curva que resulta es x igual a y cuadrado" antes de que la curva termine de dibujarse. Mové el TransformFromCopy dentro de ese mismo bloque narrar y, si hace falta, dividí la frase en dos bloques.
3. [Superposición] El panel de la escena 4 (cuatro líneas) tapa el eje y. Reducilo a tres líneas o bajá el font_size a 26.

No cambies colores, voz, portada ni cierre. Al final actualizá la tabla del storyboard para que refleje los valores corregidos.

# Ejemplo de iteración que se decide NO aceptar (también se documenta)

La IA propuso agregar una animación de "rebote" a los puntos reflejados y un degradado en la recta y = x. No se aceptó: no corrige ningún valor ni mejora la comprensión de la relación (a,b) → (b,a), y añade movimiento que compite con el único parámetro que debe cambiar en la escena.
