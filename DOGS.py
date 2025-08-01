# http://dogs.ceo проект работа со ссылками

import requests
from tkinter import Tk, Toplevel, messagebox, Button, Label
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO
import random


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
    status_label.config(text="Загрузка...")
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
            breed = extract_breed() or "Дворянин"
            tab = ttk.Frame(notebook)
            notebook.add(tab, text=f"Изображение {breed} {notebook.index('end') + 1}")
            label = ttk.Label(tab, image=img) # положить в метку-вкладку картинку
            label.image = img # чтобы картинка осталась в памяти
            label.pack(padx=10, pady=10)
            notebook.select(tab)  # Теперь вкладка открывается и показывается
            status_label.config(text="")
        except requests.RequestException as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить изображение: {e}")

def get_random_color():
    # Генерируем случайный цвет в формате HEX (#RRGGBB)
    return f"#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}"


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
        label1.config(text=breed, font=("Arial", 10, "bold")) # Сначала обновляем Label
        label1.config(fg=get_random_color()) # рандомные цвета отключить вместе с функцией
        return breed

    except Exception as e:
        messagebox.showerror(f"Ошибка обработки URL: {e}")
        return None


def start_progress():
    progress['value'] = 0
    progress.start(30)
    window.after(3000, lambda: [progress.stop(), show_image()])


window = Tk()
window.title("Случайное изображение")
window.geometry("360x250+500+500")

# Метка для названия породы
label1 = Label(window)
label1.pack(pady=5)

# Прогресс-бар
progress_frame = ttk.Frame(window)
progress_frame.pack(fill='x', pady=5)
progress = ttk.Progressbar(progress_frame, mode='determinate', length=300)
progress.pack(pady=5, anchor='center')

# Статус-лейбл
status_label = ttk.Label(window, text="")
status_label.pack(pady=5)

# Фрейм для кнопок
button_frame = ttk.Frame(window)
button_frame.pack(fill='x', pady=10)

button = ttk.Button(button_frame, text="Загрузить изображение", command=start_progress)
button.pack(side='left', padx=10, expand=True)

delete_button = ttk.Button(button_frame, text="Удалить все вкладки",
                         command=lambda: [notebook.forget(tab) for tab in notebook.tabs()])
delete_button.pack(side='left', padx=10, expand=True)

# Фрейм для настроек размеров
size_frame = ttk.Frame(window)
size_frame.pack(fill='x', pady=10)

width_label = ttk.Label(size_frame, text="Ширина:")
width_label.pack(side='left', padx=(10, 0))

width_spinbox = ttk.Spinbox(size_frame, from_=200, to=500, increment=50, width=5)
width_spinbox.pack(side='left', padx=(0, 10))
width_spinbox.set(300)  # Начальное значение 300

height_label = ttk.Label(size_frame, text="Высота:")
height_label.pack(side='left', padx=(10, 0))

height_spinbox = ttk.Spinbox(size_frame, from_=200, to=500, increment=50, width=5)
height_spinbox.pack(side='left', padx=(0, 10))
height_spinbox.set(300)  # Начальное значение 300

# Метка для изображения (если нужна)
label = Label(window)
label.pack(pady=5)

# Окно для Notebook
top_level_window = Toplevel(window)
top_level_window.title("Изображения пёсиков")
top_level_window.geometry("400x400")

notebook = ttk.Notebook(top_level_window)
notebook.pack(expand=True, fill='both', padx=10, pady=10)

window.mainloop()