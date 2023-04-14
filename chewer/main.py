"""Text-Chewer program"""
import re  # разбираем строку на отдельные слова
from collections import Counter  # ищем часто используемые слова, счетчик объектов
import os  # работа с файлами

import pymorphy2  # pip3 install pymorphy2; pip3 install pymorphy2-dicts
import pyperclip  # pip3 install pyperclip
from bs4 import BeautifulSoup  # pip3 install bs4
from charset_normalizer import from_path  # pip3 install charset-normalizer
from docx import Document  # pip3 install python-docx
from wordcloud import WordCloud  # pip3 install wordcloud


class TheChewer:
    """Класс приложения"""

    def __init__(self, file_path: str,
                 parts_of_speech: list | tuple = ['ALL'],
                 height: int = 1920,
                 width: int = 1080,
                 words_quantity: int = 10,
                 colors: str = "Greys"
                 ):
        """Инициализация объекта класса приложения"""
        # self.toggle_copying = "off"  # копирование результата
        self.file_path = file_path  # путь к файлу (dish)
        self.words_quantity = words_quantity  # количество слов в облаке
        self.file_name = re.search(r'/\w+.\w+$', self.file_path)  # получение имени файла
        try:
            self.content = str(from_path(self.file_path).best())  # нормализация кодировки
        except FileNotFoundError:
            print('error!')

        self.content = self.make_text_from_file()  # получаем текст из файла
        self.words = self.write_all_words()  # запись слов в список
        self.parts_of_speech = parts_of_speech  # части речи, которые будем искать в тексте
        self.infinitive_words = self.write_infinitives(self.parts_of_speech)  #
        self.most_frequent_words = self.write_most_frequent_words()
        self.height_ = height
        self.width_ = width
        self.wordcloud = self.create_wordcloud(self.height_, self.width_)


    def make_text_from_file(self) -> str:
        """Проверка расширение файла, достаем текст;
        self.content"""
        if self.file_path.endswith(".txt"):
            content = self.make_text_from_txt()
        elif self.file_path.endswith(".fb2"):
            content = self.make_text_from_fb2()
        elif self.file_path.endswith(".docx"):
            content = self.make_text_from_docx()
        else:
            content = ""
        return content

    # ------------------------------

    def make_text_from_txt(self):
        """Работаем с txt-файлом"""
        content = str(from_path(self.file_path).best())
        return content

    def make_text_from_fb2(self):
        """Работаем с fb2-файлом"""
        with open(self.file_path, "rb") as file:
            data = file.read()
        bs_data = BeautifulSoup(data, "xml")
        paragraphs = bs_data.find_all("p")
        content = " ".join([p.text for p in paragraphs])
        return content

    def make_text_from_docx(self):
        """Работаем с docx-файлом"""
        document = Document(self.file_path)
        content = " ".join([p.text for p in document.paragraphs])
        return content

    # ------------------------------

    def write_all_words(self, text: str = None) -> list:
        """Создание списка всех слов текста;
        self.words"""
        if text is None:
            text = self.content
        words = re.findall(r"[а-яё0-9]+", text.lower())
        return words

    def write_infinitives(self, parts_of_speech=None) -> list:
        """Создание списка инфинитивных форм
        слов из текста определенных частей речи;
        self.infinitive_words"""
        if parts_of_speech is None:
            parts_of_speech = self.parts_of_speech
        if parts_of_speech == ["ALL"]:
            parts_of_speech = [
                "NOUN",
                "ADJF",
                "ADJS",
                "COMP",
                "VERB",
                "INFN",
                "PRTF",
                "PRTS",
                "GRND",
                "NUMR",
                "ADVB",
                "NPRO",
                "PRED",
                "PREP",
                "CONJ",
                "PRCL",
                "INTJ",
            ]
        else:
            morph = pymorphy2.MorphAnalyzer()
            infinitives = list()
            for word in self.words:
                parse = morph.parse(word)[0]
                if parse.tag.POS in parts_of_speech:
                    infinitives.append(parse.normal_form)
                else:
                    continue
            return infinitives

    def write_most_frequent_words(self) -> dict:
        """Создание словаря наиболее используемых слов;
        self.most_frequent_words"""
        top = self.words_quantity
        counter = Counter(self.infinitive_words).most_common(top)
        return dict(counter)

    def create_file_of_most_frequent_words(self):
        """Запись наиболее используемых слов в файл"""
        file_path = "Result/Bills/" + self.file_name.replace(".", "_") + "_MFW" + ".txt"
        with open(file_path, "w", encoding="utf-8") as file:
            for key, value in self.most_frequent_words.items():
                line = f"{key}: {value}\n"
                file.write(line)
        print(
            f"+ The most used words are written to a file along the path {file_path}\n"
        )

    def create_wordcloud(self, h: int = 1920, w: int = 1080, colors=None) -> WordCloud:
        """Создание облака;
        self.wordcloud"""
        if colors is None:
            colors = self.colors
        result = WordCloud(width=w, height=h, font_step=10, colormap=colors)
        result = result.generate_from_frequencies(self.most_frequent_words)
        return result

    def create_file_of_wordcloud(self):
        """Сохранение облака в виде файла с изображением"""
        # file_path = "Result/Clouds/" + str(self.file_name).replace(".", "_") + "_WC.png"
        self.wordcloud.to_file("Result/Clouds/wordcloud.png")


if __name__ == "__main__":
    DISH_PATH = "/Users/vessel/PycharmProjects/text_chewer_project/text_chewer/chewer/Dishes/text.fb2"
    app = TheChewer(file_path=DISH_PATH, words_quantity=10, width=1920, height=2080)
    app.create_file_of_wordcloud()
    app.toggle_copying = "on"

    if app.toggle_copying == "on":
        pyperclip.copy(app.content)  # перенести в класс
