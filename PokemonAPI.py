import tkinter as tk
from io import BytesIO
from tkinter import ttk
import requests
from PIL import Image, ImageTk


def get_pokemon_data(number):
    url = f'https://pokeapi.co/api/v2/pokemon/{number}'  # Получаем адрес
    responce = requests.get(url)
    responce.raise_for_status()  # Проверить 200
    #data = responce.json()  # Получаем
    return responce.json()

def load_image():
    responce = requests.get(url)
    responce.raise_for_status()  # Проверить 200
    img = Image.open(BytesIO(responce.content))
    img.thumbnail((250, 250))
    return ImageTk.PhotoImage(img)


def show_pokemon():
    try:
        number = sb.get()  # Получаем номер из спинбокса
        data = get_pokemon_data(number)
        """
        url = f'https://pokeapi.co/api/v2/pokemon/{number}'  # Получаем адрес
        responce = requests.get(url)
        responce.raise_for_status()  # Проверить 200
        data = responce.json()  # Получаем
        print(data['sprites']['other']['official-artwork']['front_default'])
        """
        img_url = data['sprites']['other']['official-artwork']['front_default']
        photo = load_image()
        #responce = requests.get(img_url)
        #responce.raise_for_status()

        l.img = tk.Label(win, image=photo)
        l.img.image = photo
        l.img.place(pady=10)

    except Exception as e:
        print(f"e")



win = tk.Tk()
win.title('Pokemon Viewer')
win.geometry('400x300')

l = tk.Label(win, text='Pokemon Viewer')
l.pack(pady=10)

sb = ttk.Spinbox(win, from_=100, to=200)
sb.pack(pady=10)

sb.pack(pady=10)

b = ttk.Button(win, text='Показать Pokemon', command=show_pokemon)
b.pack(pady=10)

pb = ttk.Progressbar(win, orient='horizontal', length=400, mode='indeterminate')
pb.pack(pady=10)

win.mainloop()
