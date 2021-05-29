import turtle
import math


def domcek(korytnacka):
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

t = turtle.Turtle()
t.color()
domcek(t)
turtle.mainloop()