"""
Ввод цвета, угадывания случайного цвета компьютера
"""
import tkinter as tk
from tkinter import *
import random

# Глобальная переменная для хранения случайного цвета компьютера
comp_color = None

def generate_comp_color():
    """Генерирует случайный цвет (1 - красный, 2 - желтый, 3 - зеленый)"""
    return random.choice([1, 2, 3])

def Color_comparison_Red():
    global comp_color
    comp_color = generate_comp_color()
    if comp_color == 1:
        result_label.config(text="ЦВЕТ УГАДАН!", fg="green")
    else:
        result_label.config(text=f"НЕВЕРНО! Был загадан цвет: {get_color_name(comp_color)}", fg="red")

def Color_comparison_Yellow():
    global comp_color
    comp_color = generate_comp_color()
    if comp_color == 2:
        result_label.config(text="ЦВЕТ УГАДАН!", fg="green")
    else:
        result_label.config(text=f"НЕВЕРНО! Был загадан цвет: {get_color_name(comp_color)}", fg="red")

def Color_comparison_Green():
    global comp_color
    comp_color = generate_comp_color()
    if comp_color == 3:
        result_label.config(text="ЦВЕТ УГАДАН!", fg="green")
    else:
        result_label.config(text=f"НЕВЕРНО! Был загадан цвет: {get_color_name(comp_color)}", fg="red")

def get_color_name(color_num):
    """Возвращает название цвета по номеру"""
    colors = {1: "Красный", 2: "Желтый", 3: "Зеленый"}
    return colors.get(color_num, "Неизвестный")

# завершение работы
def programmStop():
    root.destroy()

# создание окна
root = tk.Tk()
root.geometry("500x400")
root.title("Светофор")
root.resizable(False, False)

# Создаём рамку (Frame) и размещаем её на всё окно
frame = tk.Frame(root, bg="white", highlightbackground="gray", highlightthickness=5)
frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Текст-инструкция
textwindow = Label(frame, text='Выберите цвет, чтобы угадать:', font=("Arial", 14), bg="white")
textwindow.pack(pady=10)

# Разделительная линия
separator = Label(frame, text="─" * 40, bg="white")
separator.pack(pady=5)

# Кнопки с цветами
button1 = tk.Button(frame, text="Красный", bg="red", fg="white", font=("Arial", 12), width=20)
button1.pack(pady=5)
button1.config(command=Color_comparison_Red)

button2 = tk.Button(frame, text="Желтый", bg="yellow", font=("Arial", 12), width=20)
button2.pack(pady=5)
button2.config(command=Color_comparison_Yellow)

button3 = tk.Button(frame, text="Зеленый", bg="green", fg="white", font=("Arial", 12), width=20)
button3.pack(pady=5)
button3.config(command=Color_comparison_Green)

# Разделительная линия
separator = Label(frame, text="─" * 40, bg="white")
separator.pack(pady=5)

# Label для отображения результата
result_label = Label(frame, text="Результат: ", font=("Arial", 14), bg="white", width=40, relief="sunken")
result_label.pack(pady=10)

# Разделительная линия
separator = Label(frame, text="─" * 40, bg="white")
separator.pack(pady=5)

# завершение работы
buttonStop = tk.Button(frame, text="Завершение программы", bg="lightyellow", font=("Arial", 10))
buttonStop.pack(pady=5)
buttonStop.config(command=programmStop)

root.mainloop()