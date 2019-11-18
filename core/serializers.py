from rest_framework import serializers


class SectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    color = serializers.CharField(max_length=7)


class SubsectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    color = serializers.CharField(max_length=7)