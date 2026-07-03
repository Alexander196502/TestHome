"""
Задание 3
Доработайте проект калькулятора. Добавьте кнопку для умножения трех чисел.
"""
import tkinter as tk
from tkinter import *

# Функция сложения
def addition():
    try:
        # Получаем значения из полей ввода и преобразуем их в числа
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        num3 = float(entry3.get())
        # Результат сложения
        result = num1 + num2 + num3
        # Обновляем текст в label с результатом
        result_label.config(text=f"Сумма: {result:.2f}", bg="lightgreen")
    except ValueError:
        # если введены не цифры
        result_label.config(text="Ошибка: введите числа (можно дробные)", bg="red")

# Функция умножения
def multiplication():
    try:
        # Получаем значения из полей ввода и преобразуем их в числа
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        num3 = float(entry3.get())
        # Результат умножения
        result = num1 * num2 * num3
        # Обновляем текст в label с результатом
        result_label.config(text=f"Произведение: {result:.2f}", bg="lightgreen")
    except ValueError:
        # если введены не цифры
        result_label.config(text="Ошибка: введите числа (можно дробные)", bg="red")

# Функция вычитания (дополнительно)
def subtraction():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        num3 = float(entry3.get())
        result = num1 - num2 - num3
        result_label.config(text=f"Разность: {result:.2f}", bg="lightgreen")
    except ValueError:
        result_label.config(text="Ошибка: введите числа (можно дробные)", bg="red")

# Функция деления (дополнительно)
def division():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        num3 = float(entry3.get())
        if num2 == 0 or num3 == 0:
            result_label.config(text="Ошибка: деление на ноль!", bg="red")
        else:
            result = num1 / num2 / num3
            result_label.config(text=f"Частное: {result:.2f}", bg="lightgreen")
    except ValueError:
        result_label.config(text="Ошибка: введите числа (можно дробные)", bg="red")

# Очистка полей
def clear_fields():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    result_label.config(text="", bg="lightgray")

# Завершение работы
def programmStop():
    root.destroy()

# Создание окна
root = tk.Tk()
root.geometry("500x450")
root.title("Калькулятор")
root.resizable(False, False)

# Создаём рамку (Frame) и размещаем её на всё окно
frame = tk.Frame(root, bg="white", highlightbackground="gray", highlightthickness=5)
frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Текст-инструкция
textwindow = Label(frame, text='Введите три числа и нажмите на кнопку для вычисления:',
                   font=("Arial", 10), bg="white")
textwindow.pack(pady=5)

# Поля ввода с подписями
label1 = Label(frame, text="Число 1:", bg="white")
label1.pack()
entry1 = tk.Entry(frame, width=30, font=("Arial", 10))
entry1.pack(pady=2)

label2 = Label(frame, text="Число 2:", bg="white")
label2.pack()
entry2 = tk.Entry(frame, width=30, font=("Arial", 10))
entry2.pack(pady=2)

label3 = Label(frame, text="Число 3:", bg="white")
label3.pack()
entry3 = tk.Entry(frame, width=30, font=("Arial", 10))
entry3.pack(pady=2)

# Разделительная линия
separator = Label(frame, text="─" * 40, bg="white")
separator.pack(pady=5)

# Кнопки основных операций
button_frame = tk.Frame(frame, bg="white")
button_frame.pack(pady=5)

button1 = tk.Button(button_frame, text="Сложить", bg="lightblue", width=12,
                    font=("Arial", 9))
button1.grid(row=0, column=0, padx=5, pady=2)
button1.config(command=addition)

button2 = tk.Button(button_frame, text="Умножить", bg="lightgreen", width=12,
                    font=("Arial", 9))
button2.grid(row=0, column=1, padx=5, pady=2)
button2.config(command=multiplication)

button3 = tk.Button(button_frame, text="Вычесть", bg="#FFB6C1", width=12,
                    font=("Arial", 9))
button3.grid(row=1, column=0, padx=5, pady=2)
button3.config(command=subtraction)

button4 = tk.Button(button_frame, text="Разделить", bg="#FFD700", width=12,
                    font=("Arial", 9))
button4.grid(row=1, column=1, padx=5, pady=2)
button4.config(command=division)

# Label для отображения результата
text_Rez = Label(frame, text="Результат:", font=("Arial", 12, "bold"),
                 bg="lightgray")
text_Rez.pack(pady=5)
result_label = Label(frame, font=("Arial", 12), bg="lightgray", width=30,
                     relief="sunken")
result_label.pack(pady=5)

# Разделительная линия
separator2 = Label(frame, text="─" * 40, bg="white")
separator2.pack(pady=5)

# Кнопки управления
control_frame = tk.Frame(frame, bg="white")
control_frame.pack(pady=5)

buttonClear = tk.Button(control_frame, text="Очистить поля", bg="lightyellow",
                       width=15, font=("Arial", 9))
buttonClear.grid(row=0, column=0, padx=5, pady=2)
buttonClear.config(command=clear_fields)

buttonStop = tk.Button(control_frame, text="Завершить", bg="lightcoral",
                      width=15, font=("Arial", 9))
buttonStop.grid(row=0, column=1, padx=5, pady=2)
buttonStop.config(command=programmStop)

root.mainloop()