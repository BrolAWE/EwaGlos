from rest_framework import serializers

from core.models import Section, WordTranslation, SectionTranslation, Subsection, Synonym, CloseSenseWord, Word


class SectionTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionTranslation
        fields = ['language', 'name']


class SectionSerializer(serializers.ModelSerializer):
    translations = SectionTranslationSerializer(many=True, read_only=True)

    class Meta:
        model = Section
        fields = ['code', 'color', 'translations']


class SubsectionTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionTranslation
        fields = ['language', 'name']


class SubsectionSerializer(serializers.ModelSerializer):
    translations = SubsectionTranslationSerializer(many=True, read_only=True)

    class Meta:
        model = Subsection
        fields = ['code', 'color', 'translations']


class SynonymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Synonym
        fields = ['synonym']


class WordTranslationSerializer(serializers.ModelSerializer):
    synonyms = SynonymSerializer(many=True, read_only=True)

    class Meta:
        model = WordTranslation
        fields = ['language', 'name', 'definition', 'comment', 'image_description', 'synonyms']


class CloseSenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CloseSenseWord
        fields = ['close_sense']


class WordSerializer(serializers.ModelSerializer):
    translations = WordTranslationSerializer(many=True, read_only=True)
    close_senses = CloseSenseSerializer(many=True, read_only=True)

    class Meta:
        model = Word
        fields = ['code', 'image', 'translations', 'close_senses']
