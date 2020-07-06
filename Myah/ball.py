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




root = tkinter.Tk () # виджет главного окна, root - название окна

button1 = tkinter.Button(root, text="Button1", command=button1_command) # создание кнопки, вызов обработчика событий
# такой вызов сортировщика не относится к мышке, поэтому event(num) здесь не нужен, а для второй кнопки нужен.
# Вводим функцию
button1.bind("<Button>", print_hello) #если к одной кнопке назначить
# и обработчик Print_hellow и button1_command(), то кнопка будет
# работать по нажатию мыши, если не отпуская кнопку мыши перевести ее с кнопки,
# то срабатывания не будет. Если отпустить мышь на кнопке, сработает команда
# button1_command

button1.pack() #  упаковщик окна, размещает кнопку в окне

button2 = tkinter.Button(root, text="Button2")
button2.bind("<Button>", print_hello) # создали вторую кнопку, #  вызов обработчика событий, к которому назначим действие
# функцию напечатать текст hello, <Button> - привязка к кнопке мыши
button2.pack()
# пока не расписано me обе кнопки срабатывают одинаково


root.mainloop() #обработка работы с окном и закрытие его
