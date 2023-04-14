import sys  # system module
from PyQt6 import QtWidgets, uic
from text_chewer import the_chewer  # app class import


class app_interface(QtWidgets.QMainWindow):
    """Class of App Interface"""

    def __init__(self):
        super(app_interface, self).__init__()

        # Загрузка интерфейса программы
        uic.loadUi("text_chewer_interface.ui", self)
        self.show()

        self.file_path = str()
        # Выбор пути к файлу
        self.file_path = self.dish_path_btn.clicked.connect(self.select_file)

        self.text = str()
        if not self.file_path:
            # Забираем текст
            self.text = self.dish_text.toPlainText()
            self.dish_text.setReadOnly(True)

        # Части речи
        self.parts_of_speech = list()
        pofs_checkboxes = (self.NOUN, self.ADJF, self.ADJS, self.VERB, self.INFN)
        if self.all_pofs_checkbox.isChecked():
            for chb in pofs_checkboxes:
                chb.setCheckable(False)
            self.parts_of_speech.append("ALL")
        else:
            for chb in pofs_checkboxes:
                self.parts_of_speech.append(chb.objectName())

        # Получаем количество слов
        self.words = self.words_.value()

        # Получаем высоту изображения
        self.wc_height = self.height_.value()

        # Получаем ширину изображения
        self.wc_width = self.width_.value()

        # Подтверждение копирования в буфер обмена
        self.toggle_copying = (
            "on" if self.toggle_copying_checkbox.isChecked() else "off"
        )

        # Завершение
        self.ready_btn.clicked.connect(self.run)

    def select_file(self):
        """Вызов диалога выбора файла"""
        file_path = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Choose the file path.",
            sys.argv[0],
            "Text files (*.txt, *.fb2, *.docx)",
        )
        return file_path

    def run(self):
        self.app = the_chewer()
        self.app.file_path = self.file_path
        if self.text:
            self.app.content = self.text
        self.app.parts_of_speech = self.parts_of_speech
        self.app.top = self.words
        self.app.height_ = self.wc_height
        self.app.width_ = self.wc_width
        self.app.toggle_copying = self.toggle_copying
