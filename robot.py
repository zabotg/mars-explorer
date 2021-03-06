#!/usr/bin/env python3
# -*- coding: utf-8 -*

#---------------------------------------------
# Created By  : Guilherme Felipe Zabot
# Created Date: 2022-04-26
# version ='1.0'
# --------------------------------------------
class Robot():
    def __init__(self, x, y, facing):
        self.x = x
        self.y = y
        self.facing = facing
        self.positions = ['N', 'E', 'S', 'W']

    def move(self, commands):
        for command in commands:
            if command == 'L':
                self.facing = self.facing_left()
            elif command == 'R':
                self.facing = self.facing_right()
            elif command == 'M':
                self.move_forward()
            else:
                return 'Invalid command'

    def facing_left(self):
        index = self.positions.index(self.facing)
        if(index == 0):
            return self.positions[3]
        else:
            return self.positions[index - 1]

    def facing_right(self):
        index = self.positions.index(self.facing)
        if(index == 3):
            return self.positions[0]
        else:
            return self.positions[index + 1]

    def move_forward(self):
        if self.facing == 'N':
            self.y += 1
        elif self.facing == 'E':
            self.x += 1
        elif self.facing == 'S':
            self.y -= 1
        elif self.facing == 'W':
            self.x -= 1

    def print_position(self):
        print(self.x, self.y, self.facing)