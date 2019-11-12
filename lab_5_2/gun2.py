
from random import randrange as rnd, choice
import tkinter as tk
import math
import time



root = tk.Tk()
root.geometry('800x600')
canvas = tk.Canvas(root, bg='white')
canvas.pack(fill=tk.BOTH, expand=1)

a = 450
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
        self.x = 20
        self.y = 450
        self.vy = 2
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canvas.create_line(self.x, self.y, self.x + 30,
                                     self.y , width=7)

    def set_coords(self):
        canvas.coords(
            self.id,

            self.x,
            self.y,
            self.x + max(self.f2_power, 20) * math.cos(self.an),
            self.y + max(self.f2_power, 20) * math.sin(self.an)
        )

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
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
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
        self.color = 'red'
        self.id = canvas.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.id_points = canvas.create_text(30, 30, text=self.points, font='28')
        self.new_target()

    def new_target(self):

        self.x = rnd(600, 780)
        self.y = rnd(300, 400)
        self.r = rnd(2, 50)
        x = self.x
        y = self.y
        r = self.r
        color = self.color = 'red'
        canvas.coords(self.id, x - r, y - r, x + r, y + r)
        canvas.itemconfig(self.id, fill=color)

    def hit(self, points=1):

        canvas.coords(self.id, -10, -10, -10, -10)
        self.points += points
        canvas.itemconfig(self.id_points, text=self.points)


t1 = Target()
screen1 = canvas.create_text(400, 300, text='', font='28')
g1 = Gun()
bullet = 0
balls = []


def new_game(event=''):
    global g1, t1, screen1, balls, bullet
    t1.new_target()
    canvas.bind('<Button-1>', g1.fire2_start)
    canvas.bind('<ButtonRelease-1>', g1.fire2_end)
    canvas.bind('<Motion>', g1.targetting)
    z = 0.03
    t1.live = 1
    while t1.live:
        for b in balls:
            b.move()
            b.live -= 1
            if b.live <= 0:
                canvas.delete(b.id)
                balls.remove(b)
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
                canvas.bind('<Button-1>', '')
                canvas.bind('<ButtonRelease-1>', '')
                if bullet % 10 == 1:
                    canvas.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрел')
                elif bullet % 10 == 2 or bullet % 10 == 3 or bullet % 10 == 4:
                    canvas.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрела')
                else:
                    canvas.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
                canvas.update()
                time.sleep(0.25)
                bullet = 0
        canvas.update()
        time.sleep(z)
        g1.targetting()
        g1.power_up()
        g1.move()
    canvas.itemconfig(screen1, text='')
    canvas.update()
    root.after(750, new_game)



new_game()
tk.mainloop()
