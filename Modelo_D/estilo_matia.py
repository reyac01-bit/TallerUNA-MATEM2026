"""
estilo_matia.py — Identidad fija de los videos MatIA (NO editar para cada video).

Todo video hereda de VideoMatIA. Así, voz, colores, portada, cierre y ejes
son idénticos en todos los videos; cada escena nueva solo aporta contenido.

API disponible para las escenas (y para el prompt que se da a la IA):
    self.narrar(texto)                    -> context manager: anima mientras se oye la voz
    self.portada(titulo, subtitulo="")    -> portada estándar (ya narra el título)
    self.cierre(lineas)                   -> resumen final estándar (lista de str en Tex)
    self.ejes(x_range, y_range, ...)      -> Axes con el estilo de la serie
    self.formula(tex, color=None)         -> MathTex en esquina superior izquierda
    self.panel(lineas)                    -> columna de Tex alineada a la izquierda
    self.limpiar()                        -> desvanece todo lo que esté en pantalla
    Colores: C_FUNCION, C_FUNCION2, C_FUNCION3, C_ENFASIS, C_OK, C_ALERTA
"""

from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

# ---------- Paleta fija de la serie ----------
C_FONDO = "#0f1b2d"
C_TEXTO = "#f4f4f4"
C_FUNCION = "#4cc9f0"     # azul claro
C_FUNCION2 = "#f72585"    # magenta
C_FUNCION3 = "#b5e48c"    # verde claro
C_ENFASIS = "#ffd166"     # amarillo
C_OK = "#80ed99"
C_ALERTA = "#ff6b6b"

VOZ_IDIOMA = "es"
VOZ_ACENTO = "com"        # "com" neutro | "es" España | "com.mx" México
SERIE = "MatIA · Red Académica MatIA"
INSTITUCION = "MATEM-UNA · Precálculo 2026"


class VideoMatIA(VoiceoverScene):
    """Escena base: fija voz, fondo, tipografía y bloques reutilizables."""

    def setup(self):
        super().setup()
        self.camera.background_color = C_FONDO
        Text.set_default(color=C_TEXTO)
        Tex.set_default(color=C_TEXTO)
        MathTex.set_default(color=C_TEXTO)
        self.set_speech_service(GTTSService(lang=VOZ_IDIOMA, tld=VOZ_ACENTO))

    # ----- voz -----
    def narrar(self, texto):
        return self.voiceover(text=texto)

    # ----- bloques estándar -----
    def portada(self, titulo, subtitulo=""):
        t = Text(titulo, font_size=44, weight=BOLD)
        s = Text(subtitulo, font_size=26, color=C_ENFASIS) if subtitulo else VGroup()
        pie = Text(f"{SERIE}  ·  {INSTITUCION}", font_size=18, color=GREY_B).to_edge(DOWN)
        grupo = VGroup(t, s).arrange(DOWN, buff=0.4)
        with self.narrar(f"{titulo}. {subtitulo}" if subtitulo else titulo):
            self.play(Write(t), FadeIn(pie))
            if subtitulo:
                self.play(FadeIn(s, shift=UP))
        self.play(FadeOut(s), FadeOut(pie), t.animate.scale(0.6).to_edge(UP, buff=0.3))
        self.titulo_actual = t

    def cierre(self, lineas, narracion=None):
        self.limpiar()
        items = [Tex(r"\textbf{Resumen}", font_size=40, color=C_ENFASIS)]
        items += [Tex(f"{i+1}. {l}", font_size=32) for i, l in enumerate(lineas)]
        g = VGroup(*items).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        if g.width > 12:
            g.scale_to_fit_width(12)
        texto = narracion or " ".join(lineas)
        with self.narrar(texto):
            self.play(FadeIn(g, lag_ratio=0.3))
        pie = Text(SERIE, font_size=18, color=GREY_B).to_edge(DOWN)
        self.play(FadeIn(pie))
        self.wait(2)

    def ejes(self, x_range, y_range, x_length=7, y_length=4.5, **kw):
        ax = Axes(
            x_range=x_range, y_range=y_range,
            x_length=x_length, y_length=y_length, tips=False,
            axis_config={"include_numbers": True, "font_size": 24, "color": GREY_B},
            **kw,
        ).to_edge(DOWN, buff=0.4)
        return ax

    def formula(self, tex, color=None, font_size=36):
        m = MathTex(tex, font_size=font_size, color=color or C_TEXTO)
        m.to_corner(UL).shift(DOWN * 0.9)
        return m

    def panel(self, lineas, font_size=32, debajo_de=None):
        g = VGroup(*[Tex(l, font_size=font_size) if not isinstance(l, Mobject) else l
                     for l in lineas]).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        if debajo_de is not None:
            g.next_to(debajo_de, DOWN, aligned_edge=LEFT, buff=0.3)
        else:
            g.to_corner(UL).shift(DOWN * 0.9)
        return g

    def limpiar(self):
        conservar = getattr(self, "titulo_actual", None)
        objetos = [m for m in self.mobjects if m is not conservar]
        if objetos:
            self.play(*[FadeOut(m) for m in objetos])
