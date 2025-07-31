# http://dogs.ceo проект работа со ссылками

import requests
from tkinter import Tk, Toplevel, messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO



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

button = Button(text="Загрузить изображение", command=show_imedge)
button.pack(pady=10)

window.mainloop()