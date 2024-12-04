from manim import *

class Pith(Scene):
    def construct(self):
        t = Text(
            "this is a demo, im still learning.",
            font_size=72
        ).to_edge(UP)

        sq = Square(
            side_length=3,
            stroke_color=GREEN,
            fill_color=GREEN,
            fill_opacity=1,
        )

        t2 = Text(
            "and then, a circle.",
            font_size=72,
        ).to_edge(UP)

        t3 = Text(
            "finally, a triangle.",
            font_size=72,
        ).to_edge(UP)

        c = Circle(
            radius=1.5,
            fill_opacity=1
        )

        tri = Triangle(
            fill_opacity=1,
            color=BLUE,
        ).scale(3)

        t4 = Text(
            "you can also multiply shapes...",
            font_size=72
        ).to_edge(UP)

        c2 = Circle(
            radius=3,
            color=WHITE,
            fill_opacity=1
        )

        # Create a list of colors for the smaller circles
        colors = [RED, ORANGE, YELLOW, GREEN, BLUE, DARK_BLUE, PURPLE]

        # Use a loop to create the smaller circles and position them
        circle_group = VGroup()
        for i, color in enumerate(colors):
            c_temp = Circle(
                radius=1.5,
                color=color,
                fill_opacity=1
            )
            if i == 0:
                c_temp.next_to(c2, RIGHT, buff=-1)
            else:
                c_temp.next_to(circle_group[i-1], RIGHT, buff=-1)
            circle_group.add(c_temp)

        t5 = Text(
            "white has every color...",
            font_size=72
        ).to_edge(UP)

        # Animations
        self.play(Write(t, run_time=2))
        self.play(Transform(t, sq, run_time=3))

        self.play(Transform(t, t2, run_time=2))
        self.wait(1)
        self.play(Transform(t, c, run_time=3))

        self.play(Transform(t, t3, run_time=3))
        self.wait(1)
        self.play(Transform(t, tri, run_time=2))

        self.play(Transform(t, t4, run_time=3))
        self.wait(1)
        self.play(Transform(t, c2, run_time=3))

        self.play(
            Transform(t, circle_group.to_edge(LEFT), run_time=2),
            Write(t5, run_time=1)
        )

        self.wait(4)



class CirclesTogether(Scene):
    def construct(self):
        c2 = Circle(
            radius=3,
            color=WHITE,
            fill_opacity=1
        )

        c3 = Circle(
            radius=1.5,
            color=RED,
            fill_opacity=1,
        )

        # Position c3 to the right of c2
        c3.next_to(c2, RIGHT, buff=0)  # 'buff' controls the spacing

        self.play(Create(c2), Create(c3))
        self.wait(2)




class CircleColorDiv(Scene):
    def construct(self):
        t = Text(
            "this is a demo, im still learning.",
            font_size=72
        ).to_edge(UP)

        sq = Square(
            side_length=3,
            stroke_color=GREEN,
            fill_color=GREEN,
            fill_opacity=1,
        )

        c2 = Circle(
            radius=3,
            color=WHITE,
            fill_opacity=1
        )

        # Create a list of colors for the smaller circles
        colors = [RED, ORANGE, YELLOW, GREEN, BLUE, DARK_BLUE, PURPLE]

        buff_size = 1.25

        # Use a loop to create the smaller circles and position them
        circle_group = VGroup()
        for i, color in enumerate(colors):
            c_temp = Circle(
                radius=1.5,
                color=color,
                fill_opacity=1
            )
            if i == 0:
                c_temp.next_to(c2, RIGHT, buff=-buff_size)
            else:
                c_temp.next_to(circle_group[i-1], RIGHT, buff=-buff_size)
            circle_group.add(c_temp)

        t5 = Text(
            "white has every color...",
            font_size=72
        ).to_edge(UP)

        t6 = Text(
            "what i should make next?",
            font_size=65,
        )


        self.play(
            Write(t, run_time=2)
        )
        self.wait(1)

        self.play(
            Transform(t, c2, run_time=3)
        )

        self.play(
            Transform(
                t,
                circle_group.to_edge(LEFT),
                run_time=4,
            ),
            Write(t5, run_time=1)
        )

        self.play(
            Transform(
                t,
                c2,
                run_time=4,
            ),
            Write(t5, run_time=0.001)
        )

        self.play(
            Transform(
                t5,
                t6,
                run_time=2,
            ),
            t.animate.scale(0)
        )

        self.wait(2)
