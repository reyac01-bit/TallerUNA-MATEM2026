"""
video_inversa_reflexion.py — MODELO D de la serie MatIA (Momento 4, MATEM-Precálculo 2026)
Bloque II · Funciones / exponencial y logarítmica.

APRENDIZAJE: la gráfica de la función inversa es la reflexión de la gráfica de f
respecto a la recta y = x, porque cada par (a, b) de f se convierte en (b, a) de f⁻¹;
esa reflexión solo es una función cuando f es inyectiva.

SOLUCIÓN DE REFERENCIA (resuelta antes de pedir el código):
  f(x) = 2x + 1  → f⁻¹(x) = (x − 1)/2.  Pares: (0,1)→(1,0); (1,3)→(3,1); (2,5)→(5,2).
  g(x) = x²      → su reflejo x = y² NO es función (a x = 4 le corresponden y = 2 y y = −2).
                   Restringida a x ≥ 0, la inversa es √x: (0,0)→(0,0); (1,1)→(1,1); (2,4)→(4,2).
  h(x) = 2ˣ      → h⁻¹(x) = log₂ x.  Pares: (0,1)→(1,0); (1,2)→(2,1); (2,4)→(4,2).
  En los tres casos los puntos de la gráfica sobre y = x (si los hay) no se mueven.
"""
from manim import *
from estilo_matia import *


class InversaReflexion(VideoMatIA):
    def construct(self):
        # ---------- ESCENA 1 · Portada ----------
        self.portada("La función inversa como reflexión",
                     "¿Qué pasa con cada punto al invertir una función?")

        # ---------- ESCENA 2 · Pregunta de predicción y definición ----------
        ax = self.ejes([-1, 5, 1], [-1, 5, 1], x_length=5.5, y_length=5.5).shift(RIGHT * 2.2)
        diag = ax.plot(lambda x: x, x_range=[-1, 5], color=GREY_B, stroke_width=2)
        etq_diag = MathTex("y=x", font_size=28, color=GREY_B).next_to(ax.c2p(4.6, 4.6), RIGHT, buff=0.1)
        p13 = Dot(ax.c2p(1, 3), color=C_FUNCION)
        e13 = MathTex("(1,\\,3)", font_size=30, color=C_FUNCION).next_to(p13, UL, buff=0.1)
        pregunta = self.panel([Tex(r"\textbf{Predecí:}", font_size=30, color=C_ENFASIS),
                               Tex(r"si $(1,3)$ es un punto de $f$,", font_size=28),
                               Tex(r"¿qué punto tiene $f^{-1}$?", font_size=28)])
        with self.narrar("Antes de ver la respuesta, pensá: si el punto uno coma tres está en la "
                         "gráfica de una función f, ¿qué punto debe estar en la gráfica de su inversa?"):
            self.play(Create(ax), Create(diag), Write(etq_diag))
            self.play(FadeIn(p13), Write(e13), Write(pregunta))
        p31 = Dot(ax.c2p(3, 1), color=C_FUNCION2)
        e31 = MathTex("(3,\\,1)", font_size=30, color=C_FUNCION2).next_to(p31, DR, buff=0.1)
        seg = DashedLine(ax.c2p(1, 3), ax.c2p(3, 1), color=C_ENFASIS)
        defin = self.panel([MathTex(r"(a,b)\in f \iff (b,a)\in f^{-1}", font_size=32, color=C_ENFASIS),
                            Tex(r"Intercambiar coordenadas es", font_size=26),
                            Tex(r"reflejar respecto a $y=x$.", font_size=26)], debajo_de=pregunta)
        with self.narrar("La inversa deshace lo que hace f: si f manda uno a tres, la inversa manda "
                         "tres a uno. El punto uno coma tres se convierte en tres coma uno. "
                         "Intercambiar las coordenadas es exactamente reflejar el punto respecto a "
                         "la recta y igual a x: la recta es el eje de simetría."):
            self.play(Create(seg))
            self.play(TransformFromCopy(p13, p31), Write(e31))
            self.play(Write(defin))
        self.limpiar()

        # ---------- ESCENA 3 · Ejemplo lineal f(x)=2x+1 ----------
        ax = self.ejes([-1, 5, 1], [-1, 5, 1], x_length=5.5, y_length=5.5).shift(RIGHT * 2.2)
        diag = ax.plot(lambda x: x, x_range=[-1, 5], color=GREY_B, stroke_width=2)
        f = lambda x: 2 * x + 1
        gf = ax.plot(f, x_range=[-1, 2], color=C_FUNCION)
        ef = self.formula(r"f(x)=2x+1", color=C_FUNCION)
        pts = VGroup(*[Dot(ax.c2p(a, f(a)), color=C_FUNCION) for a in (0, 1, 2)])
        with self.narrar("Primer ejemplo: f de x igual a dos x más uno. Marcamos tres puntos: "
                         "cero coma uno, uno coma tres y dos coma cinco."):
            self.play(Create(ax), Create(diag), Create(gf), Write(ef))
            self.play(FadeIn(pts))
        pts_inv = VGroup(*[Dot(ax.c2p(f(a), a), color=C_FUNCION2) for a in (0, 1, 2)])
        finv = lambda x: (x - 1) / 2
        ginv = ax.plot(finv, x_range=[-1, 5], color=C_FUNCION2)
        einv = MathTex(r"f^{-1}(x)=\frac{x-1}{2}", font_size=36, color=C_FUNCION2).next_to(ef, DOWN, aligned_edge=LEFT, buff=0.4)
        with self.narrar("Reflejamos cada punto: cero coma uno pasa a uno coma cero; uno coma tres "
                         "a tres coma uno; dos coma cinco a cinco coma dos. Los puntos reflejados "
                         "quedan sobre una nueva recta."):
            self.play(TransformFromCopy(pts, pts_inv))
        with self.narrar("Esa recta es la gráfica de la inversa: f inversa de x igual a x menos uno "
                         "sobre dos. Comprobá con un punto: f inversa de tres es tres menos uno "
                         "sobre dos, igual a uno. Correcto."):
            self.play(TransformFromCopy(gf, ginv), Write(einv))
        self.limpiar()

        # ---------- ESCENA 4 · Contraejemplo g(x)=x² ----------
        ax = self.ejes([-2.5, 5, 1], [-2.5, 5, 1], x_length=5.5, y_length=5.5).shift(RIGHT * 2.2)
        diag = ax.plot(lambda x: x, x_range=[-2.5, 5], color=GREY_B, stroke_width=2)
        g = lambda x: x ** 2
        gg = ax.plot(g, x_range=[-2.2, 2.2], color=C_FUNCION)
        eg = self.formula(r"g(x)=x^2", color=C_FUNCION)
        with self.narrar("Segundo ejemplo, el que rompe la idea ingenua: g de x igual a x cuadrado. "
                         "¿Basta con reflejar la parábola para obtener la inversa?"):
            self.play(Create(ax), Create(diag), Create(gg), Write(eg))
        refl = ax.plot_parametric_curve(lambda t: np.array([t ** 2, t, 0]), t_range=[-2.2, 2.2], color=C_ALERTA)
        with self.narrar("Reflejamos. La curva que resulta es x igual a y cuadrado."):
            self.play(TransformFromCopy(gg, refl))
        vert = DashedLine(ax.c2p(4, -2.5), ax.c2p(4, 5), color=C_ENFASIS)
        d1, d2 = Dot(ax.c2p(4, 2), color=C_ENFASIS), Dot(ax.c2p(4, -2), color=C_ENFASIS)
        aviso = self.panel([Tex(r"A $x=4$ le corresponden", font_size=28),
                            MathTex(r"y=2\ \text{ y }\ y=-2", font_size=32, color=C_ALERTA),
                            Tex(r"$\Rightarrow$ el reflejo \textbf{no} es función.", font_size=28),
                            Tex(r"$g$ no es inyectiva: $g(2)=g(-2)=4$.", font_size=26)], debajo_de=eg)
        with self.narrar("Pero fijate: a x igual a cuatro le corresponden dos valores, y igual a dos "
                         "y y igual a menos dos. El reflejo no es una función. La razón es que g no "
                         "es inyectiva: dos y menos dos tienen la misma imagen, cuatro."):
            self.play(Create(vert), FadeIn(d1), FadeIn(d2))
            self.play(Write(aviso))
        rama = ax.plot(g, x_range=[0, 2.2], color=C_FUNCION3, stroke_width=6)
        raiz = ax.plot(lambda x: np.sqrt(x), x_range=[0, 5], color=C_FUNCION3, stroke_width=6)
        eraiz = MathTex(r"x\ge 0:\quad g^{-1}(x)=\sqrt{x}", font_size=32, color=C_FUNCION3).next_to(aviso, DOWN, aligned_edge=LEFT, buff=0.3)
        with self.narrar("Si restringimos el dominio a x mayor o igual que cero, g sí es inyectiva, "
                         "y el reflejo de esa rama es la función raíz cuadrada de x. El punto dos "
                         "coma cuatro pasa a cuatro coma dos."):
            self.play(FadeOut(refl), FadeOut(vert), FadeOut(d1), FadeOut(d2), Create(rama))
            self.play(TransformFromCopy(rama, raiz), Write(eraiz))
        self.limpiar()

        # ---------- ESCENA 5 · h(x)=2^x y log2 ----------
        ax = self.ejes([-1.5, 5, 1], [-1.5, 5, 1], x_length=5.5, y_length=5.5).shift(RIGHT * 2.2)
        diag = ax.plot(lambda x: x, x_range=[-1.5, 5], color=GREY_B, stroke_width=2)
        h = lambda x: 2 ** x
        gh = ax.plot(h, x_range=[-1.5, 2.3], color=C_FUNCION)
        eh = self.formula(r"h(x)=2^x", color=C_FUNCION)
        pts = VGroup(*[Dot(ax.c2p(a, h(a)), color=C_FUNCION) for a in (0, 1, 2)])
        with self.narrar("Tercer ejemplo: la exponencial h de x igual a dos elevado a la x, con los "
                         "puntos cero coma uno, uno coma dos y dos coma cuatro. Es creciente, así que "
                         "es inyectiva y tiene inversa en todo su dominio."):
            self.play(Create(ax), Create(diag), Create(gh), Write(eh), FadeIn(pts))
        pts_inv = VGroup(*[Dot(ax.c2p(h(a), a), color=C_FUNCION2) for a in (0, 1, 2)])
        glog = ax.plot(lambda x: np.log2(x), x_range=[0.35, 5], color=C_FUNCION2)
        elog = MathTex(r"h^{-1}(x)=\log_2 x", font_size=36, color=C_FUNCION2).next_to(eh, DOWN, aligned_edge=LEFT, buff=0.4)
        nota = self.panel([Tex(r"$\log_2 4 = 2$ porque $2^2=4$", font_size=28),
                           Tex(r"Dominio de $\log_2 x$: $x>0$", font_size=28, color=C_ENFASIS)], debajo_de=elog)
        with self.narrar("Reflejamos: uno coma cero, dos coma uno, cuatro coma dos. La curva reflejada "
                         "es el logaritmo en base dos. Logaritmo de cuatro es dos porque dos al "
                         "cuadrado es cuatro: la inversa responde la pregunta «¿a qué exponente?»."):
            self.play(TransformFromCopy(pts, pts_inv))
            self.play(TransformFromCopy(gh, glog), Write(elog))
        with self.narrar("Y observá el dominio: la exponencial solo toma valores positivos, así que su "
                         "inversa solo acepta entradas positivas. Por eso el logaritmo existe únicamente "
                         "para x mayor que cero."):
            self.play(Write(nota))

        # ---------- ESCENA 6 · Cierre ----------
        self.cierre(
            [r"$(a,b)\in f \iff (b,a)\in f^{-1}$: la inversa refleja respecto a $y=x$.",
             r"El reflejo es función solo si $f$ es inyectiva ($x^2$ necesita $x\ge 0$).",
             r"$2^x$ y $\log_2 x$ son reflejo una de la otra; dominio de $\log_2 x$: $x>0$.",
             r"Para comprobar: $f^{-1}(f(a))=a$ con un punto concreto."],
            narracion="Resumiendo. La gráfica de la inversa es la reflexión de la gráfica de f "
                      "respecto a la recta y igual a x, porque cada par a coma b se convierte en b "
                      "coma a. Ese reflejo es una función solo cuando f es inyectiva; por eso x "
                      "cuadrado necesita restringirse. La exponencial y el logaritmo son reflejo una "
                      "de la otra, y el dominio del logaritmo hereda el ámbito de la exponencial. "
                      "Siempre comprobá con un punto concreto.",
        )


# =============================================================================
# STORYBOARD (salida de la R de Revisión) — una fila por escena
# | Esc | Estado de pantalla                     | Qué se mueve / aparece                    | Valor de control y justificación                          |
# |  1  | Portada + subtítulo                    | Título                                    | —                                                          |
# |  2  | Ejes cuadrados, y=x, punto (1,3)       | Pregunta de predicción; reflejo a (3,1)   | (1,3)→(3,1): intercambio de coordenadas                    |
# |  3  | f(x)=2x+1 con (0,1),(1,3),(2,5)        | Puntos reflejados; recta f⁻¹=(x−1)/2       | f⁻¹(3)=(3−1)/2=1 ✔; (2,5)→(5,2) sobre la recta              |
# |  4  | g(x)=x² y su reflejo x=y²              | Recta x=4 corta en y=2 y y=−2; rama x≥0→√x | g(2)=g(−2)=4 (no inyectiva); √4=2 ✔                        |
# |  5  | h(x)=2ˣ con (0,1),(1,2),(2,4)          | Puntos reflejados; curva log₂x            | log₂4=2 porque 2²=4 ✔; log₂x definido solo si x>0          |
# |  6  | Resumen de 4 líneas                    | Aparición escalonada                      | —                                                          |
# Duración estimada: 105–120 s (13 bloques de narración). Render de prueba: manim -ql video_inversa_reflexion.py InversaReflexion
# =============================================================================
