"""
Задание 3
Доработайте проект калькулятора. Добавьте кнопку для умножения трех чисел в том числе дробных.
"""
import tkinter as tk
from tkinter import *

# Функция сложения
def addition():
    try:
        # Получаем значения из полей ввода и преобразуем их в числа с плавающей точкой
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        num3 = float(entry3.get())
        # Результат сложения
        result = num1 + num2 + num3
        # Обновляем текст в label с результатом
        result_label.config(text=f"Сумма: {result:.2f}")
    except ValueError:
        # Если введены не цифры
        result_label.config(text="Ошибка: введите числа (можно дробные)!")

# Функция умножения
def multiplication():
    try:
        # Получаем значения из полей ввода и преобразуем их в числа с плавающей точкой
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        num3 = float(entry3.get())
        # Результат умножения
        result = num1 * num2 * num3
        # Обновляем текст в label с результатом
        result_label.config(text=f"Произведение: {result:.2f}")
    except ValueError:
        # Если введены не цифры
        result_label.config(text="Ошибка: введите числа (можно дробные)!")

# Очистка полей
def clear_fields():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    result_label.config(text="")
    # Возвращаем фокус на первое поле
    entry1.focus()

# Завершение работы
def programmStop():
    root.destroy()

# Создание окна
root = tk.Tk()
root.geometry("500x450")
root.title("Калькулятор")
root.resizable(False, False)

# Создаём рамку (Frame) и размещаем её на всё окно
frame = tk.Frame(root, bg="#f0f0f0", highlightbackground="#4a90d9", highlightthickness=3)
frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Заголовок
title_label = Label(frame, text="🧮 Калькулятор", font=("Arial", 16, "bold"),
                   bg="#f0f0f0", fg="#2c3e50")
title_label.pack(pady=10)

# Текст-инструкция
textwindow = Label(frame, text='Введите три числа и нажмите на кнопку для вычисления:',
                   font=("Arial", 10), bg="#f0f0f0")
textwindow.pack(pady=5)

# Поля ввода с подписями
label1 = Label(frame, text="Число 1:", font=("Arial", 10), bg="#f0f0f0")
label1.pack(anchor="w", padx=100)
entry1 = tk.Entry(frame, width=30, font=("Arial", 10), relief="solid", bd=1)
entry1.pack(pady=2)

label2 = Label(frame, text="Число 2:", font=("Arial", 10), bg="#f0f0f0")
label2.pack(anchor="w", padx=100)
entry2 = tk.Entry(frame, width=30, font=("Arial", 10), relief="solid", bd=1)
entry2.pack(pady=2)

label3 = Label(frame, text="Число 3:", font=("Arial", 10), bg="#f0f0f0")
label3.pack(anchor="w", padx=100)
entry3 = tk.Entry(frame, width=30, font=("Arial", 10), relief="solid", bd=1)
entry3.pack(pady=2)

# Кнопки в рамке
button_frame = Frame(frame, bg="#f0f0f0")
button_frame.pack(pady=10)

# Кнопка сложения
button1 = tk.Button(button_frame, text="➕ Сложить три числа", bg="#4a90d9",
                   fg="white", font=("Arial", 10, "bold"), width=18, height=1)
button1.pack(side=LEFT, padx=5)
button1.config(command=addition)

# Кнопка умножения
button2 = tk.Button(button_frame, text="✖️ Умножить три числа", bg="#27ae60",
                   fg="white", font=("Arial", 10, "bold"), width=18, height=1)
button2.pack(side=LEFT, padx=5)
button2.config(command=multiplication)

# Изменение курсора при наведении на кнопки
for btn in [button1, button2]:
    btn.bind("<Enter>", lambda e, b=btn: b.config(cursor="hand2"))
    btn.bind("<Leave>", lambda e, b=btn: b.config(cursor=""))

# Label для отображения результата
result_frame = Frame(frame, bg="#ffffff", relief="solid", bd=1)
result_frame.pack(pady=10, padx=50, fill="x")

text_Rez = Label(result_frame, text="Результат: ", font=("Arial", 12, "bold"),
                bg="#ffffff", fg="#2c3e50")
text_Rez.pack(side=LEFT, padx=10, pady=5)

result_label = Label(result_frame, font=("Arial", 12, "bold"),
                    bg="#ffffff", fg="#e74c3c")
result_label.pack(side=LEFT, padx=5, pady=5)

# Нижняя панель с кнопками управления
control_frame = Frame(frame, bg="#f0f0f0")
control_frame.pack(pady=5)

# Очистка полей
buttonClear = tk.Button(control_frame, text="🗑️ Очистить поля", bg="#f39c12",
                       fg="white", font=("Arial", 10), width=14)
buttonClear.pack(side=LEFT, padx=5)
buttonClear.config(command=clear_fields)
buttonClear.bind("<Enter>", lambda e: buttonClear.config(cursor="hand2"))
buttonClear.bind("<Leave>", lambda e: buttonClear.config(cursor=""))

# Завершение работы
buttonStop = tk.Button(control_frame, text="❌ Выход", bg="#e74c3c",
                      fg="white", font=("Arial", 10), width=14)
buttonStop.pack(side=LEFT, padx=5)
buttonStop.config(command=programmStop)
buttonStop.bind("<Enter>", lambda e: buttonStop.config(cursor="hand2"))
buttonStop.bind("<Leave>", lambda e: buttonStop.config(cursor=""))

# Устанавливаем начальный фокус
entry1.focus()

# Запуск основного цикла
root.mainloop()