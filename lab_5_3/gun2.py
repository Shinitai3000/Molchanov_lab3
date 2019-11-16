from random import randrange as rnd, choice
import tkinter as tk
import math
import time

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canvas = tk.Canvas(root, bg='white')
canvas.pack(fill=tk.BOTH, expand=1)
a = 450
p = 0.0
screen2 = canvas.create_text(30, 30, text=p, font='28')

menu = 1
Spisok_spiskov = []
name = ''


def dey(r):
    return r[1]


def spasisohrani():
    global Spisok_spiskov
    top = open('spisok.txt', 'r')
    imya = []
    score = []
    d = 1
    for i in top:
        if d:
            imya.append(i)
        else:
            score.append(i)
        d = 1 - d
    for i in range(0, len(imya), 1):
        Spisok_spiskov.append([imya[i][:-1], float(score[i][:-1])])
    Spisok_spiskov.sort(key=dey, reverse=1)


def sohranispasi():
    global Spisok_spiskov
    top = open('spisok.txt', 'w')
    for i in Spisok_spiskov:
        top.write(i[0] + '\n')
        top.write(str(i[1]) + '\n')


class Ball:
    def __init__(self):
        global a

        self.x = 40
        self.y = a
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.gy = -2
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canvas.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = 80

    def set_coords(self):
        canvas.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move(self):

        friction_x = 1
        friction_y = 0.5
        self.vy += self.gy
        self.x += self.vx
        self.y -= self.vy

        if self.x + self.r >= 800:
            self.x -= (self.x + self.r) - 800
            self.vx = -self.vx
        elif self.x - self.r <= 0:
            self.x = self.r
            self.vx = -self.vx

        if self.y + self.r >= 500:
            self.y -= (self.y + self.r) - 500
            self.vy = -self.vy * friction_y

            # Трение
            if self.vx > 0:
                self.vx -= friction_x * abs(self.vy)
                if self.vx < 0:
                    self.vx = 0
            elif self.vx < 0:
                self.vx += friction_x * abs(self.vy)
                if self.vx > 0:
                    self.vx = 0

        self.set_coords()

    def hittest(self, obj):
        if math.hypot(self.x - obj.x, self.y - obj.y) <= (self.r + obj.r):
            canvas.delete(self.id)
            return True
        else:
            return False


class Gun:
    def __init__(self):
        global s
        self.live = s
        self.x = 20
        self.y = 450
        self.vy = 2
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canvas.create_line(self.x, self.y, self.x + 30,
                                     self.y, width=7)

    def destroy1(self):
        canvas.coords(
            self.id,
            -100,
            -100,
            -100,
            -100
        )

    def set_coords(self):
        canvas.coords(
            self.id,

            self.x,
            self.y,
            self.x + max(self.f2_power, 20) * math.cos(self.an),
            self.y + max(self.f2_power, 20) * math.sin(self.an)
        )

    def g_up(self, event):
        global a
        self.y -= self.vy
        if self.y < 100:
            self.y += self.vy
        a = self.y

        self.set_coords()

    def g_down(self, event):
        global a
        self.y += self.vy
        if self.y > 500:
            self.y -= self.vy
        a = self.y

        self.set_coords()

    def move(self):
        global a
        self.y += self.vy
        if self.y > 500:
            self.vy = - self.vy
        if self.y < 100:
            self.vy = - self.vy
        a = self.y

        self.set_coords()

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        global balls, bullet
        bullet += 1
        new_ball = Ball()
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = 3 * self.f2_power * math.cos(self.an)
        new_ball.vy = - 3 * self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):

        if event:
            self.an = math.atan((event.y - self.y) / (event.x - 20))
        if self.f2_on:
            canvas.itemconfig(self.id, fill='orange')
        else:
            canvas.itemconfig(self.id, fill='black')
        canvas.coords(self.id, 20, self.y,
                      20 + max(self.f2_power, 20) * math.cos(self.an),
                      self.y + max(self.f2_power, 20) * math.sin(self.an)
                      )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canvas.itemconfig(self.id, fill='orange')
        else:
            canvas.itemconfig(self.id, fill='black')


class Target:
    def __init__(self):
        self.points = 0
        self.live = 1
        self.x = 0
        self.y = 0
        self.r = 0
        self.vx = 0
        self.vy = 0
        self.color = 'red'
        self.id = canvas.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        # self.id_points = canvas.create_text(30, 30, text=self.points, font='28')
        self.new_target()

    def new_target(self):
        self.vx = rnd(-10, 10)
        self.vy = rnd(-10, 10)
        self.x = rnd(500, 760)
        self.y = rnd(300, 400)
        self.r = rnd(10, 30)
        color = self.color = 'red'
        canvas.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        canvas.itemconfig(self.id, fill=color)

    def hit(self):
        global p
        canvas.coords(self.id, -10, -10, -10, -10)
        p += 1 / s
        canvas.itemconfig(screen2, text=round(p, 2))

    def set_coords(self):
        canvas.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move(self):

        self.y += self.vy
        self.x += self.vx

        if self.x + self.r >= 760:
            self.x -= (self.x + self.r) - 760
            self.vx = -self.vx
        elif self.x - self.r <= 10:
            self.x = 10 + self.r
            self.vx = -self.vx

        if self.y + self.r >= 500:
            self.y -= (self.y + self.r) - 500
            self.vy = -self.vy
        elif self.y + self.r <= 80:
            self.vy = -self.vy
        self.set_coords()


screen1 = canvas.create_text(400, 300, text='', font='28')

bullet = 0
balls = []

n = 1


def change(event=''):
    global menu, n
    menu = 1 - menu
    n = 1
    print(menu, n)


s = 1


def spisok():
    change()
    window = tk.Toplevel(root)
    window.geometry('300x600')
    for i in range(0, len(Spisok_spiskov), 1):
        txt = str(i + 1) + '     ' + Spisok_spiskov[i][0] + ' = ' + str(Spisok_spiskov[i][1]) + ' Points'
        msg = tk.Message(window, text=txt, width=1000)
        msg.pack()
        #window.create_text(50, 200 + 30 * i, text=txt, justify=tk.CENTER, font="Verdana 25", anchor=tk.W)


def new_game(event=''):
    global g, screen1, screen2, balls, bullet, menu, n, but1, e1, k, s, text1, text2, text3, but2, e2, name
    if menu == 1:
        if n == 1:
            but1 = tk.Button(canvas, text="Start", width=16, height=1, command=change, font="Verdana 25")
            but1.grid()
            text1 = canvas.create_text(470, 78, text="Введите число целей", justify=tk.CENTER, font="Verdana 12")

            e1 = tk.Entry(canvas, width=56)
            e1.grid()

            l1 = tk.Label(text="Как же я люблю делать информатику в др", fg="#eee", bg="#333")
            l1.pack()
            text2 = canvas.create_text(500, 90, text="Введите имя", justify=tk.CENTER,
                                       font="Verdana 12")
            text3 = canvas.create_text(400, 130,
                                       text="Пауза на правую кнопку мыши, пушка вверх - на Таб, вниз на - Левый Альт",
                                       justify=tk.CENTER,
                                       font="Verdana 12")
            e2 = tk.Entry(canvas, width=50)
            e2.grid()
            but3 = tk.Button(canvas, text="Leadertop", width=16, height=1, command=spisok, font="Verdana 25")
            but3.grid()
            n = 0
    else:
        but1.destroy()
        canvas.itemconfig(text1, text="")
        canvas.itemconfig(text2, text="")
        canvas.itemconfig(text3, text="")
        if s == 1:
            name = e2.get()
            k = int(e1.get())
            screen2 = canvas.create_text(500, 30, text=p, font='28')
            s = k
        e1.destroy()
        e2.destroy()
        g = Gun()
        canvas.bind('<Tab>', g.g_up)
        canvas.bind('<Alt_L>', g.g_down)
        canvas.bind('<Button-3>', change)
        canvas.bind('<Button-1>', g.fire2_start)
        canvas.bind('<ButtonRelease-1>', g.fire2_end)
        canvas.bind('<Motion>', g.targetting)
        z = 0.03
        targets = []
        for i in range(s):
            targets.append(Target())
        while len(targets) != 0:
            if menu != 1:
                canvas.bind('<Motion>', g.targetting)
                canvas.bind('<Button-1>', g.fire2_start)
                canvas.bind('<ButtonRelease-1>', g.fire2_end)
                canvas.bind('<Tab>', g.g_up)
                canvas.bind('<Alt_L>', g.g_down)
                # g.move()
                for t in targets:
                    t.move()
                    if abs(t.x - g.x) < 30 and abs(t.y - g.y) < 30:
                        g.live -= 1
                        print("CATCH")
                        print(str(g.live))
                        if g.live == 0:
                            Spisok_spiskov.append([name, p])
                            sohranispasi()
                            exit()
                for b in balls:
                    b.move()
                    b.live -= 1
                    if b.live <= 0:
                        canvas.delete(b.id)
                        balls.remove(b)
                    for t in targets:
                        if b.hittest(t) and t.live:
                            t.live = 0
                            t.hit()
                            targets.remove(t)
            else:
                canvas.bind('<Button-1>', '')
                canvas.bind('<ButtonRelease-1>', '')
                canvas.bind('<Motion>', '')
                canvas.bind('<Tab>', '')
                canvas.bind('<Alt_L>', '')
            canvas.update()
            time.sleep(z)
            g.targetting()
            g.power_up()
            if len(targets) == 0:
                g.destroy1()
                canvas.delete(g.id)
                for b in balls:
                    canvas.delete(b.id)
                    balls.remove(b)
                canvas.bind('<Button-1>', '')
                canvas.bind('<ButtonRelease-1>', '')
                if 10 < bullet < 20:
                    canvas.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
                elif bullet % 10 == 1:
                    canvas.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрел')
                elif bullet % 10 == 2 or bullet % 10 == 3 or bullet % 10 == 4:
                    canvas.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрела')
                else:
                    canvas.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
                canvas.update()
                time.sleep(0.35)
                bullet = 0
        canvas.itemconfig(screen1, text='')
        canvas.update()
    root.after(750, new_game)


spasisohrani()
new_game()

tk.mainloop()
