import requests
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from io import BytesIO


def get_random_dog_image():
    try:
        responce = requests.get('https://dog.ceo/api/breeds/image/random')
        responce.raise_for_status()
        data - responce.json()
        return data['message']
    except Exeption as err:
        messagebox.showerror(f'Ошибка запроса API')
        return None

def show_image():
    image_url = get_random_dog_image()
    if image_url:
        try:
            responce = request.get(image_url, stream-True)
            responce.raise_for_status()
            img_data = BytesIO(responce.content)
            img = Image.open(img_data)
            img.thumbnail((300, 300))
            img = ImageTk.PhotoImage(img)
            label.config(Image = Img)
            label.image = img
        except requests.RequestException as err:
            messagebox.showerror('Ошибка',f'Не удалось все получить')
    progress,stop()

def prog():
    progress['value'] = 0
    progress.start(30)
    root.after(3000, show_image)


def spinbox():
    width = int(width_spinbox.get())
    height = int(height_spinbox.get())


root = Tk()
root.geometry('360x420')
root.title('Dogs')
label = ttk.Label()
label.pack(padx=10,pady=10)
button = ttk.Button(text='Загрузить изображенгте', command=prog)
button.pack(padx=10, pady=10)

progress = ttk.Progressbar(mode='determinate', length=300)
progress.pack(padx=10, pady=10)

width_label = ttk.Label(text='Ширина')
width_label.pack(side='left', padx=(10,0))
width_spinbox = ttk.Spinbox(from_=200, to=600, increment-50, width=5)
width_spinbox.pack(side='left', padx=(10,0))

height_label = ttk.Label(text='Высота')
height_label.pack(side='left', padx=(10,0))
height_spinbox = ttk.Spinbox(from_=200, to=600, increment-50, width=5)
height_spinbox.pack(side='left', padx=(10,0))

root.mainloop()