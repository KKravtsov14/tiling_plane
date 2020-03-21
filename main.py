#tiling program
#Developers: Kravtsov - 80%
import turtle as t

def main():

    colors = {2: 'red', -1: 'orange', 1: 'yellow', -3: 'green', 3: 'blue', -2: 'purple', 4: 'black', -4: 'white'}

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

    color_1 = get_color_choice()

    n = int(input('Введите количество шестиугольников в ряду(от 4 до 20):'))
    if not 4 <= n <= 20:
        n = try_n(n)

    for i in colors:
        if color_1 == colors[i]:
            color = i

    if n == 4:
        t.up()
        t.speed(0)
        hexagons_tiles(n, n, -490, 250, 125, color, 1.615, 1.85)
        t.mainloop()

    elif n == 5:
        t.up()
        t.speed(0)
        hexagons_tiles(n, n, -400, 250, 100, color, 1.64, 1.825)
        t.mainloop()
    elif n == 6:
        t.up()
        t.speed(0)
        hexagons_tiles(n, n, -450, 250, 80, color, 1.655, 1.81)
        t.mainloop()

    elif n == 7:
        t.up()
        t.speed(0)
        hexagons_tiles(n, n, -400, 280, 70, color, 1.67, 1.79)
        t.mainloop()

    elif n == 8:
        t.up()
        t.speed(0)
        hexagons_tiles(n, n, -450, 280, 60, color, 1.68, 1.78)
        t.mainloop()

    elif n == 9:
        t.up()
        t.speed(0)
        hexagons_tiles(n, n, -380, 295, 55, color, 1.69, 1.775)
        t.mainloop()

    elif n == 10:
        t.up()
        t.speed(0)
        hexagons_tiles(n, n, -450, 290, 48, color, 1.69, 1.775)
        t.mainloop()

    elif n == 11:
        t.up()
        t.speed(0)
        hexagons_tiles(n, n, -385, 300, 42, color, 1.695, 1.77)
        t.mainloop()

    elif n == 12:
        t.up()
        t.speed(0)
        hexagons_tiles(n, n, -415, 300, 38, color, 1.7, 1.765)
        t.mainloop()

    elif n == 13:
        t.up()
        t.speed(0)
        hexagons_tiles(n, n, -385, 300, 35, color, 1.7, 1.765)
        t.mainloop()

    elif n == 14:
        t.up()
        t.speed(0)
        hexagons_tiles(n, n, -405, 300, 32, color, 1.705, 1.76)
        t.mainloop()

    elif n == 15:
        t.up()
        t.speed(0)
        hexagons_tiles(n, n, -380, 300, 30, color, 1.705, 1.76)
        t.mainloop()

    elif n == 16:
        t.up()
        t.speed(0)
        hexagons_tiles(n, n, -410, 310, 29, color, 1.71, 1.755)
        t.mainloop()

    elif n == 17:
        t.up()
        t.speed(0)
        hexagons_tiles(n, n, -390, 315, 27, color, 1.71, 1.755)
        t.mainloop()

    elif n == 18:
        t.up()
        t.speed(0)
        hexagons_tiles(n, n, -405, 315, 25, color, 1.71, 1.755)
        t.mainloop()

    elif n == 19:
        t.up()
        t.speed(0)
        hexagons_tiles(n, n, -390, 315, 24, color, 1.715, 1.75)
        t.mainloop()

    elif n == 20:
        t.up()
        t.speed(0)
        hexagons_tiles(n, n, -405, 315, 22.5, color, 1.715, 1.75)
        t.mainloop()

def get_color_choice():
    color_1 = input('Введите цвет:')
    lst = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black', 'white']
    while color_1 not in lst:
        color_1 = input('Некорректный ввод первого цвета. Повторите еще раз:')
    return color_1


def try_n(n):
    lst = []
    for i in range(4, 20):
        lst.append(str(i))
    while n not in lst:
        n = input('Некорректный ввод шестиугольников. Повторите еще раз:')
    return int(n)


def draw_hexagon(x, y, side_len, color):
    colors = {2: 'red', -1: 'orange', 1: 'yellow', -3: 'green', 3: 'blue', -2: 'purple', 4: 'black', -4: 'white'}
    t.pencolor('black')
    t.begin_fill()
    t.up()
    t.goto(x, y)
    t.right(30)
    t.down()
    for i in range(6):
        t.forward(side_len)
        t.left(60)
    t.left(30)
    t.fillcolor(colors[color])
    t.end_fill()
    t.up()


def hexagons_line(n, x, y, side_len, color):
    if n == 1:
        draw_hexagon(x, y, side_len, color)
    else:
        t.up()
        draw_hexagon(x, y, side_len, color)
        t.up()
        hexagons_line(n - 1, x + (m.sqrt(3) * side_len), y, side_len, -color)


def hexagons_tiles(n1, n, x, y, side_len, color, coef2, coef1):
    if n1 == 1:
        hexagons_line(n, x, y, side_len, color)

    else:
        hexagons_line(n, x, y, side_len, color)
        if n1 % 2 != 0:
            t.up()
            t.backward(((n - 1) * (coef1 * side_len)) + (side_len / 2))
            x_new = t.xcor()
            y_new = y - side_len - (side_len / 2)
            t.up()
            hexagons_tiles(n1 - 1, n, x_new, y_new, side_len, color, coef2, coef1)

        else:
            t.up()
            t.backward(((n - 1) * (coef2 * side_len)) - (side_len / 2))
            x_new = t.xcor()
            y_new = y - side_len - (side_len / 2)
            hexagons_tiles(n1 - 1, n, x_new, y_new, side_len, color, coef2, coef1)

main()