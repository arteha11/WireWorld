import pygame
import pygame_widgets

from logic import field, one_from_two
from constants import *
from buttons import *

import logging
logging.basicConfig(level=logging.INFO)


monitor_w = pygame.display.Info().current_w
monitor_h = pygame.display.Info().current_h
field_w = monitor_w // (CELL_SIZE + LINE_SIZE)
field_h = monitor_h // (CELL_SIZE + LINE_SIZE)

pygame.init()
pygame.display.init()

field.field["20/20"] = "3"
field.field["21/21"] = "3"
field.field["20/22"] = "1"
field.field["19/21"] = "2"

screen = pygame.display.set_mode((monitor_w, monitor_h), pygame.FULLSCREEN)
pygame.display.set_caption("WireWorld")

icon = pygame.image.load("icons\\icon.png")
pygame.display.set_icon(icon)

pygame.mouse.set_visible(False)


def darker_col(col):
    return col[0] * 0.75, col[1] * 0.75, col[2] * 0.75

def lighter_col(col):
    if col[0] * 1.25 < 255:
        r = col[0] * 1.25
    else:
        r = col[0]
    if col[1] * 1.25 < 255:
        g = col[1] * 1.25
    else:
        g = col[1]
    if col[2] * 1.25 < 255:
        b = col[2] * 1.25
    else:
        b = col[2]
    return r, g, b


def invert_screen_y(pos):
    return monitor_h - pos


def OnButton_switch(st):
    global OnButton
    OnButton = st


#drawing whole field
def draw_field(surface, field, mouse_x, mouse_y, draw_type):
    screen.fill(GRAY)
    for row in range(field_h):
        for col in range(field_w):
            cell = f"{col}/{row}"
            x = col * (CELL_SIZE + LINE_SIZE)
            y = row * (CELL_SIZE + LINE_SIZE)
            rect = pygame.Rect(
                x + LINE_SIZE,
                invert_screen_y(y + CELL_SIZE + LINE_SIZE),
                CELL_SIZE,
                CELL_SIZE,
                )
            pygame.draw.rect(surface, STATUS_TO_COL[field.field[cell]], rect)

#colouring cell that mouse on
    mouse_col = mouse_x // (CELL_SIZE + LINE_SIZE)
    mouse_row = mouse_y // (CELL_SIZE + LINE_SIZE) + 1
    rect = pygame.Rect(
        mouse_col * (CELL_SIZE + LINE_SIZE) + LINE_SIZE,
        invert_screen_y(mouse_row * (CELL_SIZE + LINE_SIZE)),
        CELL_SIZE, CELL_SIZE
    )
    pygame.draw.rect(surface, STATUS_TO_COL[draw_type.col], rect)

#drawing cursor
    mouse_rect1 = pygame.Rect(
        mouse_x, invert_screen_y(mouse_y), CELL_SIZE / 2, CELL_SIZE / 4
    )
    mouse_rect2 = pygame.Rect(
        mouse_x , invert_screen_y(mouse_y), CELL_SIZE / 4, CELL_SIZE / 2
    )
    pygame.draw.rect(surface, lighter_col(GRAY), mouse_rect1)
    pygame.draw.rect(surface, lighter_col(GRAY), mouse_rect2)


def main():
    f_update = pygame.USEREVENT
    pygame.time.set_timer(f_update, ITERATION_TIME)
    global draw_type

    OnButton = False
    run = True
    pause = False
    drawing = False

    while run:
        events = pygame.event.get()
        mouse_pos = pygame.mouse.get_pos()
        mouse_x = mouse_pos[0]
        mouse_y = invert_screen_y(mouse_pos[1])
        for event in events:
            if event.type == pygame.QUIT:
                run = False
            if event.type == f_update and pause != True:
                field.update()
            if event.type == pygame.KEYDOWN:
                curr_key = event.key
                match curr_key:
                    case pygame.K_p:
                        pause = not pause
                    case pygame.K_SPACE:
                        pause = not pause
                    case pygame.K_ESCAPE:
                        run = False
                    case pygame.K_1:
                        draw_type.col = "0"
                    case pygame.K_2:
                        draw_type.col = "3"
                    case pygame.K_3:
                        draw_type.col = "1"
                    case pygame.K_4:
                        draw_type.col = "2"
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
            if event.type == pygame.MOUSEBUTTONUP:
                drawing = False
            if drawing:
                mouse_col = mouse_x // (CELL_SIZE + LINE_SIZE)
                mouse_row = mouse_y // (CELL_SIZE + LINE_SIZE)
                if one_from_two(mouse_col, mouse_row) in field.field.keys() and OnButton == False:
                    field.field[one_from_two(mouse_col, mouse_row)] = draw_type.col

        draw_field(screen, field, mouse_x, mouse_y, draw_type)
        pygame_widgets.update(events)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()