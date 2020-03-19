#tiling program
import turtle as t
import math as m

n = 6
side_len = 10
color = 'brown'

def hexagon(x, y, side_len, color):
    t.goto(x, y)
    t.down()
    t.right(30)
    for i in range(6):
        t.forward(side_len)
        t.left(60)
    t.left(30)
    t.up()


def hexagons_line(n, x, y, side_len, color):
    if n == 1:
        hexagon(x, y, side_len, color)
    else:
        hexagon(x, y, side_len, color)
        hexagons_line(n - 1, x + (m.sqrt(3) * side_len), y, side_len, color)


def hexagons_tiles(n1, n, x, y, side_len, color):
    if n1 == 1:
        hexagons_line(n, x, y, side_len, color)

    else:
        hexagons_line(n, x, y, side_len, color)
        if n1 % 2 != 0:
            t.up()
            x_new = x - side_len
            y_new = y - side_len - (side_len / 2)
            hexagons_tiles(n1 - 1, n, x_new, y_new, side_len, color)
            t.down()

        else:
            t.up()
            x_new = x - side_len
            y_new = y - side_len - (side_len / 2)
            hexagons_tiles(n1 - 1, n, x_new, y_new, side_len, color)
            t.down()

hexagons_tiles(n, n, 0, 0, side_len, color)
#x_new = x - ((n - 1) * (m.sqrt(3) * side_len)) - (side_len / 2)
#y_new = y - side_len - (side_len / 2)