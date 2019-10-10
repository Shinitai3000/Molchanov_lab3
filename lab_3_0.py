from graph import *

penColor(0, 0, 0)
penSize(1)

brushColor("yellow")
circle(250, 200, 150)

brushColor("red")
circle(320, 180, 20)
brushColor("red")
circle(190, 190, 30)

brushColor("black")
circle(320, 180, 10)
brushColor("black")
circle(190, 190, 20)
rectangle(140, 260, 360, 320)


brushColor("black")
p = [(120, 110), (250, 190), (255, 180), (120, 80), (120,110)]
polygon(p)
c = [(380, 130), (360, 90), (260, 150), (280,160),(380, 130)]
polygon(c)

run()
