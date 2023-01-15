from turtle import Turtle
from random import randint, choice

width = 1
height = 2
color = ['red', 'blue', 'black', 'green', 'yellow', 'pink', 'brown', 'purple']
shape = 'square'
heading = 180
initial_speed = 5
speed_to_increase = 2


class Mycars(Turtle):
    '''creates cars and your defitions'''
    def __init__(self):
        super().__init__()
        self.color(choice(color))
        self.shape(shape)
        self.penup()
        self.setposition(randint(300, 360), randint(-250, 250))
        self.setheading(heading)
        self.shapesize(stretch_wid=width, stretch_len=height)
        self.init_speed = initial_speed

    def move(self):
        '''defines how many pixels the cars will run per moviment'''
        self.forward(self.init_speed)

    def car_gen(self):
        lista = ['car'+str(i) for i in range(10)]
        self.list_cars = []
        for item in lista:
            item = Mycars()
            self.list_cars.append(item)
        return self.list_cars

    def level_up(self):
        new_car = Mycars()
        self.list_cars.append(new_car)
        self.init_speed += speed_to_increase

    def add_car(self):
        chance_create = randint(1, 20)
        if chance_create == 1:
            new_car = Mycars()
            self.list_cars.append(new_car)
