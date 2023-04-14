"""Text-Chewer program"""
import re  # разбираем строку на отдельные слова
from collections import Counter  # ищем часто используемые слова, счетчик объектов
from charset_normalizer import from_path  # pip3 install charset-normalizer
from bs4 import BeautifulSoup  # pip3 install bs4
from docx import Document  # pip3 install docx
import pyperclip  # pip3 install pyperclip
import pymorphy2  # pip3 install pymorphy2; pip3 install pymorphy2-dicts
from wordcloud import WordCloud  # pip3 install wordcloud


class the_chewer:
    """Класс приложения"""

    def __init__(self, file_path: str, toggle_copying="off"):
        """Инициализация объекта класса приложения"""
        self.toggle_copying = (
            toggle_copying  # вкл/выкл копирования текста в буфер обмена
        )

        self.file_path = file_path

        self.file_name = (
            re.search(r"/\w+\.\w+$", self.file_path).group().replace("/", "")
        )
        self.file_extension = re.search(r"\.\w+$", file_path).group()

        self.content = str(from_path(self.file_path).best())  # нормализация кодировки
        self.content = self.make_text_from_file()

        self.words = self.write_all_words(self.content)
        self.infinitive_words = self.write_infinitives(parts_of_speech=["NOUN"])
        self.most_frequent_words = self.write_most_frequent_words()

        self.wordcloud = self.create_wordcloud(self.most_frequent_words)

    def make_text_from_file(self) -> str:
        """Проверка расширение файла, достаем текст;
        self.content"""
        if self.file_name.endswith(".txt"):
            content = self.make_text_from_txt()
        elif self.file_name.endswith(".fb2"):
            content = self.make_text_from_fb2()
        elif self.file_name.endswith(".docx"):
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

    def write_all_words(self, text: str) -> list:
        """Создание списка всех слов текста;
        self.words"""
        words = re.findall(r"[а-яё0-9]+", text.lower())
        return words

    def write_infinitives(self, parts_of_speech: list[str] = ("NOUN", "VERB")) -> list:
        """Создание списка инфинитивных форм
        слов из текста определенных частей речи;
        self.infinitive_words"""
        if len(parts_of_speech) == 1 and parts_of_speech[0] == "ALL":
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

    def write_most_frequent_words(self, top: int = 10) -> dict:
        """Создание списка наиболее используемых слов;
        self.most_frequent_words"""
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

    def create_wordcloud(self, text: str) -> WordCloud:
        """Создание облака;
        self.wordcloud"""
        result = WordCloud(width=1920, height=1080, font_step=10, colormap="Greys")
        result = result.generate_from_frequencies(text)
        return result

    def create_file_of_wordcloud(self):
        """Сохранение облака в виде файла с изображением"""
        file_path = "Result/Clouds/" + self.file_name.replace(".", "_") + "_WC.png"
        self.wordcloud.to_file(file_path)


if __name__ == "__main__":
    DISH_PATH = "Dishes/test.docx"
    app = the_chewer(DISH_PATH)

    if app.toggle_copying == "on":
        pyperclip.copy(app.content)
