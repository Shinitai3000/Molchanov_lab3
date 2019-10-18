from tkinter import *
from random import randrange as rnd, choice

root = Tk()
root.geometry('800x600')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

vx = 2
vy = 1

x = 300
y = 390

vx1 = 8
vy1 = 9

x1 = 250
y1 = 180

r1 = 20

r2 = 30

def update():
    global x, y, vx, vy
    x += vx
    y += vy
    if x + 40 > 800 or x < 40 :
        vx *= -1
    if y > 560 or y < 40:
        vy *= -1
    canv.delete('ball')
    canv.create_oval(x - r1, y - r1, x + r1, y +r1, fill='orange', tag='ball')
    root.after(10, update)

def update1():
    global x1, y1, vx1, vy1
    x1 += vx1
    y1 += vy1
    if x + 40 > 800 or x < 40 :
        vx1 *= -1
    if y > 560 or y < 40:
        vy1 *= -1
    canv.delete('ball2')
    canv.create_oval(x - r2, y - r2, x + r2, y + r2, fill='black', tag='ball2')
    update()
    root.after(10, update1)




def click(event):
    global points, x, text
    if (event.y - y)**2 + (event.x - x)**2 <= r1**2:
        points += 1
        x = -1000
        canv.delete(text)
        canv.delete(ball)
        text = canv.create_text(20,20,text=str(points), font = 'Arial 20')
    if (event.y - y)**2 + (event.x - x)**2 <= r2**2:
        points += 1
        x = -1000
        canv.delete(text)
        canv.delete(ball2)
        text = canv.create_text(20,20,text=str(points), font = 'Arial 20')
ball2 = canv.create_oval(-200,0,0,0)
ball = canv.create_oval(-100,0,0,0)
text = canv.create_text(20,20,text=0, font = 'Arial 20')
points = 0
update()

canv.bind('<Button-1>', click)

mainloop()
