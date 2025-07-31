# http://dogs.ceo проект работа со ссылками

import requests
import tkinter
from tkinter import Tk, Toplevel, messagebox, Button, Label
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO

def show_image():
    image_url = get_dog_image() # отправляем функцию в функцию которая пришлет ссылку
    if image_url: # если ссылка не пустая
        try:
            response = requests.get(image_url, stream=True) # что-то по ссылке
            response.raise_for_status() # обрабатываем ошибку или статус ответа
            img_data = BytesIO(response.content) # загрузка изображения в двоичном коде
            img = Image.open(img_data) # открытие картинки
            img.thumbnail((300, 300)) # размер картинки - ее сжатие?
            label.config(image=img) # положить в метку картинку
            label.image = img # чтобы картинка осталась в памяти
        except Exception as e:
            messagebox.showerror("Ошибка", f"Возникла ошибка: {e}")


def extract_breed ():
    try:
        url = "https://images.dog.ceo/breeds/hound-ibizan/n02091244_966.jpg"
        start = url.find('breeds/') + len('breeds/')  # Находим начало названия породы
        end = url.find('/', start)  # Находим следующий слеш '/'
        if start == -1 or end == -1: # смотрим, что и breeds присутствует и после слеша информацмя
            raise ValueError("URL не содержит информацию о породе")
        breed = url[start:end]  # Вырезаем подстроку между start и end
        if not breed:
            raise ValueError("Не удалось извлечь породу")

        return breed

    except Exception as e:
        raise ValueError(f"Ошибка обработки URL: {str(e)}")


window = Tk() # кладем в переменную
window.title("Случайное изображение")
window.geometry("360x420")

label = Label()
label.pack(pady=10)

button = Button(text="Загрузить изображение", command=show_image)
button.pack(pady=10)

window.mainloop()