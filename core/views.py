from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import *
from core.serializers import SectionSerializer


class SectionView(APIView):
    def get(self, request):
        sections = Section.objects.all()
        serializer = SectionSerializer(sections, many="True")
        return Response({"sections": serializer.data})


def word(request, pk, lan):
    try:
        word = Word.objects.get(pk=pk)
        subsection = Subsection.objects.get(pk=word.subsection.pk)
        section = Section.objects.get(pk=subsection.section.pk)
        word_translation = WordTranslation.objects.get(word=pk, language=lan)
        word_translations = WordTranslation.objects.filter(word=pk).exclude(language=lan).exclude(language="EN")
        close_senses = CloseSenseWord.objects.filter(word=pk)
        close_sense_words = Word.objects.filter(pk__in=close_senses.values_list("close_sense"))
        close_sense_translations = WordTranslation.objects.filter(
            word__in=close_senses.values_list("close_sense")).filter(language=lan)
    except Word.DoesNotExist:
        raise Http404
    return render(request, 'word.html', context={
        'word': word,
        'subsection': subsection,
        'section': section,
        'word_translation': word_translation,
        'word_translations': word_translations,
        'close_sense_words': close_sense_words,
        'close_sense_translations': close_sense_translations
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
    section = Section.objects.get(pk=pk)
    words = Word.objects.filter(subsection=pk)
    return render(request, 'subsection.html', context={
        'words': words,
        'section': section,
    })
