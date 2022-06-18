""" TODO:
    1) Разобрать метод make_text_from_file (стр. 25) на отдельные методы для разных расширений
"""
import re
from collections import Counter
from docx import Document  # pip install python-docx
import pymorphy2  # pip install pymorphy2
from wordcloud import WordCloud as wc  # pip install wordcloud
from charset_normalizer import from_path  # pip install charset-normalizer; нормализуем кодировку
from bs4 import BeautifulSoup  # pip install bs4


class App:
    def __init__(self, file_path: str, parts_of_speech: list=['NOUN', 'VERB', 'INFN']):
        """ инициализация объекта приложения """
        self.file_path = file_path # путь к файлу со словами
        self.content = self.make_text_from_file() # записываем файл текстом
        self.content = str(from_path(self.file_path).best())
        self.words = self.make_words_from_text() # записываем текст списком слов
        self.normalized_words = self.make_normalized_words(parts_of_speech) # создаем список с н. ф. 
                                                                            # слов изначального
        self.most_frequent_words = self.make_most_frequent_words(num=5)
        self.wordcloud = self.make_wordcloud(self.most_frequent_words)

    def make_text_from_file(self):
        """ преобразование файла в текст """
        # Проверяем расширение файла
        if self.file_path.endswith(".txt"):
            with open(self.file_path, "r", encoding="utf8") as file:
                content = file.read() # преобразуем txt-файл в текст
        elif self.file_path.endswith(".docx"):
            file = Document(self.file_path) # преобразуем docx-файл в текст
            content = " ".join([p.text for p in file.paragraphs])
        elif self.file_path.endswith(".fb2"): # преобразуем fb2-файл в текст
            with open(self.file_path) as file:
                content = file.read()
            soup = BeautifulSoup(content, "xml")
            paragraphs = soup.find_all('p')
            content = [p.text for p in paragraphs]
        else:
            content = ""
        return content

    def make_words_from_text(self):
        """ преобразование текста в отдельные слова """
        words = re.findall("[а-яё0-9]+", self.content.lower()) 
        return words

    def make_normalized_words(self, parts_of_speech: list):
        """ создаем новый список со словами в начальной форме
            только определенных частей речи """
        morph = pymorphy2.MorphAnalyzer()
        normalized_words = list()
        for word in self.words:
            parse = morph.parse(word)[0]
            if parse.tag.POS in parts_of_speech:
                normalized_words.append(parse.normal_form)
            else:
                continue
        return normalized_words

    def make_most_frequent_words(self, num: int = 10):
        """ создаем словарь с наиболее
        часто используемыми словами """
        counter = Counter(self.normalized_words).most_common(num)
        return dict(counter)
    
    def write_most_frequent_words(self, most_frequent_words):
        """ записываем словарь с популярными словами в файл """
        with open(self.file_path, "w", encoding="utf8") as file:
            for key, value in self.most_frequent_words.items():
                line = f"{key}: {value}\n"
                file.write(line)
            
    def make_wordcloud(self, text):
        """ создаем облако слов из самых популярных слов """
        result = wc(width=1920, height=1080, background_color='black')
        result = result.generate_from_frequencies(self.most_frequent_words)
        return result

    def save_wordcloud_to_file(self, filename: str = 'wordcloud.png'):
        """ сохраняем облако слов в файл """
        self.wordcloud.to_file(filename)


app = App("чтение из файла в список/input/text.fb2")
app.make_text_from_file()
app.save_wordcloud_to_file()