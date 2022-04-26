#!/usr/bin/env python3
# -*- coding: utf-8 -*

#---------------------------------------------
# Created By  : Guilherme Felipe Zabot
# Created Date: 2022-04-26
# version ='1.0'
# --------------------------------------------

from robot import Robot

def read_file(file):
    with open(file) as f:
        return f.read().splitlines()

def main():
    lines = read_file('input.txt')

    board_size = lines[0].split() 
    for i in range(1, len(lines), 2):
        x, y, face = lines[i].split()
        x = int(x);
        y = int(y);

        commands = list(lines[i + 1])

        robot = Robot(x, y, face)
        robot.move(commands)

        robot.print_position()

if __name__ == "__main__":
    main()