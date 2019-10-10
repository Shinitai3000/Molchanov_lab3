import math as m
from graph import *
import random


def domic(x, y, k):
    A = []
    # Большой прямоугольник
    penColor(43, 34, 0)
    brushColor(43, 34, 0)
    rectangle(x - 213 * k, y - 288 * k, x + 213 * k, y + 288 * k)
    # Крыша
    p = [(x - 247 * k, y - 288 * k), (x - 190 * k, y - 334 * k), (x + 190 * k, y - 334 * k), (x + 247 * k, y - 288 * k)]
    penColor(0, 0, 0)
    brushColor(0, 0, 0)
    polygon(p)
    # Трубы
    penColor(26, 26, 26)
    brushColor(26, 26, 26)
    rectangle(x - 137 * k, y - 311 * k, x - 150 * k, y - 381 * k)
    rectangle(x - 101 * k, y - 306 * k, x - 126 * k, y - 436 * k)
    rectangle(x + 51 * k, y - 334 * k, x + 39 * k, y - 391 * k)
    rectangle(x + 157 * k, y - 306 * k, x + 143 * k, y - 391 * k)
    # Окна
    penColor(72, 62, 55)
    brushColor(72, 62, 55)
    A.append(rectangle(x - 183 * k, y - 288 * k, x - 137 * k, y - 68 * k))
    A.append(rectangle(x - 101 * k, y - 288 * k, x - 55 * k, y - 68 * k))
    A.append(rectangle(x + 5 * k, y - 288 * k, x + 51 * k, y - 68 * k))
    A.append(rectangle(x + 111 * k, y - 288 * k, x + 157 * k, y - 68 * k))
    # Квадратики снизу
    penColor(43, 17, 0)
    brushColor(43, 17, 0)
    A.append(rectangle(x - 168 * k, y + 220 * k, x - 88 * k, y + 120 * k))
    A.append(rectangle(x - 42 * k, y + 220 * k, x + 38 * k, y + 120 * k))
    penColor(212, 170, 0)
    brushColor(212, 170, 0)
    A.append(rectangle(x + 84 * k, y + 220 * k, x + 164 * k, y + 120 * k))
    # Заборчик
    penColor(26, 26, 26)
    brushColor(26, 26, 26)
    rectangle(x - 253 * k, y - 60 * k, x + 253 * k, y - 0 * k)
    rectangle(x - 243 * k, y - 60 * k, x - 228 * k, y - 110 * k)
    rectangle(x + 243 * k, y - 60 * k, x + 228 * k, y - 110 * k)
    for i in range(5):
        rectangle(x - (186 - 81 * i) * k, y - 60 * k, x - (160 - 81 * i) * k, y - 110 * k)
    rectangle(x - 228 * k, y - 110 * k, x + 228 * k, y - 135 * k)
    return A


def ovalchik(x0, y0, A, B, f):
    n = 50
    a = []
    for i in range(n):
        x = x0 + A * m.cos(2 * m.pi * i / n)
        y = y0 + B * m.sin(2 * m.pi * i / n)
        x_f = x0 + (x - x0) * m.cos(f) - (y - y0) * m.sin(f)
        y_f = y0 + (y - y0) * m.cos(f) + (x - x0) * m.sin(f)
        a.append((x_f, y_f))
    return polygon(a)


obj = 0
obj1 = 0
obj2 = 0
obj3 = 0


def prizrak(x, y, s):
    A = []
    # Тело
    penColor(180, 180, 181)
    brushColor(180, 180, 181)
    p = [(x + 0 * s, y + 0 * s), (x - 2 * s, y), (x - 8 * s, y + 8 * s), (x - 9 * s, y + 14 * s),
         (x - 9 * s, y + 17 * s),
         (x - 12 * s, y + 24), (x - 16 * s, y + 36 * s), (x - 11 * s, y + 43 * s), (x - 16 * s, y + 55 * s),
         (x - 28 * s, y + 56 * s), (x - 32 * s, y + 64 * s), (x - 37 * s, y + 74 * s), (x - 41 * s, y + 83 * s),
         (x - 45 * s, y + 89 * s), (x - 53 * s, y + 77 * s), (x - 59 * s, y + 95 * s), (x - 62 * s, y + 116 * s),
         (x - 46 * s, y + 110 * s), (x - 40 * s, y + 108 * s), (x - 31 * s, y + 105 * s), (x - 29 * s, y + 104 * s),
         (x - 15 * s, y + 109 * s), (x - 10 * s, y + 117 * s), (x + 4 * s, y + 119 * s), (x + 13 * s, y + 115 * s),
         (x + 24 * s, y + 108 * s), (x + 43 * s, y + 104 * s), (x + 60 * s, y + 106 * s), (x + 64 * s, y + 107 * s),
         (x + 76 * s, y + 99 * s), (x + 81 * s, y + 95 * s), (x + 80 * s, y + 90 * s), (x + 80 * s, y + 79 * s),
         (x + 83 * s, y + 72 * s), (x + 89 * s, y + 72 * s), (x + 97 * s, y + 70 * s), (x + 103 * s, y + 61 * s),
         (x + 99 * s, y + 53 * s), (x + 96 * s, y + 44 * s), (x + 88 * s, y + 57 * s), (x + 79 * s, y + 32 * s),
         (x + 66 * s, y + 14 * s), (x + 63 * s, y + 9 * s), (x + 57 * s, y - 1 * s), (x + 51 * s, y - 10 * s),
         (x + 35 * s, y - 16 * s), (x + 28 * s, y - 17 * s), (x + 18 * s, y - 17 * s), (x + 5 * s, y - 6 * s),
         (x - 2 * s, y + 1 * s)]
    A.append(polygon(p))

    # Поправки к телу
    A.append(ovalchik(x + 87 * s, y + 46 * s, 18 * s, 7 * s, m.pi / 4))
    A.append(ovalchik(x - 59 * s, y + 110 * s, 10 * s, 3 * s, - m.pi / 4))
    A.append(ovalchik(x - 37 * s, y + 82 * s, 18 * s, 15 * s, - m.pi / 4))
    A.append(ovalchik(x - 21 * s, y + 46 * s, 38 * s, 8 * s, -1.3 * m.pi / 4))
    # Голова
    A.append(circle(x + 15 * s, y + 1 * s, 25 * s))
    # Глаза
    brushColor(136, 206, 223)
    A.append(circle(x + 0 * s, y - 1 * s, 8 * s))
    A.append(circle(x + 22 * s, y - 7 * s, 8 * s))
    # Зрачки
    brushColor(0, 0, 0)
    A.append(circle(x - 2 * s, y - 1 * s, 3 * s))
    A.append(circle(x + 20 * s, y - 6 * s, 3 * s))
    # Овалы на зрачках
    penColor(255, 255, 255)
    brushColor(255, 255, 255)
    A.append(ovalchik(x + 3 * s, y - 5 * s, 5 * s, 2 * s, - 0.7 * m.pi / 4))
    A.append(ovalchik(x + 25 * s, y - 10 * s, 5 * s, 2 * s, -0.7 * m.pi / 4))
    return A


def prizrak2(x, y, s):
    # Тело
    penColor(180, 180, 181)
    brushColor(180, 180, 181)
    p = [(x - 0 * s, y + 0 * s), (x + 2 * s, y), (x + 8 * s, y + 8 * s), (x + 9 * s, y + 14 * s),
         (x + 9 * s, y + 17 * s),
         (x + 12 * s, y + 24), (x + 16 * s, y + 36 * s), (x + 11 * s, y + 43 * s), (x + 16 * s, y + 55 * s),
         (x + 28 * s, y + 56 * s), (x + 32 * s, y + 64 * s), (x + 37 * s, y + 74 * s), (x + 41 * s, y + 83 * s),
         (x + 45 * s, y + 89 * s), (x + 53 * s, y + 77 * s), (x + 59 * s, y + 95 * s), (x + 62 * s, y + 116 * s),
         (x + 46 * s, y + 110 * s), (x + 40 * s, y + 108 * s), (x + 31 * s, y + 105 * s), (x + 29 * s, y + 104 * s),
         (x + 15 * s, y + 109 * s), (x + 10 * s, y + 117 * s), (x - 4 * s, y + 119 * s), (x - 13 * s, y + 115 * s),
         (x - 24 * s, y + 108 * s), (x - 43 * s, y + 104 * s), (x - 60 * s, y + 106 * s), (x - 64 * s, y + 107 * s),
         (x - 76 * s, y + 99 * s), (x - 81 * s, y + 95 * s), (x - 80 * s, y + 90 * s), (x - 80 * s, y + 79 * s),
         (x - 83 * s, y + 72 * s), (x - 89 * s, y + 72 * s), (x - 97 * s, y + 70 * s), (x - 103 * s, y + 61 * s),
         (x - 99 * s, y + 53 * s), (x - 96 * s, y + 44 * s), (x - 88 * s, y + 57 * s), (x - 79 * s, y + 32 * s),
         (x - 66 * s, y + 14 * s), (x - 63 * s, y + 9 * s), (x - 57 * s, y - 1 * s), (x - 51 * s, y - 10 * s),
         (x - 35 * s, y - 16 * s), (x - 28 * s, y - 17 * s), (x - 18 * s, y - 17 * s), (x - 5 * s, y - 6 * s),
         (x + 2 * s, y + 1 * s)]
    polygon(p)
    # Поправки к телу
    ovalchik(x - 87 * s, y + 46 * s, 18 * s, 7 * s, -m.pi / 4)
    ovalchik(x + 59 * s, y + 110 * s, 10 * s, 3 * s, + m.pi / 4)
    ovalchik(x + 37 * s, y + 82 * s, 18 * s, 15 * s, + m.pi / 4)
    ovalchik(x + 21 * s, y + 46 * s, 38 * s, 8 * s, -1.3 * (-m.pi / 4))
    # Голова
    circle(x - 15 * s, y + 1 * s, 25 * s)
    # Глаза
    brushColor(136, 206, 223)
    circle(x - 0 * s, y - 1 * s, 8 * s)
    circle(x - 22 * s, y - 7 * s, 8 * s)
    # Зрачки
    brushColor(0, 0, 0)
    circle(x + 2 * s, y - 1 * s, 3 * s)
    circle(x - 20 * s, y - 6 * s, 3 * s)
    # Овалы на зрачках
    penColor(255, 255, 255)
    brushColor(255, 255, 255)
    ovalchik(x - 3 * s, y - 5 * s, 5 * s, 2 * s, 0.7 * m.pi / 4)
    ovalchik(x - 25 * s, y - 10 * s, 5 * s, 2 * s, 0.7 * m.pi / 4)


COORDINATES = []


def coord(event):
    COORDINATES.append((event.x, event.y))
    print(COORDINATES)


onMouseDown(coord)

canvasSize(500, 660)
windowSize(500, 660)

brushColor(102, 102, 102)
polygon([(500, 0), (500, 250), (0, 250), (0, 0)])

penColor(102, 102, 102)
brushColor(231, 231, 231)
obj4 = circle(436, 60, 45)

penColor("Black")
brushColor(0, 0, 0)
polygon([(500, 250), (500, 660), (0, 660), (0, 250)])

prizrak(340, 520, 0.5)
prizrak(420, 340, 0.5)
prizrak(450, 386, 0.5)
prizrak2(90, 505, 0.6)
prizrak2(114, 566, 0.8)

obj1 = domic(423, 220, 0.3)
obj2 = domic(254, 329, 0.3)
penColor(48, 48, 48)
brushColor(48, 48, 48)
ovalchik(140, 364, 100, 30, 0)
obj3 = domic(99, 375, 0.3)
penColor(48, 48, 48)
brushColor(48, 48, 48)
ovalchik(385, 300, 150, 20, 0)

penColor(30, 20, 30)
brushColor(30, 20, 30)
ovalchik(410, 146, 180, 30, 0)

penColor(50, 50, 45)
brushColor(50, 50, 45)
ovalchik(453, 93, 100, 20, 0)

penColor(20, 20, 30)
brushColor(20, 20, 30)
ovalchik(175, 62, 200, 35, 0)

vx = 1
vy = 1
x = 376
y = 472
iiiiiiii = 0

obj = prizrak(x, y, 1)


def F():
    global obj
    global obj1
    global obj2
    global obj3
    global vx
    global vy
    global x
    global y
    global iiiiiiii
    if ((x + 100 > 500) or (x - 65 < 0)):
        vx = -vx
    if ((y + 125 > 660) or (y - 25 < 0)):
        vy = -vy
    for i in obj:
        moveObjectBy(i, vx, vy)
    x += vx
    y += vy
    for i in obj1:
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        col = "#%02X%02X%02X" % (r, g, b)
        changeFillColor(i, col)
    for i in obj2:
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        col = "#%02X%02X%02X" % (r, g, b)
        changeFillColor(i, col)
    for i in obj3:
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        col = "#%02X%02X%02X" % (r, g, b)
        changeFillColor(i, col)
    r = iiiiiiii % 512
    g = 255
    if r > 255:
        r = 511 - r
        col = "#%02X%02X%02X" % (g, r, r)
        changeFillColor(obj4, col)
    else:
        col = "#%02X%02X%02X" % (g, r, r)
        changeFillColor(obj4, col)
    iiiiiiii += 1


onTimer(F, 16)
run()
