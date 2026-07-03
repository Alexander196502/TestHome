import tkinter as tk
from tkinter import *


#функция сложения
def addition():
    try:
        # Получаем значения из полей ввода и преобразуем их в числа
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        num3 = int(entry3.get())
        # Результат сложения
        result = num1 + num2 + num3
        # Обновляем текст в label с результатом
        result_label.config(text=f"Сумма: {result}")
    except ValueError:
        # если введены не цифры
        result_label.config(text="Ошибка, введены неверные символы: введите числа!")


#функция умножения
def multiplication():
    try:
        # Получаем значения из полей ввода и преобразуем их в числа
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        num3 = int(entry3.get())
        # Результат умножения
        result = num1 * num2 * num3
        # Обновляем текст в label с результатом
        result_label.config(text=f"Произведение: {result}")
    except ValueError:
        # если введены не цифры
        result_label.config(text="Ошибка: введите числа!")




# создание окна
root = tk.Tk()
root.geometry("500x300")
root.title("Калькулятор")

# Текст-инструкция
textwindow = Label(text='Введите три числа и нажмите на кнопку для вычисления:')
textwindow.pack()

# Поля ввода
entry1 = tk.Entry(root, width=30)
entry1.pack(pady=5)

entry2 = tk.Entry(root, width=30)
entry2.pack(pady=5)

entry3 = tk.Entry(root, width=30)
entry3.pack(pady=5)

# Кнопки
button1 = tk.Button(root, text="Сложить три числа", bg="lightblue")
button1.pack(pady=5)
button1.config(command=addition)

button2 = tk.Button(root, text="Умножить три числа", bg="lightgreen")
button2.pack(pady=5)
button2.config(command=multiplication)

# Label для отображения результата
result_label = Label(root, text="Результат: ", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()