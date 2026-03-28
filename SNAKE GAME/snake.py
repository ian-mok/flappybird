import pygame
class Snake:
    def __init__(self):
        self.color = (0,0,255)
        self.head =[10,40]
        self.body = [[10,40],[10,30],[10,20],[10,10]]
        self.direction = "down"


    def move(self):
        if self.direction == "down":
            self.head[1] = self.head[1] + 10
        if self.direction == "up":
            self.head[1] = self.head[1] - 10
        if self.direction == "left":
            self.head[0] = self.head[0] - 10
        if self.direction == "right":
            self.head[0] = self.head[0] + 10
        self.body.insert(0, list(self.head))


    def hit_wall(self):
        if self.head[0] > 800 or self.head[0] < 0 or self.head[1]>600 or self.head[1]< 0:


            return True
        else:
            return False

    def hit_body(self):
        for i in range(1, len(self.body)):
            if self.head[0] == self.body[i][0] and self.head[1] == self.body[i][1]:

               return True
        return False
    def add_length(self, added):
        if not added:
            self.body.pop()













