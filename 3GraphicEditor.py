# Импорт всех классов и функций из модуля tkinter для создания GUI
from tkinter import *
# Импорт модуля для работы с диалогами выбора файлов
from tkinter import filedialog as fd
# Импорт модуля для отображения информационных сообщений и ошибок
from tkinter import messagebox as mb
# Импорт модуля PIL для работы с изображениями
from PIL import Image, ImageTk, ImageGrab
# Импорт модуля stepic для стеганографии (встраивание данных в изображения)
import stepic


# Задаю Глобальные переменные
pen_color = "black"  # Начальный цвет пера
pen_width = 5  # Начальная толщина пера (в пикселях)

# Функция-обработчик для рисования на холсте при движении мыши
def draw(event):
    # Получаем координаты курсора мыши относительно холста
    x, y = event.x, event.y
    # Используем глобальную переменную pen_width для толщины
    # Создаем круг (овал с равными сторонами) в точке рисования
    # Размер круга определяется толщиной пера: радиус = pen_width//2
    # fill=pen_color - цвет заливки, outline=pen_color - цвет контура
    canvas.create_oval(x - pen_width//2, y - pen_width//2,
                      x + pen_width//2, y + pen_width//2,
                      fill=pen_color, outline=pen_color)

# Функция установки цвета пера
def set_pen_color(color):
    global pen_color
    pen_color = color

# Функция для обновления толщины пера из поля ввода
def update_pen_width():
    global pen_width  # Объявляем, что будем изменять глобальную переменную
    try:
        # Преобразовать введенное значение в целое число
        new_width = int(width_entry.get())
        # Проверяем, что толщина положительная (больше 0)
        if new_width > 0:
            pen_width = new_width  # Устанавливаем новую толщину
            # Показываем информационное сообщение об успешном изменении
            mb.showinfo("Обновлена толщины пера", f"Толщина пера установлена на {pen_width}")
        else:
            # Выводим ошибку, если толщина <= 0
            mb.showerror("Ошибка", "Толщина должна быть задана положительным числом")
    except ValueError:
        # Обработка исключения, если введено не целое число
        mb.showerror("Ошибка", "Пожалуйста, введите целое положительное число")

# Функция для загрузки изображения на холст
def load_image():
    try:
        # Открываем диалог выбора файла с фильтром по типам изображений
        file_path = fd.askopenfilename(filetypes=[('Image files', '*.png;*.jpg;*.jpeg;*.bmp;*.gif')])
        if file_path:  # Если файл выбран (не отменен диалог)
            image = Image.open(file_path)  # Открываем изображение
            image = image.resize((600, 400))  # Изменяем размер под холст
            image_tk = ImageTk.PhotoImage(image)  # Преобразуем в формат Tkinter
            canvas.create_image(0, 0, anchor=NW, image=image_tk)  # Размещаем на холсте
            canvas.image = image_tk  # Сохраняем ссылку, чтобы изображение не удалилось сборщиком мусора
    except Exception as e:
        # Обрабатываем любые ошибки при загрузке
        mb.showerror("Ошибка", f"Не удалось загрузить изображение: {e}")

# Функция для сохранения содержимого холста в файл
def save_canvas():
    try:
        # Открываем диалог сохранения файла с указанием расширения
        file_path = fd.asksaveasfilename(defaultextension='.png',
                                        filetypes=[('PNG files', '*.png'),
                                                  ('JPEG files', '*.jpg'),
                                                  ('All files', '*.*')])
        if file_path:  # Если путь сохранения выбран
            # Координаты холста на экране
            x = window.winfo_rootx() + canvas.winfo_x()
            y = window.winfo_rooty() + canvas.winfo_y()
            x1 = x + canvas.winfo_width()   # Правая граница
            y1 = y + canvas.winfo_height()  # Нижняя граница
            # Делаем скриншот области холста и сохраняем
            ImageGrab.grab().crop((x, y, x1, y1)).save(file_path)
            mb.showinfo("Сохранено!", "Изображение успешно сохранено!")
    except Exception as e:
        # Обрабатываем ошибки сохранения
        mb.showerror("Ошибка", f"Не удалось сохранить: {e}")

# Функция для очистки холста
def clear_canvas():
    canvas.delete("all")  # Удаляем все объекты с холста
    mb.showinfo("Очистка", "Холст очищен")  # Информируем пользователя

# Функция для выхода из программы
def quit_app():
    window.destroy()  # Закрываем главное окно

# Функция-обработчик для выбора цвета (замена lambda)
def on_color_click(event):
    """Обработчик клика по цветной метке"""
    # Получаем цвет из атрибута bg метки
    color = event.widget.cget('bg')
    set_pen_color(color)

# Создание главного окна приложения
window = Tk()  # Создаем экземпляр главного окна
window.title("Графический редактор")  # Устанавливаем заголовок окна
window.geometry("800x600")  # Устанавливаем размер окна

# Создание главного меню
menu_bar = Menu(window)  # Создаем объект меню
window.config(menu=menu_bar)  # Прикрепляем меню к окну

# Создание подменю "Файл"
file_menu = Menu(menu_bar, tearoff=0)  # tearoff=0 - убираем возможность открепления
menu_bar.add_cascade(label="Файл", menu=file_menu)  # Добавляем пункт меню
file_menu.add_command(label="Загрузить изображение", command=load_image)  # Команда загрузки
file_menu.add_command(label="Сохранить холст", command=save_canvas)  # Команда сохранения
file_menu.add_separator()  # Разделитель в меню
file_menu.add_command(label="Выход", command=quit_app)  # Команда выхода

# Панель инструментов (Toolbar)
toolbar = Frame(window, bg="lightgray", height=50)  # Создаем фрейм с серым фоном
toolbar.pack(fill=X, side=TOP)  # Размещаем вверху, растягиваем по ширине

# Фрейм для выбора цвета
color_frame = Frame(toolbar, bg="lightgray")  # Фрейм внутри панели
color_frame.pack(side=LEFT, padx=5)  # Размещаем слева с отступом

# Подпись для выбора цвета
Label(color_frame, text="Цвет:", bg="lightgray").pack(side=LEFT, padx=5)

# Палитра цветов - список названий цветов
colors = ["red", "green", "blue", "black", "yellow", "purple", "orange"]
for color in colors:
    # Создаем цветную метку для каждого цвета
    lbl = Label(color_frame, text="", bg=color, width=3, height=1, relief=RAISED, bd=2)
    lbl.pack(side=LEFT, fill=X, pady=5)  # Размещаем слева с отступом
    # Привязываем событие клика с использованием отдельной функции-обработчика
    lbl.bind("<Button-1>", on_color_click)

# Фрейм для настройки толщины пера
width_frame = Frame(toolbar, bg="lightgray")
width_frame.pack(side=LEFT, padx=20)  # Размещаем слева с большим отступом

# Подпись для толщины
Label(width_frame, text="Толщина:", bg="lightgray").pack(side=LEFT, padx=5)

# Поле ввода для толщины
width_entry = Entry(width_frame, width=5)  # Создаем поле ввода шириной 5 символов
width_entry.insert(0, "5")  # Устанавливаем начальное значение "5"
width_entry.pack(side=LEFT, padx=5)  # Размещаем слева

# Кнопка для применения новой толщины
Button(width_frame, text="Установить", command=update_pen_width).pack(side=LEFT, padx=5)

# Кнопка очистки холста (размещена справа)
Button(toolbar, text="Очистить", command=clear_canvas, bg="lightcoral").pack(side=RIGHT, padx=10)

# Создание холста для рисования
canvas = Canvas(window, width=600, height=400, bg="white")  # Белый фон
canvas.pack(expand=True, fill=BOTH)  # Расширяем и заполняем все доступное пространство

# Привязка события рисования: при движении мыши с зажатой левой кнопкой вызывается draw
canvas.bind("<B1-Motion>", draw)

# Запуск главного цикла обработки событий (приложение начинает работу)
window.mainloop()