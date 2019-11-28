from django.db.models import Q
from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import *
from core.serializers import WordSerializer, \
    SectionSerializer, SubsectionSerializer


def index(request, lang="RU"):
    return render(request, 'index1.html', context={
        'lang': lang,
    })


def about(request, lang):
    return render(request, 'about.html', context={
        'lang': lang,
    })


def sections(request, lang):
    sections = SectionTranslation.objects.filter(language=lang)
    return render(request, 'sections.html', context={
        'sections': sections,
        'lang': lang,
    })


def subsections(request, lang, pk):
    subsection = Subsection.objects.filter(section=pk)
    subsections = SubsectionTranslation.objects.filter(subsection__in=subsection.values_list("pk"), language=lang)
    return render(request, 'subsections.html', context={
        'pk': pk,
        'subsections': subsections,
        'lang': lang,
    })


def words(request, lang, pk):
    subsection = Subsection.objects.get(pk=pk)
    section = SectionTranslation.objects.get(section=subsection.section, language=lang)
    word = Word.objects.filter(subsection=pk)
    words = WordTranslation.objects.filter(word__in=word.values_list("pk"), language=lang)
    return render(request, 'words.html', context={
        'subsection': subsection,
        'words': words,
        'section': section,
        'lang': lang,
        'pk': pk,
    })


def word(request, lang, pk, lan):
    try:
        word = Word.objects.get(pk=pk)
        wordtrans = WordTranslation.objects.get(language=lang, word=pk)
        subsection = SubsectionTranslation.objects.get(subsection=word.subsection.pk, language=lang)
        section = SectionTranslation.objects.get(section=subsection.subsection.section.pk, language=lang)
        word_translation = WordTranslation.objects.get(word=pk, language=lan)
        word_translations = WordTranslation.objects.filter(word=pk).exclude(language=lan).exclude(language=lang)
        close_senses = CloseSenseWord.objects.filter(word=pk)
        close_sense_words = WordTranslation.objects.filter(
            word__in=close_senses.values_list("close_sense")).filter(language=lang)
        close_sense_translations = WordTranslation.objects.filter(
            word__in=close_senses.values_list("close_sense")).filter(language=lan)
    except Word.DoesNotExist:
        raise Http404
    return render(request, 'word.html', context={
        'lang': lang,
        'word': word,
        'wordtrans': wordtrans,
        'subsection': subsection,
        'section': section,
        'word_translation': word_translation,
        'word_translations': word_translations,
        'close_sense_words': close_sense_words,
        'close_sense_translations': close_sense_translations
    })


def search(request, lang):
    query = request.GET.get("q")
    synonyms = Synonym.objects.filter(Q(synonym__icontains=query))
    words = WordTranslation.objects.filter(Q(name__icontains=query) | Q(pk__in=synonyms.values_list("word")))
    return render(request, 'search.html', context={
        'words': words,
        'lang': lang,
    })


class SectionView(APIView):
    def get(self, request):
        sections = Section.objects.all()
        serializer = SectionSerializer(sections, many="True")
        return Response({"sections": serializer.data})


class SubsectionView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        subsections = Subsection.objects.filter(section=pk)
        serializer = SubsectionSerializer(subsections, many="True")
        return Response({"subsections": serializer.data})


class WordsView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        words = Word.objects.filter(subsection=pk)
        serializer = WordSerializer(words, many="True")
        return Response({"words": serializer.data})


class WordView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        word = Word.objects.get(code=pk)
        serializer = WordSerializer(word)
        return Response(serializer.data)
