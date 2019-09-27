import math as m
from graph import *


def domic(x, y, k):
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
    rectangle(x - 183 * k, y - 288 * k, x - 137 * k, y - 68 * k)
    rectangle(x - 101 * k, y - 288 * k, x - 55 * k, y - 68 * k)
    rectangle(x + 5 * k, y - 288 * k, x + 51 * k, y - 68 * k)
    rectangle(x + 111 * k, y - 288 * k, x + 157 * k, y - 68 * k)
    # Квадратики снизу
    penColor(43, 17, 0)
    brushColor(43, 17, 0)
    rectangle(x - 168 * k, y + 220 * k, x - 88 * k, y + 120 * k)
    rectangle(x - 42 * k, y + 220 * k, x + 38 * k, y + 120 * k)
    penColor(212, 170, 0)
    brushColor(212, 170, 0)
    rectangle(x + 84 * k, y + 220 * k, x + 164 * k, y + 120 * k)
    # Заборчик
    penColor(26, 26, 26)
    brushColor(26, 26, 26)
    rectangle(x - 253 * k, y - 60 * k, x + 253 * k, y - 0 * k)
    rectangle(x - 243 * k, y - 60 * k, x - 228 * k, y - 110 * k)
    rectangle(x + 243 * k, y - 60 * k, x + 228 * k, y - 110 * k)
    for i in range(5):
        rectangle(x - (186 - 81 * i) * k, y - 60 * k, x - (160 - 81 * i) * k, y - 110 * k)
    rectangle(x - 228 * k, y - 110 * k, x + 228 * k, y - 135 * k)


def ovalchik(x0, y0, A, B, f):
    n = 50
    a = []
    for i in range(n):
        x = x0 + A * m.cos(2 * m.pi * i / n)
        y = y0 + B * m.sin(2 * m.pi * i / n)
        x_f = x0 + (x - x0) * m.cos(f) - (y - y0) * m.sin(f)
        y_f = y0 + (y - y0) * m.cos(f) + (x - x0) * m.sin(f)
        a.append((x_f, y_f))
    polygon(a)


def prizrak(x, y, s):
    #Тело
    penColor(180, 180, 181)
    brushColor(180, 180, 181)
    p = [(x + 0 * s, y + 0 * s), (x - 2 * s, y), (x - 8 * s, y + 8 * s), (x - 9 * s, y + 14 * s), (x - 9 * s, y + 17 * s),
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
    polygon(p)
    #Поправки к телу
    ovalchik(x + 87 * s, y + 46 * s, 18 * s , 7 * s, m.pi/4)
    ovalchik(x - 59 * s, y + 110 * s, 10 * s, 3 * s, - m.pi/4)
    ovalchik(x - 37 * s, y + 82 * s, 18 * s, 15 * s, - m.pi/4)
    ovalchik(x - 21 * s, y + 46 * s, 38 * s , 8 * s, -1.3 * m.pi/4)
    #Голова
    circle(x + 15 * s, y + 1 * s, 25 * s)
    #Глаза
    brushColor(136, 206, 223)
    circle(x + 0 * s, y - 1 * s, 8 * s)
    circle(x + 22 * s, y - 7 * s, 8 * s)
    #Зрачки
    brushColor(0, 0, 0)
    circle(x - 2 * s, y - 1 * s, 3 * s)
    circle(x + 20 * s, y - 6 * s, 3 * s)
    #Овалы на зрачках
    penColor(255, 255, 255)
    brushColor(255, 255, 255)
    ovalchik(x + 3 * s, y - 5 * s, 5 * s, 2 * s, - 0.7 * m.pi / 4)
    ovalchik(x + 25 * s, y - 10 * s, 5 * s, 2 * s, -0.7 * m.pi / 4)


COORDINATES = []
def coord(event):
    COORDINATES.append((event.x, event.y))
    print(COORDINATES)

onMouseDown(coord)

canvasSize(500, 660)
windowSize(500, 660)

prizrak(300,200,1)


run()
