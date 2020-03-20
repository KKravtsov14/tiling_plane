#tiling program
import turtle as t
import math as m


colors = {1: 'red', 2: 'orange', 3: 'yellow', 4: 'green', 5: 'blue', 6: 'purple', 7: 'black', 8: 'white'}
side_len = 10
def main():
    while True:
        print('''
Доступные цвета раскрашивания:
1. Красный
2. Оранжевый
3. Желтый
4. Зеленый
5. Синий
6. Фиолетовый
7. Черный
8. Белый''')
        color_1 = input('Введите первый цвет(цифру):')
        color_1 = try_color_1(color_1)
        color_2 = input('Введите второй цвет(цифру):')
        color_2 = try_color_2(color_2)
        n = input('Введите количество шестиугольников в ряду(от 4 до 16):')
        color = [color_1, color_2]
        n = try_n(n)
        hexagons_tiles(n, n, 0, 0, side_len, color)

def try_color_1(color_1):
    lst = ['1', '2', '3', '4', '5', '6', '7', '8']
    while color_1 not in lst:
        color_1 = input('Некорректный ввод первого цвета. Повторите еще раз:')
    return int(color_1)
def try_color_2(color_2):
    lst = ['1', '2', '3', '4', '5', '6', '7', '8']
    while color_2 not in lst:
        color_2 = input('Некорректный ввод второго цвета. Повторите еще раз:')
    return int(color_2)
def try_n(n):
    lst = []
    for i in range(4, 20):
        lst.append(str(i))
    while n not in lst:
        n = input('Некорректный ввод шестиугольников. Повторите еще раз:')
    return int(n)

def hexagon(x, y, side_len, color):
    t.color(colors[color[1]])
    t.begin_fill()
    t.goto(x, y)
    t.down()
    t.right(30)
    for i in range(6):
        t.forward(side_len)
        t.left(60)
    t.left(30)
    t.end_fill()
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
            t.backward(((n - 1) * (1.8 * side_len)) + (side_len / 2))
            x_new = t.xcor()
            y_new = y - side_len - (side_len / 2)
            hexagons_tiles(n1 - 1, n, x_new, y_new, side_len, color)
            t.down()

        else:
            t.up()
            t.backward(((n - 1) * (1.7 * side_len)) - (side_len / 2))
            x_new = t.xcor()
            y_new = y - side_len - (side_len / 2)
            hexagons_tiles(n1 - 1, n, x_new, y_new, side_len, color)
            t.down()
main()
#hexagons_tiles(n, n, 0, 0, side_len, color)