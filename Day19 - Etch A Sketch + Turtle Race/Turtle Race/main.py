from turtle import Turtle, Screen
import random

race = False
screen = Screen()
screen.setup(width = 500, height = 500)
guess = screen.textinput(title = "Place your bet", prompt = "Which turtle will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-75, -45, -15, 15, 45, 75]
all_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y = y_positions[turtle_index])
    all_turtles.append(new_turtle)

if guess:
    race = True

while race:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race = False
            winning_color = turtle.pencolor()
            if winning_color == guess:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner.")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
