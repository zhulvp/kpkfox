import tkinter
from random import choice, randint

ball_initial_number = 10 #начальное число шариков в игре
ball_minimal_radius = 15
ball_maximal_radius = 40
ball_available_colors = ['green', 'blue', 'red', 'lightgray', '#FF00FF', '#FFFF00']


def click_ball(event):
    """ Обработчик событий мышки для игрового холста canvas
    :param event: событие с координатами клика,
    удаляет тот шарик, по которому будем кликать мышкой, и засчитывает его в очки игрока"""
    obj = canvas.find_closest(event.x, event.y)
    x1, y1, x2, y2 = canvas.coords(obj)

    if x1 <= event.x <= x2 and y1 <= event.y <= y2:
        canvas.delete(obj)
        create_random_ball()

def move_all_balls(event):
    """передвигает шарики немного"""
    for obj in canvas.find_all():
        dx = randint(-1,1)
        dy = randint(-1,1)
        canvas.move(obj, dx, dy)


def create_random_ball():
    """создает шарик в случайном месте игрового холста canvas,
    при этом шарик не выходит за границы холста"""
    R = randint(ball_minimal_radius, ball_maximal_radius)
    x = randint(0, int(canvas['width'])-1-2*R)
    """ширина холста больше на единицу в пикселах, так как начинается считать с 0, 
    поэтому вычитаем единицу"""

    y = randint(0, int(canvas['height'])-1-2*R)
    """задаем случайные координаты х и y, функцией int переводим строковое 
    значение в числовое, чтобы провести вычисления"""
    canvas.create_oval(x, y, x+2*R, y+2*R, width=1, fill=random_color())


def random_color():
    """:return: возвращает случайный цвет из некоторого набора цветов"""
    return choice(ball_available_colors)

def init_ball_catch_game():
    """инициализация игрового пространства
    Создаем необходимое для игры количество шариков,
    по которым нужно кликать """
    for i in range (ball_initial_number):
        create_random_ball()


def init_main_window():
    """инициализация главного виджета"""
    global root, canvas

    root = tkinter.Tk()
    """создание главного виджете - окна игры"""
    canvas = tkinter.Canvas(root, background='white', width=400, height=400)
    """создание холста"""
    canvas.bind("<Button>", click_ball)
    """привязываем к мышке обработчик события """
    canvas.bind("<Motion>", move_all_balls)
    """привязываем функцию перемещения шарика к мышке
    и к игровому холсту"""
    canvas.pack()
    """упаковываем виджет холст в главное окно"""


init_main_window()
init_ball_catch_game()
root.mainloop()
print("Приходите поиграть еще")



