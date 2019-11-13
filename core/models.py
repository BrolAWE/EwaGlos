from django.db import models

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
    name = models.CharField(max_length=100, unique=True)
    colour = models.CharField(max_length=10, default=None, help_text="Please use the following format: <em>#00FF00</em>.")


class Subsection(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    colour = models.CharField(max_length=10, help_text="Please use the following format: <em>#00FF00</em>.")


class Word(models.Model):
    subsection = models.ForeignKey(Subsection, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    definition = models.TextField()
    comment = models.TextField()


class WordTranslation(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    language = models.CharField(max_length=10, unique=True, choices=LANG)
    name = models.CharField(max_length=300, primary_key=True)
    definition = models.TextField()
    comment = models.TextField()


class SectionTranslation(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    language = models.CharField(max_length=10, unique=True, choices=LANG)
    name = models.CharField(max_length=100, primary_key=True)


class SubsectionTranslation(models.Model):
    subsection = models.ForeignKey(Subsection, on_delete=models.CASCADE)
    language = models.CharField(max_length=10, unique=True, choices=LANG)
    name = models.CharField(max_length=100, primary_key=True)
