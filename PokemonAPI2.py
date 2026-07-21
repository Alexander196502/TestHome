import tkinter as tk
from tkinter import ttk, messagebox as mb
import requests
from PIL import Image, ImageTk
from io import BytesIO


# from TehZadanie14jul import current_path  # закомментировано, т.к. не используется


def get_pokemon_data(number: int):
    """
    Получает данные о покемоне из PokeAPI по его номеру.

    Аргументы:
        number (int): номер покемона (ID), который нужно запросить.

    Возвращает:
        dict: JSON-ответ от API в виде словаря с данными о покемоне.

    Логика работы:
        1. Формирует URL-адрес запроса к PokeAPI, подставляя номер покемона.
        2. Отправляет GET-запрос к API с таймаутом 10 секунд (чтобы программа не зависала надолго при проблемах с сетью).
        3. Вызывает response.raise_for_status() — если сервер вернул ошибку (например, 404 для несуществующего покемона), будет выброшено исключение HTTPError.
        4. Возвращает распарсенный JSON-ответ в виде Python-словаря.
    """
    url = f"https://pokeapi.co/api/v2/pokemon/{number}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


def load_image(url: str):
    """
    Загружает и подготавливает изображение покемона по URL.

    Аргументы:
        url (str): прямая ссылка на изображение (может быть None или пустой строкой).

    Возвращает:
        ImageTk.PhotoImage или None: готовое изображение для Tkinter либо None, если URL невалиден.

    Логика работы:
        1. Проверяет, передан ли URL. Если нет — сразу возвращает None, чтобы избежать лишних запросов.
        2. Делает GET-запрос по ссылке с таймаутом 10 секунд.
        3. Проверяет статус ответа через raise_for_status(), чтобы обработать ошибки сети/сервера.
        4. Открывает изображение из байтов (response.content) с помощью PIL.Image.
        5. Уменьшает изображение до 250×250 пикселей с сохранением пропорций (thumbnail) и качественным фильтром LANCZOS.
        6. Конвертирует изображение в формат, пригодный для отображения в Tkinter (ImageTk.PhotoImage).
    """
    if not url:
        return None
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    img = Image.open(BytesIO(response.content))
    img.thumbnail((250, 250), Image.LANCZOS)
    return ImageTk.PhotoImage(img)


def show_pokemon():
    """
    Основная функция отображения данных и картинки покемона.

    Логика работы:
        1. Пытается получить номер покемона из виджета Spinbox (sb) и преобразовать его в int.
        2. Запрашивает данные о покемоне через get_pokemon_data().
        3. Извлекает URL официального арта покемона из структуры JSON (поле front_default).
        4. Загружает изображение через load_image().
        5. Создаёт новую вкладку в Notebook, называет её именем покемона (с заглавной буквы).
        6. Размещает на вкладке Label с изображением; сохраняет ссылку на photo в атрибуте .image, чтобы сборщик мусора не удалил картинку.
        7. Формирует текстовую строку с базовой информацией: имя, рост, вес, базовый опыт.
        8. Отображает эту информацию в Label с выравниванием по левому краю.
        9. В случае любой ошибки (неверный номер, проблемы сети, отсутствие картинки и т.д.) показывает окно с ошибкой через messagebox.
        10. В блоке finally останавливает анимацию прогрессбара и возвращает кнопку в активное состояние — это выполняется всегда, даже при ошибке.
    """
    try:
        number = int(sb.get())
        data = get_pokemon_data(number)

        artwork = data['sprites']['other']['official-artwork']
        img_url = artwork.get('front_default')

        photo = load_image(img_url)

        tab = ttk.Frame(notebook)
        name = data['name'].capitalize()
        notebook.add(tab, text=name)

        l_img = tk.Label(tab, image=photo if photo else None)
        l_img.image = photo  # сохраняем ссылку, чтобы не удалилось сборщиком мусора
        l_img.pack(pady=10)

        info = (
            f"Имя: {data['name']}\n"
            f"Рост: {data['height']}\n"
            f"Вес: {data['weight']}\n"
            f"Опыт: {data['base_experience']}"
        )

        l_info = tk.Label(tab, text=info, font=("Arial", 13), justify="left")
        l_info.pack(pady=10)

    except Exception as e:
        mb.showerror("Ошибка", str(e))
    finally:
        pb.stop()
        b.config(state=tk.NORMAL)


def start_loading():
    """
    Подготавливает интерфейс к загрузке данных о покемоне и запускает процесс.

    Логика работы:
        1. Отключает кнопку, чтобы пользователь не мог нажать её повторно во время загрузки.
        2. Запускает анимацию неопределённого прогрессбара (indeterminate).
        3. Через 200 мс (win.after(200, show_pokemon)) вызывает функцию show_pokemon — такая задержка нужна, чтобы интерфейс успел отобразить прогрессбар до начала тяжёлой операции.
    """
    b.config(state=tk.DISABLED)
    pb.start(10)
    # небольшая задержка, чтобы прогрессбар успел отобразиться
    win.after(200, show_pokemon)


def show_info():
    """
    Показывает информационное окно «О программе» через messagebox.showinfo.
    Текст окна: «Tkinter + PokeAPI: просмотр покемонов по номеру».
    """
    mb.showinfo("О программе", "Tkinter + PokeAPI: просмотр покемонов по номеру")


def del_tab():
    """
    Удаляет текущую выбранную вкладку из Notebook.

    Логика работы:
        1. Получает идентификатор текущей вкладки через notebook.select().
        2. Если вкладка выбрана (current_tab не пустой), удаляет её методом forget().
    """
    current_tab = notebook.select()
    if current_tab:
        notebook.forget(current_tab)


# --- Создание главного окна приложения ---
win = tk.Tk()
win.title("Pokemon viewer")
win.geometry("400x500")  # чуть больше, чтобы всё помещалось

# --- Настройка главного меню ---
mainmenu = tk.Menu(win)
win.config(menu=mainmenu)

# Подменю «File»
filemenu = tk.Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Load", command=start_loading)
filemenu.add_separator()
filemenu.add_command(label="Close", command=win.destroy)

# Подменю «Справка»
help_menu = tk.Menu(mainmenu, tearoff=0)
help_menu.add_command(label="О программе", command=show_info)

# Добавляем подменю в главное меню
mainmenu.add_cascade(label="File", menu=filemenu)
mainmenu.add_cascade(label="Справка", menu=help_menu)

# --- Элементы интерфейса главного окна ---
l = tk.Label(win, text="Номер покемона")
l.pack(pady=10)

sb = ttk.Spinbox(win, from_=1, to=1000)
sb.pack(pady=10)

b = ttk.Button(win, text="Получить покемона", command=start_loading)
b.pack(pady=10)

pb = ttk.Progressbar(win, mode="indeterminate", length=250)
pb.pack(pady=10)

b_delete = ttk.Button(win, text="Удалить вкладку", command=del_tab)
b_delete.pack(pady=10)

# --- Окно с вкладками для покемонов ---
# Toplevel создаём только когда добавляем вкладки, а не сразу
top = tk.Toplevel(win)
top.title("Покемоны")
top.geometry("450x600")

notebook = ttk.Notebook(top)
notebook.pack(fill=tk.BOTH, expand=True)

# Запуск главного цикла обработки событий Tkinter
win.mainloop()