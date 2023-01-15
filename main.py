from screen import my_screen
from my_turtle import george, text_turtle, car_text_turtle, speed_text_turtle, gameover_turtle
from cars import Mycars
from time import sleep

# variables
sleep_time = 0.1
initial_cars = 10
Y_LIMIT = 280

# Criando carros
new_car = Mycars()
new_car.hideturtle()
list_cars = new_car.car_gen()

# text on screen
text_turtle.text_level()
car_text_turtle.text_car(len(list_cars))
speed_text_turtle.text_speed(new_car.init_speed)
gameover_turtle.hideturtle()

# Game program
game_is_on = True
while game_is_on:
    # Moving the cars
    car_text_turtle.text_car(len(list_cars))
    sleep(sleep_time)
    my_screen.create.update()
    new_car.add_car()
    for car in list_cars:
        car.move()

    # detects if turtle reach  de top edge of the screen
    if george.ycor() == Y_LIMIT:
        george.back_init()
        text_turtle.set_level()
        text_turtle.text_level()
        new_car.level_up()# incrases one more car
        speed_text_turtle.text_speed(new_car.init_speed)

    # detects if turtle colids with a car
    for car in list_cars:
        if george.distance(car) < 20:
            from my_turtle import gameover_turtle
            gameover_turtle.text_gameover()
            game_is_on = False

    # deletes the cars that reach the limit border left
    for car in list_cars:
        if car.xcor() < -350:
            list_cars.pop(list_cars.index(car))
            car = Mycars()
            list_cars.append(car)


my_screen.create.exitonclick()