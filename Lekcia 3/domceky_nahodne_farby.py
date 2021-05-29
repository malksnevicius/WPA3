import random
import turtle
import math


def domcek(korytnacka: turtle.Turtle, posx: int=0, posy: int=0) -> None:
    c = math.sqrt(300**2 + 300**2)
    korytnacka.forward(300)
    korytnacka.left(135)
    korytnacka.forward(c)
    korytnacka.right(135)
    korytnacka.forward(300)
    korytnacka.left(135)
    korytnacka.forward(213)
    korytnacka.left(90)
    korytnacka.forward(213)
    korytnacka.left(45)
    korytnacka.forward(300)
    korytnacka.left(135)
    korytnacka.forward(c)
    korytnacka.right(135)
    korytnacka.forward(300)

    t.setpos(posx, posy)


t = turtle.Turtle()
t.color('red')
# neviem nastavit nahodne farby, vraj nieco ako turtle.mode(255)
# a potom po for cykle t.color(randit(0, 255), randit(0, 255), randit(0, 255))

for i in range(5):
     px = random.randint(-500, 500)
     py = random.randint(-500, 500)
     domcek(t, px, py)

turtle.mainloop()