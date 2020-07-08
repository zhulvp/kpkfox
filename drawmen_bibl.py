from turtle import Turtle
default_scale = 10

def init_drawman():
    global t, x_current, y_current, drawman_scale
    t = Turtle()
    t.penup()
    x_current = 0
    y_current = 0
    t.goto(x_current, y_current)
    drawman_scale(default_scale)

def drawman_scale(scale):
    global drawman_scale1
    drawman_scale1 = scale

def pen_down():
    """ делегирует черепахе t
    выполнение команды опустить перо"""
    t.pendown()


def pen_up():
    t.penup()

def on_vector(dx, dy):
    to_point(x_current + dx, y_current + dy)


def to_point(x, y):
    global x_current, y_current
    x_current = x
    y_current = y
    t.goto(drawman_scale1*x_current, drawman_scale1*y_current)



init_drawman()




