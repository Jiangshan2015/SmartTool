import flet
from flet import *
from math import pi


def Loading():
    return Stack(
        controls=[
            AnimatedBox("#e9665a", None, 0),
            AnimatedBox("#7df6dd", "#23262a", pi / 4),
        ]
    ),


icons.DOWNLOADING


class AnimatedBox(UserControl):
    def __init__(self, border_color, bg_color, rotate_angle):
        self.border_color = border_color
        self.bg_color = bg_color
        self.rotate_angle = rotate_angle
        super().__init__()

    def build(self):
        return Container(
            width=48,
            height=48,
            border=border.all(2.5, self.border_color),
            bgcolor=self.bg_color,
            border_radius=2,
            rotate=transform.Rotate(self.rotate_angle, alignment.center),
            animate_rotation=animation.Animation(700, "easeInOut"),
        )
