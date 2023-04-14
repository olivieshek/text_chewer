from django import forms  # pip3 install Django
# from multiselectfield import MultiSelectField  # pip3 install django-multiselectfield


class AnalyserForm(forms.Form):
    """
    1 - выбираем откуда берем текст (файл или паста)
    TODO: текст - поле для текста
    --
    TODO: поле для файла для результата
    --
    # FIXME: не отправлять формы с пустыми частями речи
    # не получается через required, if - костыль!
    """
    dest_file = forms.FileField(
        label="Путь к файлу с текстом:",
    )  # dish file

    # FIXME: СДЕЛАЙ ЧТО НИБУДЬ УЖЕ С ФОРМОЙ ФАЙЛА, НАДО ПОЛУЧАТЬ ПУТЬ А НЕ ФАЙЛ!!!!!!

    # parts of speech list; field
    parts_of_speech = (
        ("NOUN", "существительные"),
        ("ADJF", "полные прилагательные"),
        ("ADJS", "краткие прилагательные"),
        ("COMP", "компаратив"),
        ("VERB", "глаголы (личная форма)"),
        ("INFN", "инфинитивы глаголов"),
        ("PRTF", "полные причастия"),
        ("PRTS", "краткие причастия"),
        ("GRND", "деепричастия"),
        ("NUMR", "числительные"),
        ("ADVB", "наречия"),
        ("NPRO", "местоимения"),
        ("PRED", "предикативы"),
        ("PREP", "предлоги"),
        ("CONJ", "союзы"),
        ("PRCL", "частицы"),
        ("INTJ", "междометия")
    )  # list

    parts_of_speech_field = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=parts_of_speech
    )  # field

    words_quantity = forms.IntegerField(
        label="Количество слов в облаке:",
        min_value=1,
        max_value=100,
        required=True
    )  # words_num
