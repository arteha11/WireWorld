from main import screen, monitor_w, monitor_h, invert_screen_y, darker_col, lighter_col, OnButton_switch
from constants import COL_EMPTY, COL_WIRE, COL_CURRENT, COL_TALE

from pygame_widgets.button import Button


class button_col:
    col = "3"
    def change_col(self, col):
        self.col = col

draw_type = button_col()


button_empty = Button(
    screen, monitor_w - 170, invert_screen_y(monitor_h - 10), 30, 30,
    inactiveColour=COL_EMPTY,
    hoverColour=lighter_col(COL_EMPTY),
    pressedColour=darker_col(COL_EMPTY), radius=2,
    onClick=lambda: draw_type.change_col("0")
)
button_wire = Button(
    screen, monitor_w - 130, invert_screen_y(monitor_h - 10), 30, 30,
    inactiveColour=COL_WIRE,
    hoverColour=lighter_col(COL_WIRE),
    pressedColour=darker_col(COL_WIRE), radius=2,
    onClick=lambda: draw_type.change_col("3")
)
button_current = Button(
    screen, monitor_w - 90, invert_screen_y(monitor_h - 10), 30, 30,
    inactiveColour=COL_CURRENT,
    hoverColour=lighter_col(COL_CURRENT),
    pressedColour=darker_col(COL_CURRENT), radius=2,
    onClick=lambda: draw_type.change_col("1")
)
button_tale = Button(
    screen, monitor_w - 50, invert_screen_y(monitor_h - 10), 30, 30,
    inactiveColour=COL_TALE,
    hoverColour=lighter_col(COL_TALE),
    pressedColour=darker_col(COL_TALE), radius=2,
    onClick=lambda: draw_type.change_col("2"),
    onHover=lambda: OnButton_switch(True)
)
#button_gear = Button(
#    screen, 50, invert_screen_y(monitor_h - 10), 30, 30,
#    inactiveColour=(0, 0, 0, 0),
#    hoverColour=(0, 0, 0, 0),
#    pressedColour=(0, 0, 0, 0), radius=2,
#    onClick=lambda: draw_type.change_col("2")
#)