# http://dogs.ceo
from googletrans import Translator


translator = Translator()
url = "https://images.dog.ceo/breeds/hound-ibizan/n02091244_966.jpg"
start = url.find('breeds/') + len('breeds/')  # Находим начало названия породы
end = url.find('/', start)  # Находим следующий слеш '/'
breed = url[start:end]  # Вырезаем подстроку между start и end
translation = translator.translate(breed, src='en', dest='ru')
print(translation.text)  # Выводим: hound-ibizan