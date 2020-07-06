import tkinter # можно писать from tkinter import *

def button1_command():
    print('Кнопка 1 default command)')


def print_hello(event):
    #print(event.char)
    #print(event.keycode)
    print(event.num) # номер кнопки мышки (1-левая, 3-правая, 2 -средняя)
    print(event.x, event.y)
    #print(event.x_root, event.y_root) координаты окна от верхнего левого края экрана
    me = event.widget # что можно сделать с объектом me?
    if me == button1:
        print('Hello!')
    elif me == button2:
        print('Нажата кнопка 2')
    else:
        raise ValueError() # вызвать ошибку


def init_main_window():
    """ Инициализация главного окна, создание виджетов и их упаковка"""
    global root, button1, button2, label, text, ruler
    root = tkinter.Tk ()

    button1 = tkinter.Button(root, text="Button1", command=button1_command)
    button1.bind("<Button>", print_hello)


    button2 = tkinter.Button(root, text="Button2")
    button2.bind("<Button>", print_hello)


    variable = tkinter.IntVar(0)
    label = tkinter.Label(root, textvariable=variable) # привязать метку к переменной
    scale = tkinter.Scale(root, orient=tkinter.HORIZONTAL, length=300,
                          from_=0, to=100, tickinterval=10, resolution=5, variable=variable) #создание ползунка
    text = tkinter.Entry(root, textvariable=variable) #создание текстового поля для ползунка

    for obj in button1, button2, label, scale, text:
        obj.pack()  #упаковка виджетов



init_main_window()

root.mainloop() #обработка работы с окном и закрытие его
