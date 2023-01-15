from turtle import Turtle

x_pos = 0
y_pos = -280
color = 'black'
heading = 90
shape = 'turtle'
move_turtle = 10
initial_level = 0
LEVEL_TO_INCRESE = 1
TEXT_LEVEL_POS = (-250, 270)
TEXT_CAR_POS = (-40, 270)
TEXT_SPEED_POS = (130, 270)
TEXT_GAME_OVER_POS = (-150, 0)


class Myturtle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(heading)
        self.setpos(x_pos, y_pos)
        self.color(color)
        self.shape(shape)
        self.level = initial_level

    def move(self):
        '''Move on the cars'''
        self.forward(move_turtle)

    def back_init(self):
        '''Put the pricipal turtle in your initial position'''
        self.goto(x_pos, y_pos)

    def set_level(self):
        '''Iccrease one level to the game'''
        self.hideturtle()
        self.level += LEVEL_TO_INCRESE

    def text_level(self):
        '''Print the text level on screen'''
        self.clear()
        self.hideturtle()
        self.goto(TEXT_LEVEL_POS)
        self.write(f'Level:{self.level}', 'center', font=('Arial', 15, 'bold'))

    def text_car(self, total_car=0):
        '''Print num car on screen'''
        self.clear()
        self.hideturtle()
        self.goto(TEXT_CAR_POS)
        self.write(f'Cars:{total_car}', 'center', font=('Arial', 15, 'bold'))

    def text_speed(self, speed=0):
        '''Print cars speed on screen'''
        self.clear()
        self.hideturtle()
        self.goto(TEXT_SPEED_POS)
        self.write(f'Speed:{speed}', 'center', font=('Arial', 15, 'bold'))

    def text_gameover(self):
        '''Print game over on screen'''
        self.hideturtle()
        self.pencolor('red')
        self.clear()
        self.goto(TEXT_GAME_OVER_POS)
        self.write('GAME-OVER', 'center', font=('Arial', 40, 'bold'))


# turtles
george = Myturtle() # principal
text_turtle = Myturtle() # Creates text level
car_text_turtle = Myturtle() # Creates text count car
speed_text_turtle = Myturtle() # Creates text of speed of cars
gameover_turtle = Myturtle() # creates text of game over
