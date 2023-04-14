import re  # разбирем строку на отдельные слова
from docx import Document  # pip install python-docx
from bs4 import BeautifulSoup  # прасинг xml
import pymorphy2  # нормализация частей речи
from collections import Counter  # считаем самые частые слова
from wordcloud import WordCloud  # pip install wordcloud
from charset_normalizer import from_path  # нормализуем кодировку


class Analyser:
    # Все аргументы в конструктор класса!
    def __init__(
        self,
        source_file_path="",
        parts_of_speech=[],
        words_num=10,
        dest_file_path=""
    ):
        self.source_file_path = source_file_path

        
        self.make_text_from_file()
        self.make_words_from_text()
        self.make_normalized_words("NOUN", "VERB")
        self.make_most_frequent_words(5)
        self.make_wordcloud()
        self.save_wordcloud_to_file()  # пробросить путь к файлу

    def make_text_from_file(self):  # неточное название
        """
        определяет расширение текстового файла,
        вызывает соответствуйющий метод для типов TXT, DOCX, FB2
        """
        if self.file_path.endswith(".txt"):
            self.make_text_from_txt()
        elif self.file_path.endswith(".docx"):
            self.make_text_from_docx()
        elif self.file_path.endswith(".fb2"):
            self.make_text_from_fb2()
        else:
            # прервать выполнение при пустой строке
            print("Тип файла не определен. Завершение работы.")  # exception

    def make_text_from_txt(self):
        """
        Делает строку из TXT
        """
        self.content = str(from_path(self.file_path).best())

    def make_text_from_docx(self):
        """
        Делает строку из DOCX
        """
        file = Document(self.file_path)
        self.content = " ".join([p.text for p in file.paragraphs])

    def make_text_from_fb2(self):
        """
        Делает строку из FB2
        """
        with open(self.file_path, 'rb') as f:
            data = f.read()
        bs_data = BeautifulSoup(data, "xml")
        sections = bs_data.find_all('section')
        self.content = " ".join([s.text for s in sections])

    def make_words_from_text(self):
        """
        Создает список русских слов со строчной буквы без знаков препинания
        """
        self.words = re.findall("[а-яё]+", self.content.lower())

    def make_normalized_words(self, *parts_of_speech):
        """
        Создает список нормальных форм слов
        для определенных в part_of_speech частей речи.
        https://pymorphy2.readthedocs.io/en/stable/user/grammemes.html#grammeme-docs
        """
        morph = pymorphy2.MorphAnalyzer()
        self.normalized_words = []
        for word in self.words:
            parse = morph.parse(word)[0]
            for part in parts_of_speech:
                if part in parse.tag:
                    self.normalized_words.append(parse.normal_form)

    def make_most_frequent_words(self, num=10):
        """
        Создает словарь длинной num из самых частых слов по убыванию частоты
        слово: частота
        """
        self.most_frequent_words = dict(Counter(
            self.normalized_words).most_common(num))
        
    def make_wordcloud(
        self,
        width=1920,
        height=1024,
        bgcolor="black"
    ):
        """
        Создает объект Wordcloud из словаря self.most_frequent_words
        """
        self.wordcloud = WordCloud(
            width=width,
            height=height,
            background_color=bgcolor
        )
        self.wordcloud = self.wordcloud.generate_from_frequencies(
            self.most_frequent_words
        )

    def save_wordcloud_to_file(self):
        """
        сохраняет Wordcloud в файл filename
        """
        file_path = r"C:\Users\DDT\Desktop\frequency_analyser_new-main\wordcloud.png"
        self.wordcloud.to_file(file_path)
        print("Done!")


if __name__ == "__main__":
    analyser = Analyser()