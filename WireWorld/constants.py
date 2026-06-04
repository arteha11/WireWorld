CELL_SIZE = 15 #px
LINE_SIZE = 1  #px
ITERATION_TIME = 200 #ms

# colours
COL_EMPTY = (20, 20, 20)
COL_CURRENT = (100, 255, 255)
COL_TALE = (255, 70, 70)
COL_WIRE = (255, 190, 25)
GRAY = (90, 90, 90)

NEIGHBOURS_PL = [-1, 0, 1]


ITERATION_TO_ITERATION = {
    "0": "0",
    "1": "2",
    "2": "3"
}

STATUS_TO_COL = {
    "0": COL_EMPTY,
    "1": COL_CURRENT,
    "2": COL_TALE,
    "3": COL_WIRE
}