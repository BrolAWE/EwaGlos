from rest_framework import serializers


class SectionSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=100)
    color = serializers.CharField(max_length=7)


class SubsectionSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=100)
    color = serializers.CharField(max_length=7)


class WordSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=100)
    image = serializers.CharField(max_length=100)
