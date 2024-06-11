import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter a color:")
colors = ["red", "blue", "orange", "yellow", "green", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtles_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtles_index])
    new_turtle.goto(x=-230, y= y_positions[turtles_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_turtle = turtle.pencolor()
            if winner_turtle == user_bet:
                print("You have won.")
            else:
                print(f"You have lost. The winning turtle was {winner_turtle}")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
