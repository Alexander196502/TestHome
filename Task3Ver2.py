"""
Задание 3
Доработайте проект калькулятора. Добавьте кнопку для умножения трех чисел.
"""
import tkinter as tk
from tkinter import *


#функция сложения
def addition():
    try:
        # Получаем значения из полей ввода и преобразуем их в числа, в том числе дробные
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        num3 = float(entry3.get())
        # Результат сложения
        result = num1 + num2 + num3
        # Обновляем текст в label с результатом, 2зн после запятой
        result_label.config(text=f"Сумма: {result:.2f}", bg="white")
    except ValueError:
        # если введены не цифры
        result_label.config(text="Ошибка: введите числа (можно дробные)", bg="red")


#функция умножения
def multiplication():
    try:
        # Получаем значения из полей ввода и преобразуем их в числа
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        num3 = float(entry3.get())
        # Результат умножения
        result = num1 * num2 * num3
        # Обновляем текст в label с результатом
        result_label.config(text=f"Произведение: {result:.2f}", bg="white")
    except ValueError:
        # если введены не цифры
        result_label.config(text="Ошибка: введите числа (можно дробные)", bg="red")



# очистка полей
def clear_fields():
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry1.delete(0, END)
    result_label.config(text="", bg="white")


# завершение работы
def programmStop():
    root.destroy()




# создание окна
root = tk.Tk()
root.geometry("500x450")
root.title("Калькулятор")
root.resizable(False, False)

# Создаём рамку (Frame) и размещаем её на всё окно
frame = tk.Frame(root, bg="white", highlightbackground="gray", highlightthickness=5)
frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Текст-инструкция
textwindow = Label(frame, text='Введите три числа и нажмите на кнопку для вычисления:')
textwindow.pack()

# Поля ввода
entry1 = tk.Entry(frame, width=30)
entry1.pack(pady=5)

entry2 = tk.Entry(frame, width=30)
entry2.pack(pady=5)

entry3 = tk.Entry(frame, width=30)
entry3.pack(pady=5)

# Разделительная линия
separator = Label(frame, text="─" * 40, bg="white")
separator.pack(pady=5)

# Кнопки
button1 = tk.Button(frame, text="Сложить три числа", bg="lightblue")
button1.pack(pady=5)
button1.config(command=addition)

button2 = tk.Button(frame, text="Умножить три числа", bg="lightgreen")
button2.pack(pady=5)
button2.config(command=multiplication)

# Label для отображения результата
text_Rez = Label(frame, text="Результат: ", font=("Arial", 12), bg="white", width=12, relief="sunken")
text_Rez.pack(pady=10)
result_label = Label(frame, font=("Arial", 12), bg="white", width=30, relief="sunken")
result_label.pack(pady=10)


# Разделительная линия
separator = Label(frame, text="─" * 40, bg="white")
separator.pack(pady=5)

# очистка полей
buttonClear = tk.Button(frame, text="Очистить поля", bg="lightyellow")
buttonClear.pack(pady=5)
buttonClear.config(command=clear_fields)

# заврешение работы
buttonStop = tk.Button(frame, text="Завершение программы", bg="lightyellow")
buttonStop.pack(pady=5)
buttonStop.config(command=programmStop)

root.mainloop()