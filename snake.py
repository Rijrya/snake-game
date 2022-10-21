from turtle import Screen, Turtle
import time


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        self.heading = self.head.heading()

    def create_snake(self):
        for _ in range(3):
            turtle = Turtle(shape='square')
            turtle.color('white')
            turtle.penup()
            turtle.goto(x=-20 * _, y=0)
            self.snake.append(turtle)

    def extend(self):
        turtle = Turtle(shape='square')
        turtle.penup()
        turtle.goto(600, 600)
        turtle.color("white")
        self.snake.append(turtle)

    def move(self):
        for segment in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[segment - 1].xcor()
            new_y = self.snake[segment - 1].ycor()
            self.snake[segment].goto(new_x, new_y)
        self.snake[0].forward(20)

    def up(self):
        if self.snake[0].heading() != 270.0:
            self.snake[0].setheading(90)

    def right(self):
        if self.snake[0].heading() != 180.0:
            self.snake[0].setheading(0)

    def down(self):
        if self.snake[0].heading() != 90.0:
            self.snake[0].setheading(270)

    def left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180.0)

    def reset(self):
        for seg in self.snake:
            seg.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]
