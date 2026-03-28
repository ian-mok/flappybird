import pygame
import random

class Apple:
    def __init__(self):
        self.colour =(0,0,255)
        self.body = [random.randint (0,800) // 10 * 10,random.randint(0,600) //10 * 10]

    def reset_apple(self):
            self.body = [random.randint(0, 800) // 10 * 10, random.randint(0, 600) // 10 * 10]



