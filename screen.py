from turtle import Screen
from my_turtle import george

width = 600
height = 600


class Myscreen:
    def __init__(self):
        self.create = Screen()
        self.create.setup(width=width, height=height)
        self.create.listen()
        self.create.onkey(george.move, 'Up')
        self.create.tracer(0)
        
my_screen = Myscreen()