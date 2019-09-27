from graph import*
import math as m
ass = []



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


def oval(x, y, A, B):
    n=60
    points_oval=[]
    for i in range(n):
        points_oval.append((x+A*m.cos(2*m.pi*i/n), y+B*m.sin(2*m.pi*i/n)))
    polygon(points_oval)

def coord(event):
    ass.append((event.x, event.y))
    print(ass)
onMouseDown(coord)





brushColor(102, 102, 102)
polygon([(500, 0),(500, 250),(0, 250),(0, 0)])

penColor(231,231,231)
brushColor(231,231,231)
circle(436, 60, 45)

penColor("Black")
brushColor(0, 0, 0)
polygon([(500, 250), (500, 600), (0, 600), (0, 250)])

penColor(19, 19, 19)
brushColor("black")
polygon([(227, 118), (246, 148),(0,148),(19,118)])

penColor(76, 76, 76)
brushColor(76, 76, 76)
oval(498, 113, 230, 23)

brushColor(19, 19, 19)
oval(385, 164, 180, 23)

penColor(30, 30, 30)
brushColor(30, 30, 30)
polygon([(154,118),(164,118),(164,80),(154,80)])

brushColor(30, 30, 30)
polygon([(33, 133), (42, 133),(42,60),(33,60)])

penColor(48, 48, 48)
brushColor(48, 48, 48)
oval(185, 70, 180, 30)

penColor(76, 76 ,76)
brushColor(76, 76, 76)
oval(343, 53, 156, 25)

penColor(30,30,30)
brushColor(30,30,30)
polygon([(56,136), (76, 136),(76,30),(56,30)])


polygon([(206,133),(216,133), (216, 70), (206, 70)])

penColor(43,34,0)
brushColor(43,34,0)
polygon([(22,148),(22,422),(224,422),(224,148)])

penColor(72,62,55)
brushColor(72,62,55)
rectangle(36, 240, 60, 148)
rectangle(80, 240, 104, 148)
rectangle(138, 240, 164, 148)
rectangle(191, 240,213, 148)

penColor(43, 17, 0)
brushColor(43, 17, 0)
rectangle(34, 390, 84, 330)
rectangle(99, 390, 149, 330)

penColor(212,170,0)
brushColor(212, 170,0)
rectangle(164, 390, 214, 330)

penColor(26, 26, 26)
brushColor(26, 26, 26)
rectangle(0, 250, 246, 280)
rectangle(10, 220, 16, 250)
rectangle(236, 250, 230, 220)
for i in range(5):
    rectangle(34 + 40*i, 220, 44 + 40*i, 250 )
rectangle(16, 220, 230, 210)

#The Ghost
penColor(180,180,181)
p = [(365, 426), (363, 426), (357, 434), (356, 440), (356, 443), (353, 452), (349, 461), (345, 469), (339, 481), (337, 482), (333, 490), (328, 500), (324, 509), (320, 515), (312, 521), (306, 529), (303, 540), (319, 534), (325, 532), (334, 529), (344, 528), (350, 533), (355, 541), (369, 543), (378, 539), (389, 532), (408, 528), (425, 530), (429, 531), (441, 525), (446, 519), (445, 514), (445, 503), (448, 496), (454, 496), (462, 494), (468, 485), (464, 477), (461, 468), (453, 461), (444, 456), (431, 438), (428, 433), (422, 423), (416, 414), (400, 408), (393, 407), (383, 407), (370, 418), (363, 425)]
brushColor(180,180,181)
polygon(p)

circle(378, 420,25)
brushColor(136,206,223)

circle(365, 419, 9)
brushColor(136,206,223)

circle(386, 414, 9)
penColor("Black")
brushColor("black")
circle(364, 419, 2)
brushColor("black")
circle(384, 414, 2)


#End of the Ghost

penColor("white")
brushColor("White")
ovalchik(367, 416, 4, 1, - m.pi / 4)
ovalchik(387, 411, 4, 1, - m.pi / 4)
run()