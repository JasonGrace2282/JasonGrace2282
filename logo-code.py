from manim import *
# SHOUTOUT TO MANIM!


class Logo(Scene):
    def construct(self):
        name = Text("Aarush Deshpande", color=RED).scale(0.5).set_stroke(color=RED)
        username = Text("JasonGrace2282", color=BLUE).set_stroke(color=BLUE)
        group = VGroup(name, username).arrange(DOWN).scale(0.7)
        self.play(Write(name), Write(username, reverse=True), run_time=1)
        big_group = group.copy().scale(2)
        self.play(
            group.animate(rate_func=rate_functions.ease_out_bounce).scale(2), 
            Circumscribe(big_group, Circle)
        )
        self.wait()
        self.play(
            Succession(
                Unwrite(name),
                Unwrite(username),
                run_time=1,
            )
        )


with tempconfig({"format": "gif", "transparent": True}):
    Logo().render()
