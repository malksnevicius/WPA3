import turtle
import random


def stvorec(t : turtle.Turtle):
    """ Vykresli stvorec od stredu
    :param t:objekt korytnacka
    :return: None
    """
    for _ in range(4):
        t.forward(100)
        t.left(90)

korytnacka1 = turtle.Turtle()
korytnacka1.shape("turtle")
korytnacka1.color("red")
stvorec(korytnacka1)

korytnacka2 = turtle.Turtle()
korytnacka2.shape("turtle")
korytnacka2.color("blue")
stvorec(korytnacka2)

turtle.mainloop()