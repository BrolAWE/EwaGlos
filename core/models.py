from django.db import models
import cloudinary.models

# Create your models here.

LANG = (
    ('BG', 'Bulgarian'),
    ('DE', 'German'),
    ('EN', 'English'),
    ('ES', 'Spanish'),
    ('FR', 'French'),
    ('HR', 'Croatian'),
    ('HU', 'Hungarian'),
    ('IT', 'Italian'),
    ('RO', 'Romanian'),
    ('RU', 'Russian'),
    ('TR', 'Turkish')
)


class Section(models.Model):
    name = models.CharField(max_length=100, help_text="Пример зполнения: <em>Искусства и ремёсла</em>.",
                            verbose_name="Название раздела")
    color = models.CharField(max_length=7, help_text="Пример зполнения: <em>#00FF00</em>.", verbose_name="Цвет")

    def __str__(self):
        return "{0}, {1}".format(self.pk, self.name)

    class Meta:
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"


class Subsection(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, db_column="section",
                                verbose_name="Выбрать/добавить раздел")
    name = models.CharField(max_length=100, help_text="Пример зполнения: <em>Строительство</em>.",
                            verbose_name="Название подраздела")
    color = models.CharField(max_length=7, help_text="Пример зполнения: <em>#00FF00</em>. "
                                                     "Для большей информации используйте таблицу цветов HTML",
                             verbose_name="Цвет")

    def __str__(self):
        return "{0}, {1}".format(self.pk, self.name)

    class Meta:
        verbose_name = "Подраздел"
        verbose_name_plural = "Подразделы"


class Word(models.Model):
    subsection = models.ForeignKey(Subsection, on_delete=models.CASCADE, verbose_name="Выбрать/добавить подраздел")
    name = models.CharField(max_length=100, help_text="Пример заполнения 1: <em>Пещера</em>"
                                                      "<br>Пример заполнения 2: <em>камень-сырец/саман</em>",
                            verbose_name="Слово")
    image = cloudinary.models.CloudinaryField('картинка')

    def __str__(self):
        return "{0}, {1}".format(self.pk, self.name)

    class Meta:
        verbose_name = "Слово"
        verbose_name_plural = "Слова"


class WordTranslation(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE, verbose_name="Выбрать/добавить слово")
    language = models.CharField(max_length=2, choices=LANG, verbose_name="Выбрать язык")
    name = models.CharField(max_length=100, help_text="Напишите перевод слова на выбранном языке", verbose_name="Перевод")
    definition = models.TextField(help_text="Напишите определение слова на выбранном языке", verbose_name="Определение")
    comment = models.TextField(help_text="Напишите комментарий слова на выбранном языке", verbose_name="Комментарий")
    image_description = models.TextField(help_text="Пример заполнения: <em>объект изображения, время создания объекта, автор изображения,"
                                                   " время создания изображения</em>", verbose_name="Описание картинки")

    def __str__(self):
        return "{0}, {1}".format(self.pk, self.name)

    class Meta:
        verbose_name = "Перевод слова"
        verbose_name_plural = "Переводы слов"


class SectionTranslation(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name="Выбрать/добавить раздел")
    language = models.CharField(max_length=2, choices=LANG, verbose_name="Выбрать язык")
    name = models.CharField(max_length=100, help_text="Напишите перевод раздела на выбранном языке", verbose_name="Перевод")

    class Meta:
        verbose_name = "Перевод раздела"
        verbose_name_plural = "Переводы разделов"


class SubsectionTranslation(models.Model):
    subsection = models.ForeignKey(Subsection, on_delete=models.CASCADE, verbose_name="Выбрать/добавить подраздел")
    language = models.CharField(max_length=2, choices=LANG, verbose_name="Выбрать язык")
    name = models.CharField(max_length=100, help_text="Напишите перевод подраздела на выбранном языке", verbose_name="Перевод")

    class Meta:
        verbose_name = "Перевод подраздела"
        verbose_name_plural = "Переводы подразделов"


class CloseSenseWord(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE, help_text="Choose from the list the word",
                             related_name="word", verbose_name="Исходное слово")
    close_sense = models.ForeignKey(Word, on_delete=models.CASCADE,
                                    help_text="Choose from the list the close sense word", related_name="close_sense",
                                    verbose_name="Близкое по смыслу слово")

    def __str__(self):
        return "{0}, {1}".format(self.word, self.close_sense)


    class Meta:
        verbose_name = "Близкое по смыслу слово"
        verbose_name_plural = "Близкие по смыслу слова"
