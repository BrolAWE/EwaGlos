from rest_framework import serializers

from core.models import Section, WordTranslation, SectionTranslation


class SectionTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionTranslation
        fields = ['language', 'name']


class SectionSerializer(serializers.ModelSerializer):
    translations = SectionTranslationSerializer(many=True, read_only=True)

    class Meta:
        model = Section
        fields = ['code', 'color', 'translations']


class SubsectionSerializer(serializers.Serializer):
    section = serializers.CharField(max_length=100)
    code = serializers.CharField(max_length=100)
    color = serializers.CharField(max_length=7)


class WordSerializer(serializers.Serializer):
    subsection = serializers.CharField(max_length=100)
    code = serializers.CharField(max_length=100)
    image = serializers.CharField(max_length=100)
