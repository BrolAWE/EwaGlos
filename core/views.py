from django.http import Http404
from django.shortcuts import render

# Create your views here.
from core.models import *


def word(request, pk, lan):
    try:
        word = Word.objects.get(pk=pk)
        subsection = Subsection.objects.get(pk=word.subsection.pk)
        section = Section.objects.get(pk=subsection.section.pk)
        word_translation = WordTranslation.objects.get(word=pk, language=lan)
        word_translations = WordTranslation.objects.filter(word=pk).exclude(language=lan).exclude(language="EN")
    except Word.DoesNotExist:
        raise Http404
    return render(request, 'word.html', context={
        'word': word,
        'subsection': subsection,
        'section': section,
        'word_translation': word_translation,
        'word_translations': word_translations
    })


def index(request):
    sections = Section.objects.all()
    return render(request, 'index.html', context={
        'sections': sections,
    })


def section(request, pk):
    subsections = Subsection.objects.filter(section=pk)
    return render(request, 'section.html', context={
        'subsections': subsections,
    })


def subsection(request, pk):
    words = Word.objects.filter(subsection=pk)
    return render(request, 'subsection.html', context={
        'words': words,
    })
