from drawmen_bibl import *
from time import sleep

def f(x):
    return x*x


x = -5.0
to_point(x, f(x))
pen_down()
while x <= 5:
    to_point(x, f(x))
    x +=0.1
pen_up()

sleep(10)
