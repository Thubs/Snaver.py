#!/bin/python3

"""

    A terminal screensaver written in python3
    Copyright (C) 2022 Thubs

    This program is a screensaver that shows the classic game snake the terminal as a screensaver.
    There is no input needed to run the program.
    If you want to change the program a config file should be generated.

"""

import random
import time

class Enclosure:
    # Create a visible border marked using the '#' character with a size of 20 by 40
    def __init__(self):
        self.size = 20
        self.border = []
        self.snake = []
        self.food = []
        self.direction = 'right'
        self.score = 0
        self.generate_border()
        self.generate_food()
        self.generate_snake()

    def generate_border(self):
        # Generate the border
        for i in range(self.size):
            self.border.append('#')
        self.border = ''.join(self.border)
        

class Fruit:
    """
        A class that represents a fruit.
        The fruit is a random position on the screen.
        The fruit is represented by a '$' character.
    """
    def __init__(self, screen):
        """
            Initializes the fruit.
            The fruit is a random position on the screen.
            The fruit is represented by a '$' character.
        """
        self.screen = screen
        self.x = 0
        self.y = 0
        self.fruit = '$'
        # Set the fruit to be red
        self.screen.set_color(1)
        self.generate()

    def generate(self):
        """
            Generates a random position for the fruit.
        """
        self.x = random.randint(0, self.screen.width - 1)
        self.y = random.randint(0, self.screen.height - 1)
        self.draw()

    def draw(self):
        """
            Draws the fruit on the screen.
        """
        self.screen.draw_char(self.x, self.y, self.fruit)

    def eat(self, snake):
        """
            Checks if the snake ate the fruit.
            If the snake ate the fruit, the fruit is regenerated.
        """
        if self.x == snake.x and self.y == snake.y:
            self.generate()
            snake.grow()

class Snake:
    """
        Create a head that is represented by the "@" charcter
        and a body with the "o" character
    """
    def __init__(self, screen):
        self.screen = screen
        self.x = 0
        self.y = 0
        self.body = []
        self.body.append(self.x)
        self.body.append(self.y)
        self.head = '@'
        self.body_char = 'o'
        self.direction = 'right'
        self.score = 0
        # treat the body as a movable wall