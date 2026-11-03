ROL
Actuá como especialista en educación matemática de secundaria y programador experto en Manim Community Edition (v0.19 o superior) con manim-voiceover. Trabajás para la serie de videos "MatIA" de MATEM-UNA Precálculo 2026, que ya tiene una identidad visual y de voz definida en el archivo estilo_matia.py (no debés modificarla ni redefinirla).

RESULTADO
Entregá únicamente un archivo Python llamado video_[NOMBRE_CORTO].py que defina UNA clase [NombreClase](VideoMatIA) con el método construct, que produzca un video narrado de entre 60 y 120 segundos sobre:

   [APRENDIZAJE: qué relación matemática debe quedar clara al terminar el video]

Estructura obligatoria en 4 a 6 ESCENAS (cada escena = un estado de pantalla que se limpia antes de la siguiente): self.portada(...) → definición o situación inicial con una PREGUNTA DE PREDICCIÓN antes del primer movimiento → 2 o 3 ejemplos (incluido al menos un contraejemplo o caso que rompa la idea ingenua; un solo parámetro cambia a la vez) → self.cierre([...]). Cada escena lleva de 1 a 3 bloques de narración.

RECEPTOR
Estudiantes de [NIVEL: p. ej. undécimo año / MATEM-Precálculo, bloque II: funciones] que ya conocen [CONOCIMIENTOS PREVIOS] y que suelen cometer el error de [ERROR FRECUENTE QUE EL VIDEO DEBE DESARMAR]. Lenguaje en español de Costa Rica, voseo moderado, sin jerga innecesaria.

RESTRICCIONES
- Empezá con: from manim import * / from estilo_matia import *
- Usá solo la API de estilo_matia: self.narrar(texto) como context manager, self.portada, self.cierre, self.ejes, self.formula, self.panel, self.limpiar, y los colores C_FUNCION, C_FUNCION2, C_FUNCION3, C_ENFASIS, C_OK, C_ALERTA. No crees Axes, colores ni servicios de voz propios.
- Cada idea va dentro de un bloque "with self.narrar(...)": la narración debe decir exactamente lo que se ve, en el mismo orden; nunca anuncies algo que aún no está en pantalla.
- Entre 8 y 14 bloques de narración; cada uno de 1 a 3 oraciones.
- Usá MathTex/Tex para toda expresión matemática; Text solo para títulos.
- Sin archivos externos, sin imágenes, sin bibliotecas adicionales, sin LaTeX exótico (solo amsmath).
- Evitá textos superpuestos: llamá self.limpiar() antes de cambiar de ejemplo; el panel de fórmulas va arriba a la izquierda y los ejes abajo.
- Matemática exacta: los valores que se dibujan (ceros, vértices, puntos marcados) deben coincidir con los que se dicen.
- Entregá solo el código, sin markdown, sin explicación fuera de comentarios.

RECURSOS
- Solución matemática de referencia (resuelta por mí, usala tal cual, no la cambies):
  [PEGAR AQUÍ: funciones, derivadas, valores notables, intervalos, conclusión]
- Programa MATEM-Precálculo 2026, núcleo: [NÚCLEO].
- Ejemplo modelo del formato: video_puntos_criticos.py (misma serie).

REVISIÓN
Antes de entregar, verificá y declará al final del archivo, como comentario, el STORYBOARD: una fila por escena con (1) número y nombre, (2) estado de pantalla, (3) qué se mueve o aparece, (4) texto de la narración, (5) valor de control que debe verificarse cuadro a cuadro y su justificación con la solución de referencia; más la duración estimada total. Si algún valor no coincide con la solución de referencia, corregí el código, no la referencia.
