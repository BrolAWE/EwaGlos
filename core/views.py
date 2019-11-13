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
    except Word.DoesNotExist:
        raise Http404
    return render(request, lan.lower()+'.html', context={
        'word': word,
        'subsection': subsection,
        'section': section,
        'word_translation': word_translation
    })
