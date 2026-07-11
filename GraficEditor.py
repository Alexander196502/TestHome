#Графический
#редактор
#собранная
#версия
#графического
#редактора
#с
#функциями:

#python
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from PIL import Image, ImageTk, ImageGrab
import stepic


class GraphicEditor:
    def __init__(self):
        self.window = Tk()
        self.window.title("Графический редактор")
        self.window.geometry("800x600")

        # Переменные для рисования
        self.pen_color = "black"
        self.pen_size = 5

        # Создание меню
        self.create_menu()

        # Создание панели инструментов
        self.create_toolbar()

        # Создание холста
        self.canvas = Canvas(self.window, width=600, height=400, bg="white")
        self.canvas.pack(pady=10)
        self.canvas.bind("<B1-Motion>", self.draw)

        # Создание панели цветов
        self.create_color_palette()

        # Создание панели размеров
        self.create_size_controls()

    def create_menu(self):
        """Создание главного меню"""
        menu_bar = Menu(self.window)
        self.window.config(menu=menu_bar)

        # Меню "Файл"
        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Файл", menu=file_menu)
        file_menu.add_command(label="Загрузить изображение", command=self.load_image)
        file_menu.add_command(label="Сохранить холст", command=self.save_canvas)
        file_menu.add_separator()
        file_menu.add_command(label="Выход", command=self.quit_app)

        # Меню "Стеганография"
        stego_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Стеганография", menu=stego_menu)
        stego_menu.add_command(label="Зашифровать текст", command=self.encode_text)
        stego_menu.add_command(label="Расшифровать текст", command=self.decode_text)

    def create_toolbar(self):
        """Создание панели инструментов"""
        toolbar = Frame(self.window)
        toolbar.pack(pady=5)

        Button(toolbar, text="Очистить", command=self.clear_canvas).pack(side=LEFT, padx=5)
        Button(toolbar, text="Загрузить", command=self.load_image).pack(side=LEFT, padx=5)
        Button(toolbar, text="Сохранить", command=self.save_canvas).pack(side=LEFT, padx=5)

    def create_color_palette(self):
        """Создание палитры цветов"""
        color_frame = Frame(self.window)
        color_frame.pack(pady=5)

        Label(color_frame, text="Цвет: ").pack(side=LEFT)

        colors = ["black", "red", "green", "blue", "yellow", "purple", "orange", "pink", "brown"]
        for color in colors:
            lbl = Label(color_frame, text="", bg=color, width=3, height=1, relief=RAISED)
            lbl.pack(side=LEFT, padx=2)
            lbl.bind("<Button-1>", lambda e, c=color: self.change_color(c))

    def create_size_controls(self):
        """Создание элементов управления размером кисти"""
        size_frame = Frame(self.window)
        size_frame.pack(pady=5)

        Label(size_frame, text="Размер: ").pack(side=LEFT)

        sizes = [3, 5, 7, 10, 15, 20]
        for size in sizes:
            btn = Button(size_frame, text=str(size), width=3,
                         command=lambda s=size: self.change_size(s))
            btn.pack(side=LEFT, padx=2)

    def draw(self, event):
        """Функция для рисования на холсте"""
        x, y = event.x, event.y
        self.canvas.create_oval(x - self.pen_size // 2, y - self.pen_size // 2,
                                x + self.pen_size // 2, y + self.pen_size // 2,
                                fill=self.pen_color, outline=self.pen_color)

    def change_color(self, color):
        """Изменение цвета кисти"""
        self.pen_color = color

    def change_size(self, size):
        """Изменение размера кисти"""
        self.pen_size = size

    def clear_canvas(self):
        """Очистка холста"""
        self.canvas.delete("all")

    def load_image(self):
        """Загрузка изображения на холст"""
        try:
            file_path = fd.askopenfilename(
                filetypes=[('Image files', '*.png;*.jpg;*.jpeg;*.bmp;*.gif')]
            )
            if file_path:
                image = Image.open(file_path)
                image = image.resize((600, 400))
                image_tk = ImageTk.PhotoImage(image)
                self.canvas.create_image(0, 0, anchor=NW, image=image_tk)
                self.canvas.image = image_tk
        except Exception as e:
            mb.showerror("Ошибка", f"Не удалось загрузить изображение: {e}")

    def save_canvas(self):
        """Сохранение холста в файл"""
        try:
            file_path = fd.asksaveasfilename(
                defaultextension='.png',
                filetypes=[('PNG files', '*.png'), ('JPEG files', '*.jpg')]
            )
            if file_path:
                x = self.window.winfo_rootx() + self.canvas.winfo_x()
                y = self.window.winfo_rooty() + self.canvas.winfo_y()
                x1 = x + self.canvas.winfo_width()
                y1 = y + self.canvas.winfo_height()
                ImageGrab.grab().crop((x, y, x1, y1)).save(file_path)
                mb.showinfo("Сохранено!", "Изображение успешно сохранено!")
        except Exception as e:
            mb.showerror("Ошибка", f"Не удалось сохранить: {e}")

    def encode_text(self):
        """Шифрование текста в изображении"""
        # Создаем диалоговое окно для ввода текста
        encode_window = Toplevel(self.window)
        encode_window.title("Шифрование текста")
        encode_window.geometry("400x200")

        Label(encode_window, text="Текст для шифрования:").pack(pady=5)
        text_entry = Entry(encode_window, width=40)
        text_entry.pack(pady=5)

        Label(encode_window, text="Сохранить как:").pack(pady=5)
        name_entry = Entry(encode_window, width=40)
        name_entry.insert(0, "encoded_image.png")
        name_entry.pack(pady=5)

        def do_encode():
            try:
                # Сохраняем текущий холст как изображение
                x = self.window.winfo_rootx() + self.canvas.winfo_x()
                y = self.window.winfo_rooty() + self.canvas.winfo_y()
                x1 = x + self.canvas.winfo_width()
                y1 = y + self.canvas.winfo_height()
                temp_image = ImageGrab.grab().crop((x, y, x1, y1))

                # Кодируем текст
                text = text_entry.get()
                output_name = name_entry.get()

                encoded_image = stepic.encode(temp_image, text.encode())
                encoded_image.save(output_name)

                mb.showinfo("Успешно", f"Текст успешно зашифрован в файл {output_name}")
                encode_window.destroy()
            except Exception as e:
                mb.showerror("Ошибка", str(e))

        Button(encode_window, text="Зашифровать", command=do_encode).pack(pady=10)

    def decode_text(self):
        """Расшифровка текста из изображения"""
        try:
            file_path = fd.askopenfilename(
                filetypes=[('Image files', '*.png;*.jpg;*.jpeg;*.bmp;*.gif')]
            )
            if file_path:
                image = Image.open(file_path)
                decoded_text = stepic.decode(image)

                # Показываем расшифрованный текст
                decode_window = Toplevel(self.window)
                decode_window.title("Расшифрованный текст")
                decode_window.geometry("400x200")

                Label(decode_window, text="Расшифрованный текст:", font=("Arial", 12)).pack(pady=10)
                text_widget = Text(decode_window, height=5, width=40)
                text_widget.pack(pady=10)
                text_widget.insert("1.0", decoded_text)
                text_widget.config(state="disabled")

                Button(decode_window, text="Закрыть", command=decode_window.destroy).pack(pady=10)
        except Exception as e:
            mb.showerror("Ошибка", f"Не удалось расшифровать: {e}")

    def quit_app(self):
        """Выход из приложения"""
        if mb.askyesno("Выход", "Вы уверены, что хотите выйти?"):
            self.window.destroy()

    def run(self):
        """Запуск приложения"""
        self.window.mainloop()


# Запуск приложения
if __name__ == "__main__":
    editor = GraphicEditor()
    editor.run()