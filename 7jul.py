"""
from tkinter import *
a = 128512

def change():
    global a
    a+=1
    metka['text'] = chr(a)

window = Tk()
metka = Label(text = chr(a), font='Arial 64')
metka.pack()
knopka = Button(text="Следующий", font='Arial 14')
knopka.config(command=change)
knopka.pack()
metka1 = Label(text="Метка 1", bg="red")
metka1.pack()
metka2 = Label(text="Метка 2", bg="yellow")
metka2.pack()
metka3 = Label(text="Метка 3", bg="lightgreen")
metka3.pack()
metka1 = Label(text="Метка 1", bg="red")
metka1.pack(side=LEFT)
metka2 = Label(text="Метка 2", bg="yellow")
metka2.pack(side=LEFT)
metka3 = Label(text="Метка 3", bg="lightgreen")
metka3.pack(side=LEFT)

frame_top = Frame(window)
frame_bottom = Frame(window)
frame_top.pack()
frame_bottom.pack()

metka1 = Label(frame_top, text="Метка 1", bg="red")
metka1.pack(side=LEFT)
metka2 = Label(frame_top, text="Метка 2", bg="yellow")
metka2.pack(side=LEFT)
metka3 = Label(frame_bottom, text="Метка 3", bg="lightgreen")
metka3.pack(side=LEFT)
metka4 = Label(frame_bottom, text="Метка 4", bg="lightblue")
metka4.pack(side=LEFT)



window.mainloop()

import tkinter as tk

window = tk.Tk()
window.title("Пример с фреймами и метками")

frame_top = tk.Frame(window)
frame_bottom = tk.Frame(window)

frame_top.pack()
frame_bottom.pack()

tk.Label(frame_top, text='Метка 1', bg='red').pack(side=tk.LEFT, padx=5, pady=5)
tk.Label(frame_top, text='Метка 2', bg='yellow').pack(side=tk.LEFT, padx=5, pady=5)
tk.Label(frame_top, text='Метка 3', bg='lightgreen').pack(side=tk.LEFT, padx=5, pady=5)

tk.Label(frame_bottom, text='Метка 4', bg='lightblue').pack(side=tk.RIGHT, padx=5, pady=5)
tk.Label(frame_bottom, text='Метка 5', bg='pink').pack(side=tk.RIGHT, padx=5, pady=5)
tk.Label(frame_bottom, text='Метка 6', bg='magenta').pack(side=tk.RIGHT, padx=5, pady=5)

window.mainloop()


from tkinter import *

window = Tk()

metka = Label(

text="Я люблю Python",

fg="Indigo",

bg="Lavender",

width=15,

height=5)

metka.pack()

window.mainloop()
"""
"""
from tkinter import *
from tkinter import messagebox as mb

def book_seat():
    s = seat_entry.get().upper()
    try:
        if seats[s] == 'свободно':
            seats[s] = 'забронировано'
            update_canvas()
            mb.showinfo("Успех", f"Место '{s}' успешно забронировано.")
        else:
            mb.showerror("Ошибка", f"Место '{s}' уже забронировано.")
    except KeyError:
        mb.showerror("Ошибка", f"Место '{s}' не существует.")

def update_canvas():
    canvas.delete("all")
    for i, (seat, status) in enumerate(seats.items()):
        x = i * 40 + 20  # Уменьшаем шаг и начальное смещение
        y = 20  # Фиксированное положение по оси Y для одного ряда
        color = "green" if status == 'свободно' else "red"
        canvas.create_rectangle(x, y, x + 30, y + 30, fill=color)  # Уменьшаем размер квадратов
        canvas.create_text(x + 15, y + 15, text=seat)  # Центрируем текст в квадрате


window = Tk()
window.title("Бронирование мест")
window.geometry("400x200")

canvas = Canvas(width=400, height=80)
canvas.pack(pady=10)

# Инициализация мест
seats = {f"Б{i}": 'свободно' for i in range(1, 10)}
update_canvas()

seat_entry = Entry()
seat_entry.pack(pady=10)

Button(text="Забронировать место", command=book_seat).pack(pady=10)

window.mainloop()
"""
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


class BookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Система бронирования мест")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        # Инициализация мест (3 ряда по 6 мест)
        self.seats = {}
        rows = ['A', 'B', 'C']
        for row in rows:
            for num in range(1, 7):
                self.seats[f"{row}{num}"] = 'свободно'

        # Создание интерфейса
        self.create_widgets()
        self.update_canvas()

    def create_widgets(self):
        # Заголовок
        title = Label(self.root, text="🎫 Бронирование мест в кинозале",
                      font=('Arial', 14, 'bold'))
        title.pack(pady=10)

        # Канвас для отображения мест
        self.canvas = Canvas(self.root, width=400, height=200, bg='white')
        self.canvas.pack(pady=10)

        # Легенда
        legend_frame = Frame(self.root)
        legend_frame.pack(pady=5)

        Label(legend_frame, text="●", fg="green", font=('Arial', 14)).pack(side=LEFT)
        Label(legend_frame, text="Свободно", font=('Arial', 10)).pack(side=LEFT, padx=(0, 15))

        Label(legend_frame, text="●", fg="red", font=('Arial', 14)).pack(side=LEFT)
        Label(legend_frame, text="Забронировано", font=('Arial', 10)).pack(side=LEFT)

        # Поле ввода
        input_frame = Frame(self.root)
        input_frame.pack(pady=10)

        Label(input_frame, text="Введите место (например, A1):",
              font=('Arial', 10)).pack(side=LEFT, padx=5)

        self.seat_entry = Entry(input_frame, width=10, font=('Arial', 10))
        self.seat_entry.pack(side=LEFT, padx=5)
        self.seat_entry.bind('<Return>', lambda e: self.book_seat())

        # Кнопки
        button_frame = Frame(self.root)
        button_frame.pack(pady=10)

        Button(button_frame, text="Забронировать", command=self.book_seat,
               bg='#4CAF50', fg='white', font=('Arial', 10), width=15).pack(side=LEFT, padx=5)

        Button(button_frame, text="Отменить бронь", command=self.cancel_booking,
               bg='#f44336', fg='white', font=('Arial', 10), width=15).pack(side=LEFT, padx=5)

        Button(button_frame, text="Сбросить все", command=self.reset_all,
               bg='#FF9800', fg='white', font=('Arial', 10), width=15).pack(side=LEFT, padx=5)

        # Статистика
        self.stats_label = Label(self.root, text="", font=('Arial', 10))
        self.stats_label.pack(pady=5)

        self.update_stats()

    def book_seat(self):
        s = self.seat_entry.get().strip().upper()
        if not s:
            mb.showwarning("Предупреждение", "Введите номер места!")
            return

        try:
            if self.seats[s] == 'свободно':
                self.seats[s] = 'забронировано'
                self.update_canvas()
                self.update_stats()
                mb.showinfo("Успех", f"✅ Место '{s}' успешно забронировано!")
                self.seat_entry.delete(0, END)
            else:
                mb.showerror("Ошибка", f"❌ Место '{s}' уже забронировано!")
        except KeyError:
            mb.showerror("Ошибка", f"❌ Место '{s}' не существует!\nДоступны: A1-A6, B1-B6, C1-C6")

    def cancel_booking(self):
        s = self.seat_entry.get().strip().upper()
        if not s:
            mb.showwarning("Предупреждение", "Введите номер места!")
            return

        try:
            if self.seats[s] == 'забронировано':
                self.seats[s] = 'свободно'
                self.update_canvas()
                self.update_stats()
                mb.showinfo("Успех", f"✅ Бронь на место '{s}' отменена!")
                self.seat_entry.delete(0, END)
            else:
                mb.showerror("Ошибка", f"❌ Место '{s}' не забронировано!")
        except KeyError:
            mb.showerror("Ошибка", f"❌ Место '{s}' не существует!")

    def reset_all(self):
        if mb.askyesno("Подтверждение", "Вы уверены, что хотите сбросить все брони?"):
            for seat in self.seats:
                self.seats[seat] = 'свободно'
            self.update_canvas()
            self.update_stats()
            mb.showinfo("Успех", "✅ Все брони сброшены!")

    def update_canvas(self):
        self.canvas.delete("all")

        # Рисуем сетку мест
        rows = ['A', 'B', 'C']
        for row_idx, row in enumerate(rows):
            for col_idx, num in enumerate(range(1, 7)):
                seat = f"{row}{num}"
                status = self.seats[seat]

                x = col_idx * 60 + 40
                y = row_idx * 60 + 30

                # Цвет в зависимости от статуса
                color = "#4CAF50" if status == 'свободно' else "#f44336"

                # Рисуем квадрат
                self.canvas.create_rectangle(x, y, x + 40, y + 40,
                                             fill=color, outline="black", width=1)

                # Текст внутри квадрата
                self.canvas.create_text(x + 20, y + 20, text=seat,
                                        font=('Arial', 9, 'bold'), fill="white")

        # Заголовки рядов
        for row_idx, row in enumerate(rows):
            y = row_idx * 60 + 50
            self.canvas.create_text(15, y, text=row, font=('Arial', 10, 'bold'))

    def update_stats(self):
        total = len(self.seats)
        booked = sum(1 for status in self.seats.values() if status == 'забронировано')
        free = total - booked

        self.stats_label.config(
            text=f"📊 Статистика: Всего мест: {total} | Свободно: {free} | Забронировано: {booked}",
            fg='blue' if free > 0 else 'red'
        )


# Запуск приложения
if __name__ == "__main__":
    root = Tk()
    app = BookingApp(root)
    root.mainloop()

