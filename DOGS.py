# http://dogs.ceo проект работа со ссылками

import requests
from tkinter import Tk, Toplevel, messagebox, Button, Label
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO


def get_dog_image():
    try:
        response = requests.get("https://dog.ceo/api/breeds/image/random")  # что-то по ссылке
        response.raise_for_status()  # обрабатываем ошибку или статус ответа
        data = response.json()
        return data ['message']
    except Exception as e:
        messagebox.showerror("Ошибка", f"Возникла ошибка при запросе к API: {e}")
        return None


def show_image():
    image_url = get_dog_image() # отправляем функцию в функцию которая пришлет ссылку
    if image_url: # если ссылка не пустая
        try:
            response = requests.get(image_url, stream=True) # что-то по ссылке
            response.raise_for_status() # обрабатываем ошибку или статус ответа
            img_data = BytesIO(response.content) # загрузка изображения в двоичном коде
            img = Image.open(img_data) # открытие картинки
            img_size = (int(width_spinbox.get()), int(height_spinbox.get()))
            img.thumbnail(img_size) # размер картинки - ее сжатие?
            img = ImageTk.PhotoImage(img)
            label.config(image=img) # положить в метку картинку
            label.image = img # чтобы картинка осталась в памяти
            extract_breed()

        except Exception as e:
            messagebox.showerror("Ошибка", f"Возникла ошибка при загрузке изображений: {e}")


def extract_breed():
    try:
        url = get_dog_image()
        start = url.find('breeds/') + len('breeds/')  # Находим начало названия породы
        end = url.find('/', start)  # Находим следующий слеш '/'
        if start == -1 or end == -1: # смотрим, что и breeds присутствует и после слеша информацмя
            raise ValueError("URL не содержит информацию о породе")
        breed = url[start:end]  # Вырезаем подстроку между start и end
        if not breed:
            raise ValueError("Не удалось извлечь породу")
        label1.config(text=breed) # Сначала обновляем Label
        return breed

    except Exception as e:
        messagebox.showerror(f"Ошибка обработки URL: {e}")
        return None


window = Tk() # кладем в переменную
window.title("Случайное изображение")
window.geometry("360x420")
label1 = Label()
label1.pack(pady=10)

label = Label()
label.pack(pady=10)

button = Button(text="Загрузить изображение", command=show_image)
button.pack(pady=10)

width_label = ttk.Label(window, text="Ширина:")
width_label.pack(side='left', padx=(10, 0))
width_spinbox = ttk.Spinbox(window, from_=200, to=500, increment=50, width=5)
width_spinbox.pack(side='left', padx=(0, 10))

height_label = ttk.Label(window, text="Высота:")
height_label.pack(side='left', padx=(10, 0))
height_spinbox = ttk.Spinbox(window, from_=200, to=500, increment=50, width=5)
height_spinbox.pack(side='left', padx=(0, 10))

window.mainloop()