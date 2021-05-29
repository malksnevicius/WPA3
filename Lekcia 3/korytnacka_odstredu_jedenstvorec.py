def stvorec(t):
    """ Vykresli stvorec od stredu
    :param t:objekt korytnacka
    :return: None
    """
    for _ in range(4):
        t.forward(100)
        t.left(90)


t = turtle.Turtle()
t.shape("turtle")
t.color("red")
stvorec(t)

turtle.mainloop()