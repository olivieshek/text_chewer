from PySide2 import QtCore, QtGui, QtWidgets  # pip3 install PySide2


class Ui_ApplicationWindow(object):
    """Class of the PyQt Window of the Application"""

    def setupUi(self, ApplicationWindow):
        ApplicationWindow.setObjectName("ApplicationWindow")
        ApplicationWindow.resize(500, 710)
        ApplicationWindow.setMinimumSize(QtCore.QSize(500, 710))
        ApplicationWindow.setAutoFillBackground(True)
        ApplicationWindow.setStyleSheet(background_color="#AABDBA")

        self.centralwidget = QtWidgets.QWidget(ApplicationWindow)

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 461, 131))

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setVerticalSpacing(0)

        self.dish_path = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.dish_path.setStyleSheet('font: 13pt "Courier New";')
        self.dish_path.setObjectName("dish_path")

        self.gridLayout.addWidget(self.dish_path, 1, 0, 1, 1)

        self.dish_text = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.dish_text.setStyleSheet(
            'background-color: "#E0E7E5"; border: 2px solid rgb(119, 140, 125);'
        )
        self.dish_text.setObjectName("dish_text")
        self.gridLayout.addWidget(self.dish_text, 0, 0, 1, 1)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 630, 461, 51))
        self.pushButton.setStyleSheet(
            "background-color: rgb(129, 162, 166);\n" 'font: bold 14.5pt "Courier New";'
        )
        self.pushButton.setObjectName("pushButton")

        self.wordcloud_settings_frame = QtWidgets.QFrame(self.centralwidget)
        self.wordcloud_settings_frame.setGeometry(QtCore.QRect(20, 170, 461, 441))
        self.wordcloud_settings_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.wordcloud_settings_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.wordcloud_settings_frame.setObjectName("wordcloud_settings_frame")

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.wordcloud_settings_frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 230, 461, 211))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")

        self.wordcloud_settings = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.wordcloud_settings.setContentsMargins(0, 0, 0, 0)
        self.wordcloud_settings.setSpacing(0)
        self.wordcloud_settings.setObjectName("wordcloud_settings")

        self.words_layout = QtWidgets.QHBoxLayout()
        self.words_layout.setObjectName("words_layout")

        self.words_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.words_label.setStyleSheet(
            'font: 13pt "Courier New"; background-color: "#B7C1BF";'
        )
        self.words_label.setObjectName("words_label")

        self.words_layout.addWidget(self.words_label)

        self.words = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.words.setStyleSheet('background-color: "#CCD3D2";')
        self.words.setMinimum(1)
        self.words.setMaximum(1000)
        self.words.setProperty("value", 20)
        self.words.setDisplayIntegerBase(10)
        self.words.setObjectName("words")

        self.words_layout.addWidget(self.words)

        self.wordcloud_settings.addLayout(self.words_layout)

        self.height_layout = QtWidgets.QHBoxLayout()
        self.height_layout.setObjectName("height_layout")

        self.height_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.height_label.setStyleSheet(
            'font: 13pt "Courier New"; background-color: "#B7C1BF";'
        )
        self.height_label.setObjectName("height_label")

        self.height_layout.addWidget(self.height_label)

        self.height = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.height.setStyleSheet('background-color: "#CCD3D2";')
        self.height.setMinimum(1)
        self.height.setMaximum(5000)
        self.height.setProperty("value", 1000)
        self.height.setDisplayIntegerBase(10)
        self.height.setObjectName("height")

        self.height_layout.addWidget(self.height)

        self.wordcloud_settings.addLayout(self.height_layout)

        self.width_layout = QtWidgets.QHBoxLayout()
        self.width_layout.setObjectName("width_layout")

        self.width_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.width_label.setStyleSheet(
            'font: 13pt "Courier New"; background-color: "#B7C1BF";'
        )
        self.width_label.setObjectName("width_label")

        self.width_layout.addWidget(self.width_label)

        self.width = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.width.setStyleSheet('background-color: "#CCD3D2";')
        self.width.setMinimum(1)
        self.width.setMaximum(5000)
        self.width.setProperty("value", 1920)
        self.width.setDisplayIntegerBase(10)
        self.width.setObjectName("width")

        self.width_layout.addWidget(self.width)

        self.wordcloud_settings.addLayout(self.width_layout)

        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.wordcloud_settings_frame)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(1, 41, 459, 171))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")

        self.pofs_layout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.pofs_layout.setContentsMargins(0, 0, 0, 0)
        self.pofs_layout.setVerticalSpacing(4)
        self.pofs_layout.setObjectName("pofs_layout")

        self.pofs_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.pofs_label.setBaseSize(QtCore.QSize(0, 0))
        self.pofs_label.setAutoFillBackground(False)
        self.pofs_label.setStyleSheet(
            'font: 14pt "Courier New"; background-color: "#B7C1BF";'
        )
        self.pofs_label.setObjectName("pofs_label")

        self.pofs_layout.addWidget(self.pofs_label, 3, 0, 1, 1)

        self.pofs_checkboxes = QtWidgets.QVBoxLayout()
        self.pofs_checkboxes.setSpacing(14)
        self.pofs_checkboxes.setObjectName("pofs_checkboxes")
        self.nouns = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.nouns.setObjectName("nouns")
        self.pofs_checkboxes.addWidget(self.nouns)
        self.fulladj = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.fulladj.setObjectName("fulladj")
        self.pofs_checkboxes.addWidget(self.fulladj)
        self.shortadj = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.shortadj.setObjectName("shortadj")
        self.pofs_checkboxes.addWidget(self.shortadj)
        self.persverbs = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.persverbs.setObjectName("persverbs")
        self.pofs_checkboxes.addWidget(self.persverbs)
        self.infverbs = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.infverbs.setObjectName("infverbs")
        self.pofs_checkboxes.addWidget(self.infverbs)
        self.pofs_layout.addLayout(self.pofs_checkboxes, 4, 0, 1, 1)
        self.setup_label_layout = QtWidgets.QFrame(self.wordcloud_settings_frame)
        self.setup_label_layout.setGeometry(QtCore.QRect(1, 1, 461, 31))
        self.setup_label_layout.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setup_label_layout.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setup_label_layout.setObjectName("setup_label_layout")
        self.label = QtWidgets.QLabel(self.setup_label_layout)
        self.label.setGeometry(QtCore.QRect(150, 10, 171, 16))
        self.label.setStyleSheet('font: 15pt bold "Courier New";')
        self.label.setObjectName("label")
        ApplicationWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ApplicationWindow)
        QtCore.QMetaObject.connectSlotsByName(ApplicationWindow)

    def retranslateUi(self, ApplicationWindow):
        _translate = QtCore.QCoreApplication.translate
        ApplicationWindow.setWindowTitle(_translate("ApplicationWindow", "text chewer"))
        self.dish_path.setText(
            _translate("ApplicationWindow", "choose file\n" " path...")
        )
        self.pushButton.setText(_translate("ApplicationWindow", "ready"))
        self.words_label.setText(
            _translate("ApplicationWindow", "words in\n" "wordcloud")
        )
        self.height_label.setText(
            _translate("ApplicationWindow", "height of\n" "wordcloud")
        )
        self.width_label.setText(
            _translate("ApplicationWindow", "width of\n" "wordcloud")
        )
        self.pofs_label.setText(_translate("ApplicationWindow", "parts of speech:"))
        self.nouns.setText(_translate("ApplicationWindow", "nouns"))
        self.fulladj.setText(_translate("ApplicationWindow", "full adjectives"))
        self.shortadj.setText(_translate("ApplicationWindow", "short adjectives"))
        self.persverbs.setText(_translate("ApplicationWindow", "personal verbs"))
        self.infverbs.setText(_translate("ApplicationWindow", "infinitive verbs"))
        self.label.setText(_translate("ApplicationWindow", "set up your wordcloud:"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ApplicationWindow = QtWidgets.QMainWindow()
    ui = Ui_ApplicationWindow()
    ui.setupUi(ApplicationWindow)
    ApplicationWindow.show()
    sys.exit(app.exec_())
