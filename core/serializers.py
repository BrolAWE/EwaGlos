from rest_framework import serializers


class SectionSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=100)
    color = serializers.CharField(max_length=7)


class SubsectionSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=100)
    color = serializers.CharField(max_length=7)


class WordsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)


class WordSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    subsection = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100)
    definition = serializers.CharField(max_length=5000)
    comment = serializers.CharField(max_length=5000)
    image = serializers.CharField(max_length=5000)
    image_description = serializers.CharField(max_length=5000)
