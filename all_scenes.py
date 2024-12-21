# import everything from manim
from manim import *

# This is the main scene, the name of the mp4 file matches this class name 
class Main(Scene):
    def construct(self): # this builds the animation...
        """
        manim animations are split into 2 sections, adding objects to memory
        and adding those objects to the animation itself.
        """

        # make a text object (but don't show it, just add it into memory)
        # The first arg is the string in the text
        # The second arg is the font size
        t = Text(
            "This is a demo, I'm still learning.",
            font_size=72
        ).to_edge(UP) # basically means that when the text appears, it will be on top.



        # make a square object (in memory)
        # side lengths are 3
        # stroke colour which means boundary color which is green
        # fill colour is also green
        # fill_opacity means transparency of fill, 1 means no transparent, 0 means fully transparent 
        sq = Square(
            side_length=3,
            stroke_color=GREEN,
            fill_color=GREEN,
            fill_opacity=1,
        )

        # I'm pretty sure you can figure this out
        t2 = Text(
            "and then, a circle.",
            font_size=72,
        ).to_edge(UP)

        t3 = Text(
            "Finally, a triangle.",
            font_size=72,
        ).to_edge(UP)

        # make a circle in memory
        # radius is 1.5 idk the measurement tho
        c = Circle(
            radius=1.5,
            fill_opacity=1
        )

        # make a triangle in memory
        tri = Triangle(
            fill_opacity=1,
            color=BLUE,
        ).scale(3) # scale it by 3 (again, idk what its scaling measurement is.)


        t4 = Text(
            "you can also multiply shapes...",
            font_size=72
        ).to_edge(UP)

        c2 = Circle(
            radius=3,
            color=WHITE,
            fill_opacity=1
        )

        # Create a list of colours for the smaller circles
        colors = [RED, ORANGE, YELLOW, GREEN, BLUE, DARK_BLUE, PURPLE]

        # Use a loop to create the smaller circles and position them
        circle_group = VGroup() # vgroup is like a list of manim objects
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
            "White has every colour...",
            font_size=72
        ).to_edge(UP)

        # Animations

        # self.play is used to play animations
        self.play(Write(t, run_time=2)) # The Write function applies a smooth writing animation while adding the text, run_time is a named parameter which is how long the writing will take to finish.


        # The Transform function transforms one object into another (smoothly by default)
        self.play(Transform(t, sq, run_time=3)) # since I transformed t into sq, t is now a square object


        # Since t was now a square, this bit of code makes it look like the square is transforming into some text
        self.play(Transform(t, t2, run_time=2))
        self.wait(1) # wait method waits a certain seconds before playing the next animation, in this case, 1.

        # transforms t into circle object
        self.play(Transform(t, c, run_time=3))

        # transforms t which was a circle into t3 which is a text object
        self.play(Transform(t, t3, run_time=3))
        self.wait(1)

        # transforms t into a triangle
        self.play(Transform(t, tri, run_time=3))

        # transforms t into a text
        self.play(Transform(t, t4, run_time=3))
        self.wait(1)

        # turns t into a white circle
        self.play(Transform(t, c2, run_time=3))

        # It transforms the white circle into a bunch of smaller circles, 
        # simulating the division of the colour white into other colours. 
        self.play(
            Transform(t, circle_group.to_edge(LEFT), run_time=2),
            Write(t5, run_time=1)
        )


        self.wait(4)

# and that's it, I hope you learned a few things, I'm sorry it took so long, I was ill and couldn't add comments, again, sorry!
