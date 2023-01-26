from rest_framework import serializers


class PostSerializer(serializers.Serializer):
    file = serializers.FileField()
