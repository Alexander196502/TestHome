"""
Ввод цвета, угадывания случайного цвета компьютера
"""
import tkinter as tk
from tkinter import *
import random

def Color_comparison_Red():
    Comp_color = FComp_color()
    if Comp_color == 1:
        result_label = 'ЦВЕТ УГАДАН'
        return
    else:
        result_label = 'НЕВЕРНО!'
        return

def Color_comparison_Yellow():
    Comp_color = FComp_color()
    if Comp_color == 2:
        result_label = 'ЦВЕТ УГАДАН'
        return
    else:
        result_label = 'НЕВЕРНО!'
        return

def Color_comparison_Green():
    if Comp_color == 3:
        result_label = 'ЦВЕТ УГАДАН'
        return
    else:
        result_label = 'НЕВЕРНО!'
        return

def FComp_color(rez_color):
    rez_color = random.choice([1, 2, 3])
    return(rez_color)




# завершение работы
def programmStop():
    root.destroy()




# создание окна
root = tk.Tk()
root.geometry("500x550")
root.title("Свтофор")
root.resizable(False, False)

# Создаём рамку (Frame) и размещаем её на всё окно
frame = tk.Frame(root, bg="white", highlightbackground="gray", highlightthickness=5)
frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Текст-инструкция
textwindow = Label(frame, text='Выберите цвет, угадать :')
textwindow.pack()

### Поля ввода
### entry1 = tk.Entry(frame, width=30)
### entry1.pack(pady=5)

### entry2 = tk.Entry(frame, width=30)
### entry2.pack(pady=5)

### entry3 = tk.Entry(frame, width=30)
### entry3.pack(pady=5)
###
# Разделительная линия
separator = Label(frame, text="─" * 40, bg="white")
separator.pack(pady=5)

result_label = ''

# Кнопки
button1 = tk.Button(frame, text="Red", bg="Lightgray")
button1.pack(pady=5)
button1.config(command=Color_comparison_Red)

button2 = tk.Button(frame, text="Yellow", bg="Lightgray")
button2.pack(pady=5)
button2.config(command=Color_comparison_Yellow)

button3 = tk.Button(frame, text="Green", bg="lightgreen")
button3.pack(pady=5)
button3.config(command=Color_comparison_Green)

###button4 = tk.Button(frame, text="Деление(1/2/3)", bg="lightgreen")
###button4.pack(pady=5)
###button4.config(command=divide)

# Label для отображения результата
text_Rez = Label(frame, text="Результат: ", font=("Arial", 12), bg="white", width=12, relief="sunken")
text_Rez.pack(pady=10)
result_label = Label(frame, font=("Arial", 12), bg="white", width=30, relief="sunken")
result_label.pack(pady=10)


# Разделительная линия
separator = Label(frame, text="─" * 40, bg="white")
separator.pack(pady=5)

# очистка полей
# buttonClear = tk.Button(frame, text="Очистить поля", bg="lightyellow")
# buttonClear.pack(pady=5)
# buttonClear.config(command=clear_fields)

# заврешение работы
buttonStop = tk.Button(frame, text="Завершение программы", bg="lightyellow")
buttonStop.pack(pady=5)
buttonStop.config(command=programmStop)

root.mainloop()