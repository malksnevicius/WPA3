import turtle
import random


def stvorec(t : turtle.Turtle, posx: int=0, posy: int=0):
    """ Vykresli stvorec od stredu
    :param t:objekt korytnacka
    :return: None
    """
    t.setpos(posx, posy)
    for _ in range(4):
        t.forward(100)
        t.left(90)

t = turtle.Turtle()
t.shape("turtle")
t.color("red")

for _ in range(5):
    px = random.randint(-500, 500)
    py = random.randint(-500, 500)
    stvorec(t, px, py)

turtle.mainloop()
