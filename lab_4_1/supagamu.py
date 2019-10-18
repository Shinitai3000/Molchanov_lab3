from tkinter import *
import random

ch = 0


# переключатель(кнопка)
def change():
    global ch
    ch = 1 - ch


# сортировка
def dey(a):
    return a[1]


Spisok_spiskov = []


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
    Spisok_spiskov.sort(key=dey, reverse=TRUE)


# Записывает обновлённую инфу из Списка списков в файл
def sohranispasi():
    global Spisok_spiskov
    top = open('spisok.txt', 'w')
    for i in Spisok_spiskov:
        top.write(i[0] + '\n')
        top.write(str(i[1]) + '\n')


root = Tk()
root.geometry("800x700")
# Холст, на ктором шарики
c = Canvas(root, width=800, height=700, bg='white')
c.pack()

width = 800
heigth = 600
# Холст, на котором кнопки
d = Canvas(root, width=800, height=600, bg='white')
d.pack()

# кнопка вывода списка
b = Button(c, text="Spisok chelovekov", command=change, font="Verdana 25")
b.pack()

# ввод имени
e = Entry(c, width=56)
e.pack()


def randCircle():
    x = random.randint(100, 700)
    y = random.randint(100, 500)
    r = random.randint(10, 40)
    color = randColor()
    vx = randSign() * random.randint(1, 8)
    vy = randSign() * random.randint(1, 8)
    return [0, [x, y, r, color, vx, vy]]


def randKvadrat():
    x = random.randint(100, 700)
    y = random.randint(100, 500)
    r = random.randint(10, 40)
    color = randColor()
    vx = randSign() * random.randint(8, 10)
    vy = randSign() * random.randint(8, 10)
    return [1, [x, y, r, color, vx, vy]]


# рандомный цвет
def randColor():
    r = 255
    g = 255
    b = 255
    while r + g + b > 675:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
    col = "#%02X%02X%02X" % (r, g, b)
    return col


# Круги
def circle(a):
    global width, heigth
    vx = a[4]
    vy = a[5]
    a[0] = a[0] + vx
    a[1] = a[1] + vy
    x = a[0]
    y = a[1]
    r = a[2]
    c = a[3]
    d.create_oval(x - r, y - r, x + r, y + r, fill=c, width=0)
    if x + r > width:
        a[4] = -random.randint(1, 8)
    if x - r < 0:
        a[4] = random.randint(1, 8)
    if y + r > heigth:
        a[5] = -random.randint(1, 8)
    if y - r < 0:
        a[5] = random.randint(1, 8)


# Квадратики
def kvadrat(a):
    global width, heigth
    vx = a[4]
    vy = a[5]
    a[0] = a[0] + vx
    a[1] = a[1] + vy
    x = a[0]
    y = a[1]
    r = a[2]
    c = a[3]
    d.create_rectangle(x + r, y + r, x - r, y - r, fill=c, width=0)
    if x + r > width:
        a[4] = -random.randint(10, 20)
    if x - r < 0:
        a[4] = random.randint(10, 20)
    if y + r > heigth:
        a[5] = -random.randint(10, 20)
    if y - r < 0:
        a[5] = random.randint(10, 20)


# Рисовака
def risovaka():
    global Spisok_spiskov, ch, name, Objects, abc
    d.delete(ALL)
    d.create_text(20, 10, text = "Score" + ' ' + str(n) )
    if ch:  # рисует список игроков
        for i in range(0, len(Spisok_spiskov), 1):
            txt = str(i + 1) + '     ' + Spisok_spiskov[i][0] + ' = ' + str(Spisok_spiskov[i][1]) + ' Points'
            d.create_text(50, 60 + 30 * i, text=txt, justify=CENTER, font="Verdana 25", anchor=W)
    else:
        if len(Objects) < 50:  # условие непоражения
            for i in Objects:
                if i[0] == 0:
                    circle(i[1])
                if i[0] == 1:
                    kvadrat(i[1])
        else:
            if abc:
                Spisok_spiskov.append([e.get(), n])
                sohranispasi()
                abc = 0
    root.after(16, risovaka)


n = 0  # счёт
abc = 1  # сохраняет список один раз


# -1 или +1
def randSign():
    a = random.randint(0, 1)
    a = a * 2
    a = a - 1
    return a


# присваивает имя
def setname(a):
    global name
    name = e.get()


# мышка
def click(event):
    global Objects, n
    tmpx = event.x
    tmpy = event.y
    obj = []
    for i in Objects:
        if i[0] == 0: #ты круг?
            x = i[1][0]
            y = i[1][1]
            r = i[1][2]
            if ((x - tmpx) ** 2 + (y - tmpy) ** 2 <= r ** 2):
                n += 1
                print(n)
                for k in range(0, 3, 1):
                    obj.append(randCircle())
            else:
                obj.append(i)
        if i[0]== 1: # а может квадрат?
            x = i[1][0]
            y = i[1][1]
            r = i[1][2]
            if tmpx <= x + r and tmpx >= x - r and tmpy <= y + r and tmpy >= y - r:
                n += 5
                print(n)
                for k in range(0,2,1):
                    obj.append(randKvadrat())
            else:
                obj.append(i)
    Objects = obj


d.bind('<Button-1>', click)

# Все круги и квадраты записываются сюда
Objects = []
# Стартовый затар
for i in range(0, 5, 1):
    Objects.append(randCircle())
Objects.append(randKvadrat())
name = 0

spasisohrani()
risovaka()

mainloop()
