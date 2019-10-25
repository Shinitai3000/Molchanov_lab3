from graph import *
import math as m


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


COORDINATES = []


def coord(event):
    COORDINATES.append((event.x, event.y))
    print(COORDINATES)


onMouseDown(coord)


def chelovek(x, y, s, f):
    #Тело
    penColor(200, 110, 250)
    brushColor(200, 110, 250)
    ovalchik(x, y + 105 * s, 105 * s, 50 * s, m.pi / 2)
    # Голова
    penColor(255, 240, 200)
    brushColor(255, 240, 200)
    circle(x, y, 34 * s)
    # Левая рука
    penColor(0, 0, 0)
    line(x - 40 * s, y + 44 * s, x - 125 * s, y + 130 * s)
    # Правая рука
    penColor(0, 0, 0)
    line(x + 40 * s, y + 44 * s, x + 125 * s, y + 130 * s)
    # Ноги
    penColor(0, 0, 0)
    line(x - 20 * s, y + 200 * s, x - 65 * s, y + 200 * s + 110 * f)
    line(x + 20 * s, y + 200 * s, x + 40 * s, y + 200 * s + 110 * f)
    # Ступни
    line(x - 65 * s, y + 210 * s + 100 * f, x - 95 * s, y + 210 * s + 100 * f)
    line(x + 40 * s, y + 210 * s + 100 * f, x + 60 * s, y + 210 * s + 100 * f)


def nechelovek(x, y, s, f):
    # Тело
    telo = [(x, y), (x - 65 * s, y + 210 * s), (x + 65 * s, y + 210 * s)]
    penColor(250, 110, 180)
    brushColor(250, 110, 180)
    polygon(telo)
    # Голова
    penColor(255, 240, 200)
    brushColor(255, 240, 200)
    circle(x, y, 34 * s)
    # Левая рука
    penColor(0, 0, 0)
    line(x - 15 * s, y + 44 * s, x - 100 * s, y + 130 * s)
    # Правая рука
    penColor(0, 0, 0)
    line(x + 15 * s, y + 44 * s, x + 100 * s, y + 130 * s)
    # Ноги
    penColor(0, 0, 0)
    line(x - 20 * s, y + 210 * s, x - 20 * s, y + 210 * s + 100 * f)
    line(x + 20 * s, y + 210 * s, x + 20 * s, y + 210 * s + 100 * f)
    # Ступни
    line(x - 20 * s, y + 210 * s + 100 * f, x - 40 * s, y + 210 * s + 100 * f)
    line(x + 20 * s, y + 210 * s + 100 * f, x + 40 * s, y + 210 * s + 100 * f)


def nechelovek_left(x, y, s, f):
    # Тело
    telo = [(x, y), (x - 65 * s, y + 210 * s), (x + 65 * s, y + 210 * s)]
    penColor(250, 110, 180)
    brushColor(250, 110, 180)
    polygon(telo)
    # Голова
    penColor(255, 240, 200)
    brushColor(255, 240, 200)
    circle(x, y, 34 * s)
    # Левая рука
    penColor(0, 0, 0)
    line(x - 15 * s, y + 44 * s, x - 100 * s, y + 130 * s)
    # Правая рука
    penColor(0, 0, 0)
    line(x + 15 * s, y + 44 * s, x + 50 * s, y + 75 * s)
    line(x + 50 * s, y + 75 * s, x + 85 * s, y + 44 * s)
    # Ноги
    penColor(0, 0, 0)
    line(x - 20 * s, y + 210 * s, x - 20 * s, y + 210 * s + 100 * f)
    line(x + 20 * s, y + 210 * s, x + 20 * s, y + 210 * s + 100 * f)
    # Ступни
    line(x - 20 * s, y + 210 * s + 100 * f, x - 40 * s, y + 210 * s + 100 * f)
    line(x + 20 * s, y + 210 * s + 100 * f, x + 40 * s, y + 210 * s + 100 * f)


def nechelovek_right(x, y, s, f):
    # Тело
    telo = [(x, y), (x - 65 * s, y + 210 * s), (x + 65 * s, y + 210 * s)]
    penColor(250, 110, 180)
    brushColor(250, 110, 180)
    polygon(telo)
    # Голова
    penColor(255, 240, 200)
    brushColor(255, 240, 200)
    circle(x, y, 34 * s)
    # Левая рука
    penColor(0, 0, 0)
    line(x - 15 * s, y + 44 * s, x - 50 * s, y + 75 * s)
    line(x - 50 * s, y + 75 * s, x - 85 * s, y + 44 * s)
    # Правая рука
    penColor(0, 0, 0)
    line(x + 15 * s, y + 44 * s, x + 100 * s, y + 130 * s)
    # Ноги
    penColor(0, 0, 0)
    line(x - 20 * s, y + 210 * s, x - 20 * s, y + 210 * s + 100 * f)
    line(x + 20 * s, y + 210 * s, x + 20 * s, y + 210 * s + 100 * f)
    # Ступни
    line(x - 20 * s, y + 210 * s + 100 * f, x - 40 * s, y + 210 * s + 100 * f)
    line(x + 20 * s, y + 210 * s + 100 * f, x + 40 * s, y + 210 * s + 100 * f)


def buket(x0, y0, s, f):
    #Треугольник
    penColor("yellow")
    brushColor("yellow")
    x_0 = x0
    y_0 = y0
    x_1 = x0 + (-60 * s) * m.cos(f) - (-100 * s) * m.sin(f)
    y_1 = y0 + (-100 * s) * m.cos(f) + (-60 * s) * m.sin(f)
    x_2 = x0 + (60 * s) * m.cos(f) - (-100 * s) * m.sin(f)
    y_2 = y0 + (-100 * s) * m.cos(f) + (60 * s) * m.sin(f)
    p = [(x_0, y_0), (x_1, y_1), (x_2, y_2)]
    polygon(p)
    #Овальчики
    penColor("red")
    brushColor("red")
    ovalchik(x0 + (30 * s) * m.cos(f) - (-100 * s) * m.sin(f), y0 + (-100 * s) * m.cos(f) + (30 * s) * m.sin(f), 30 * s,
             25 * s, m.pi / 4)
    penColor("white")
    brushColor("white")
    ovalchik(x0 + (-30 * s) * m.cos(f) - (-100 * s) * m.sin(f), y0 + (-100 * s) * m.cos(f) + (-30 * s) * m.sin(f),
             30 * s, 25 * s, m.pi / 4)
    penColor("black")
    brushColor("black")
    ovalchik(x0 - (-120 * s) * m.sin(f), y0 + (-120 * s) * m.cos(f) , 30 * s, 25 * s, m.pi / 4)

def sharik(x0, y0, s, f):
    # Треугольник
    penColor("red")
    brushColor("red")
    x_0 = x0
    y_0 = y0
    x_1 = x0 + (-60 * s) * m.cos(f) - (-100 * s) * m.sin(f)
    y_1 = y0 + (-100 * s) * m.cos(f) + (-60 * s) * m.sin(f)
    x_2 = x0 + (60 * s) * m.cos(f) - (-100 * s) * m.sin(f)
    y_2 = y0 + (-100 * s) * m.cos(f) + (60 * s) * m.sin(f)
    p = [(x_0, y_0), (x_1, y_1), (x_2, y_2)]
    polygon(p)
    # Овальчики
    penColor("red")
    brushColor("red")
    ovalchik(x0 + (30 * s) * m.cos(f) - (-100 * s) * m.sin(f), y0 + (-100 * s) * m.cos(f) + (30 * s) * m.sin(f), 35 * s,
             30 * s, m.pi / 4)
    penColor("red")
    brushColor("red")
    ovalchik(x0 + (-30 * s) * m.cos(f) - (-100 * s) * m.sin(f), y0 + (-100 * s) * m.cos(f) + (-30 * s) * m.sin(f),
             35 * s, 30 * s, m.pi / 4)

penColor(20, 210, 110)
brushColor(20, 210, 110)
rectangle(0, 360, 1400, 1000)

penColor(170, 240, 230)
brushColor(170, 240, 230)
rectangle(0, 0, 1400, 360)

chelovek(200, 200, 1, 1)
nechelovek(420, 200, 1, 1)
nechelovek_left(620, 200, 1, 1)
nechelovek_right(790, 200, 1, 1)
nechelovek(990, 200, 1, 1)
chelovek(1210, 200, 1, 1)

line(705, 245, 705, 110)
buket(705, 110, 1, m.pi/3)
sharik(77, 330, 0.86 , -m.pi/11)
buket(1334, 330, 1, 0)
run()
