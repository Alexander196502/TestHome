import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb

def add_note():
    file_path = fd.askopenfilename(
        title="Выберите файл с заметкой",
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
    )

    if not file_path:
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            note = f.read()
        txt.insert(tk.END, note + "\n")  # <-- исправлено
    except Exception as e:
        mb.showerror("Ошибка", f"Не удалось прочитать файл:\n{e}")

def del_note():
    txt.delete('1.0', 'end')

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

win = tk.Tk()
win.title('Менеджер заметок')

# Центрирование окна
WIDTH = win.winfo_screenwidth()
HEIGHT = win.winfo_screenheight()
X, Y = 800, 500
pos_x = WIDTH // 2 - X // 2
pos_y = HEIGHT // 2 - Y // 2
win.geometry(f'{X}x{Y}+{pos_x}+{pos_y}')

# Меню
mainmenu = tk.Menu(win)
win.config(menu=mainmenu)
fm = tk.Menu(mainmenu, tearoff=0)
fm.add_command(label="Открыть", command=add_note)
fm.add_command(label="Очистить", command=del_note)
fm.add_command(label="Сохранить", command=write_note)
fm.add_separator()
fm.add_command(label="Закрыть", command=win.destroy)
mainmenu.add_cascade(label="File", menu=fm)

# Текстовое поле со скроллбаром
txt = tk.Text(win, width=40, height=8)
txt.pack(side='left', padx=10, pady=10, fill='both', expand=True)

scr = tk.Scrollbar(win, command=txt.yview)
scr.pack(side='right', fill='y')
txt.configure(yscrollcommand=scr.set)

win.mainloop()