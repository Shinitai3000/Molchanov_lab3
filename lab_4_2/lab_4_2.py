import tkinter as tk
from random import randrange as rnd, choice
import math

n = 0
root = tk.Tk()
root.geometry('800x600')

canv = tk.Canvas(root, bg="white")
canv.pack(fill=tk.BOTH, expand=1)

colors = ['red', 'orange', 'green', 'blue']
skorost = [1, 2 , 3 , -1, -2, -3 ]







class Ball:

    def __init__(self, name):
        self.name = name
        self.x = rnd(100, 700)
        self.y = rnd(100, 420)
        self.vx = choice(skorost)
        self.vy = choice(skorost)
        self.r = rnd(30, 50)
        self.id = None
        self.color = choice(colors)


    def draw(self):
        self.id = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r,
                                   self.y + self.r, fill=self.color, width=0)

    def update(self):
        canv.coords(self.id, self.x - self.r, self.y - self.r,
                    self.x + self.r, self.y + self.r)
        canv.update()

    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.x + self.r >= 800 or self.x - self.r <= 0:
            self.vx = -self.vx
        if self.y + self.r >= 460 or self.y - self.r <= 0:
            self.vy = -self.vy
        self.update()
        root.after(1, self.move)

class Square:

    def __init__(self, name):
        self.name = name
        self.x = rnd(100, 700)
        self.y = rnd(100, 420)
        self.vx = choice(skorost)
        self.vy = choice(skorost)
        self.r = rnd(30, 50)
        self.id = None
        self.color = choice(colors)


    def draw(self):
        self.id = canv.create_rectangle(self.x + self.r, self.y + self.r, self.x - self.r,
                                   self.y - self.r, fill=self.color, width=0)

    def update(self):
        canv.coords(self.id, self.x + self.r, self.y + self.r,
                    self.x - self.r, self.y - self.r)
        canv.update()

    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.x + self.r >= 800 or self.x - self.r <= 0:
            self.vx = -self.vx
        if self.y + self.r >= 460 or self.y - self.r <= 0:
            self.vy = -self.vy
        self.update()
        root.after(1, self.move)

Spisok_spiskov = []

name = 0

# присваивает имя
def setname(a):
    global name
    name = e.get()

# сортировка
def dey(a):
    return a[1]

# Добавляет инфу из файла в Список списков
def spasisohrani():
    global Spisok_spiskov
    top = open('spisok.txt', 'r')
    imya = []
    score = []
    k = 1
    for i in top:
        if k:
            imya.append(i)
        else:
            score.append(i)
        k = 1 - k
    for i in range(0, len(imya), 1):
        Spisok_spiskov.append([imya[i][:-1], int(score[i][:-1])])
    Spisok_spiskov.sort(key=dey, reverse=1)

# Записывает обновлённую инфу из Списка списков в файл
def sohranispasi():
    global Spisok_spiskov
    top = open('spisok.txt', 'w')
    for i in Spisok_spiskov:
        top.write(i[0] + '\n')
        top.write(str(i[1]) + '\n')

# Холст, на котором ввод имени
b = tk.Canvas(root, width=800, height=0, bg='white')
b.pack()

t = tk.Canvas(root, width=800, height=50, bg='white')
t.pack()

def poka():
    sohranispasi()
    exit()

bu = tk.Button(b, text="Save",width=16,height=1, command=poka, font="Verdana 25")
bu.pack()

def score():
    global n
    t.delete(tk.ALL)
    t.create_text(400, 30, justify = tk.CENTER, font="Verdana 25", text= str(n))
    root.after(1, score)



# ввод имени
e = tk.Entry(b, width=56)
e.pack()




balls = []
squares = []

for i in range(1, 6):
    ball = Ball(name=('ball' + str(i)))
    balls.append(ball)
    square = Square(name=('square' + str(i)))
    squares.append(square)
k1 = 10
k2 = 11
for ball in balls:
    ball.draw()
    ball.move()
    print("ball name = ", ball.name)
    print("ball id = ", ball.id)

for square in squares:
    square.draw()
    square.move()
    print("square name = ", square.name)
    print("square id = ", square.id)

def hit(event):
    global k2, k1, n
    for ball in balls:
        if math.hypot(event.x - ball.x, event.y - ball.y) <= ball.r:
            print("hit")
            n += 1
            canv.delete(ball.id)
            k1 = k1 + 10
            for i in range(2):
                ball = Ball(name=('square' + str(k1)))
                balls.append(ball)
                ball.draw()
                ball.move()
    for square in squares:
        if  event.x <= square.x + square.r and event.x >= square.x - square.r and event.y <= square.y + square.r and event.y >= square.y - square.r:
            print("hit")
            n += 2
            canv.delete(square.id)
            k2 = k2 + 10
            for i in range(2):
                square = Square(name=('square' + str(k2)))
                squares.append(square)
                square.draw()
                square.move()
    print(n)


canv.bind('<Button-1>', hit)

def proverka():
    if len(balls) + len(squares) >  n + 11 or len(balls) + len(squares)> 20:
        Spisok_spiskov.append([e.get(), n])
        sohranispasi()
        exit()
    root.after(100, proverka)

proverka()
score()
spasisohrani()
tk.mainloop()