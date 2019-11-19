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
    name = models.CharField(max_length=100, help_text="Use the following format: <em>Name of the section</em>.")
    color = models.CharField(max_length=7, help_text="Use the following format: <em>#00FF00</em>.")

    def __str__(self):
        return "{0}, {1}".format(self.pk, self.name)


class Subsection(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, db_column="section")
    name = models.CharField(max_length=100, help_text="Use the following format: <em>Name of the subsection</em>.")
    color = models.CharField(max_length=7, help_text="Use the following format: <em>#00FF00</em>.")

    def __str__(self):
        return "{0}, {1}".format(self.pk, self.name)


class Word(models.Model):
    subsection = models.ForeignKey(Subsection, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, help_text="Use the following format: <em>Word</em>.")
    definition = models.TextField(help_text="Write down the whole definition.")
    comment = models.TextField(help_text="Write some notes about the exhibit in the picture")
    image = cloudinary.models.CloudinaryField('image', null=True)
    image_description = models.TextField(help_text="Write the description of the picture", null=True)

    def __str__(self):
        return "{0}, {1}".format(self.pk, self.name)


class WordTranslation(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    language = models.CharField(max_length=2, choices=LANG, help_text="Choose the language from the list")
    name = models.CharField(max_length=100, help_text="Write down the translation.")
    definition = models.TextField(help_text="Write down the whole definition.")
    comment = models.TextField(help_text="Write some notes about the exhibit in the picture")
    image_description = models.TextField(help_text="Write the description translation of the picture", null=True)

    def __str__(self):
        return "{0}, {1}".format(self.pk, self.name)


class SectionTranslation(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    language = models.CharField(max_length=2, choices=LANG)
    name = models.CharField(max_length=100)


class SubsectionTranslation(models.Model):
    subsection = models.ForeignKey(Subsection, on_delete=models.CASCADE)
    language = models.CharField(max_length=2, choices=LANG)
    name = models.CharField(max_length=100)


class CloseSenseWord(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE, help_text="Choose from the list the word", related_name="word")
    close_sense = models.ForeignKey(Word, on_delete=models.CASCADE,
                                    help_text="Choose from the list the close sense word", related_name="close_sense")

    def __str__(self):
        return "{0}, {1}".format(self.pk, self.name)
