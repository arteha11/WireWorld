from constants import *

import pygame
pygame.init()


monitor_w = pygame.display.Info().current_w
monitor_h = pygame.display.Info().current_h

field_w = monitor_w // (CELL_SIZE + LINE_SIZE)
field_h = monitor_h // (CELL_SIZE + LINE_SIZE)


class cell_field:
    field = None

    def __init__(self, field):
        self.field = field

    def update(self):
        next_iteration_field = {}
        for cell in self.field.keys():
            next_iteration_field[cell] = next_iteration_status(cell, field)
        self.field = next_iteration_field


field = {}
for i in range(field_h):
    for j in range(field_w):
        field[str(j) + "/" + str(i)] = "0"
field = cell_field(field)


high = [i for i in range(field_h, 0, -1)]
length = [i for i in range(1, field_w + 1)]


"""
There are 4 types of cell:

empty   -  0
current -  1
tale    -  2
wire    -  3
"""


def two_from_one(one):
    splited = one.split("/")
    return int(splited[0]), int(splited[1])


def one_from_two(num, lett):
    return str(num) + "/" + str(lett)


# function for counting neighbours are current. 0, 1, 2 or more (3)
def count_of_neighbours_are_current(cell, field):
    num, lett = two_from_one(cell)

    neighbours_are_current = 0
    break_neediness = False

    neighbours = []

    for high_pl in NEIGHBOURS_PL:
        if break_neediness:
            break
        for length_pl in NEIGHBOURS_PL:
            if neighbours_are_current > 2:
                break_neediness = True
                break
            if high_pl == 0 and length_pl == 0:
                continue
            neighbour_num = length[(num - 1 + length_pl) % field_w]
            neighbour_lett = high[-(lett + high_pl) % field_h]
            neighbour = one_from_two(neighbour_num, neighbour_lett)
            neighbours.append(neighbour)
            if neighbour in field.field.keys():
                if field.field[neighbour] == "1":
                    neighbours_are_current += 1
    return neighbours_are_current


# function for calculating type of cell on the next iteration
def next_iteration_status(cell, field):
    if field.field[cell] != "3":
        result = ITERATION_TO_ITERATION[field.field[cell]]
    else:
        if count_of_neighbours_are_current(cell, field) in [1, 2]:
            result = "1"
        else:
            result = "3"
    return result


def terminal_visualization(field):
    n = 0
    fields = []
    for cell in field.keys():
        n += 1
        fields.append(field[cell])
        if n == field_w:
            print(fields)
            n = 0
            fields = []