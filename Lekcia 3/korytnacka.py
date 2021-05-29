import turtle
import random


def stvorec(t: turtle.Turtle, posx: int = 0, posy: int = 0 ) -> None:
    """ Vykresli stvorec na suradniciach posx, posy
    :param posx: suradnica x
    :param posy: suradnica y
    :param t: objekt s korytnackou
    :return: None
    """
    t.penup()
    t.setpos(posx, posy)
    t.pendown()
    for _ in range(4):
        t.forward(100)
        t.left(90)


korytnacka = turtle.Turtle()
korytnacka.shape("turtle")
korytnacka.color("RED")
for _ in range(5):
    px = random.randint(-500, 500)
    py = random.randint(-500, 500)
    stvorec(korytnacka, px, py)

turtle.mainloop()

