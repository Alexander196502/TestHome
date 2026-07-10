import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb

def add_note():
    # Открываем диалог выбора файла
    file_path = fd.askopenfilename(
        title="Выберите файл с заметкой",
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
    )

    # Если пользователь отменил выбор — ничего не делаем
    if not file_path:
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            note = f.read()

        # Добавляем текст в конец поля

        txt.insert(tk.END, note + "\n")

    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось прочитать файл:\n{e}")


def del_note():

    # Очищаем поле ввода
    txt.delete('1.0', 'end')

#def write_note():
#    return#file_path = fd.askopenfilename()
def write_note():
    file_path = fd.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")],
        title="Сохранить заметку"
    )
    if not file_path:
        return

    content = txt.get('1.0', tk.END).strip()
    if not content:
        mb.showwarning("Внимание", "Нет текста для сохранения.")
        return

    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        mb.showinfo("Успех", "Заметка успешно сохранена!")
    except Exception as e:
        mb.showerror("Ошибка", f"Не удалось сохранить файл:\n{e}")


win = tk.Tk()  # создаём окно
WIDTH = win.winfo_screenwidth()  # ширина экрана
HEIGHT = win.winfo_screenheight()  # высота экрана

X = 800  # ширина окна приложения
Y = 500  # высота окна приложения

# Центрируем окно на экране
pos_x = WIDTH // 2 - X // 2
pos_y = HEIGHT // 2 - Y // 2
win.geometry(f'{X}x{Y}+{pos_x}+{pos_y}')

win.title('Менеджер заметок')
#root.config(bg='gray')
"""
# --- МЕНЮ ---
menubar = tk.Menu(win)
win.config(menu=menubar)

# Меню "Файл"
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Добавить заметку из файла", command=add_note)
file_menu.add_command(label="Очистить поле", command=del_note)
file_menu.add_separator()
file_menu.add_command(label="Сохранить заметку", command=write_note)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=win.quit)
"""
mainmenu = tk.Menu(win)
win.config(menu=mainmenu)
fm = tk.Menu(mainmenu, tearoff= 1)
fm.add_command(label = "Открыть", command= add_note)
fm.add_command(label = "Очистить", command= del_note)
fm.add_command(label = "Сохранить", command= write_note)
fm.add_separator()
fm.add_command(label = "Закрыть", command= win.destroy)
mainmenu.add_cascade(label ="File", menu=fm)

# Создаём виджет Text
txt = tk.Text(win, width=40, height=8)
txt.pack(side='left', padx=10, pady=10)



scr = tk.Scrollbar(win, command=txt.yview)
scr.pack(side='left', fill='y')
txt.configure(yscrollcommand=scr.set)
"""
### Кнопка «Добавить заметку»
start_btn = tk.Button(win, text='Добавить заметку', font=('Arial', 9), command=add_note)
start_btn.pack(side=tk.LEFT)

# Кнопка «Очистить поле»
stop_btn = tk.Button(win, text='Очистить поле', font=('Arial', 9), command=del_note)
stop_btn.pack(side=tk.LEFT)

write_btn = tk.Button(win, text='Сохранить заметку', font=('Arial', 9), command=write_note)
write_btn.pack(side=tk.LEFT)
"""
win.mainloop()