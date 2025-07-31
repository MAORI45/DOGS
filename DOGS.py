# http://dogs.ceo



def extract_breed ():
    try:
        url = "https://images.dog.ceo/breeds/hound-ibizan/n02091244_966.jpg"
        start = url.find('breeds/') + len('breeds/')  # Находим начало названия породы
        end = url.find('/', start)  # Находим следующий слеш '/'
        if start == -1 or end == -1:
            raise ValueError("URL не содержит информацию о породе")
        breed = url[start:end]  # Вырезаем подстроку между start и end
        if not breed:
            raise ValueError("Не удалось извлечь породу")

        return breed

    except Exception as e:
        raise ValueError(f"Ошибка обработки URL: {str(e)}")

# translation_str = str(translation)
# print(translation_str)  # Выводим: hound-ibizan