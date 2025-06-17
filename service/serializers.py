from rest_framework import serializers
from .models import ServiceBody,ServiceHeader,MetaTagsService

class ServiceHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceHeader
        fields = "__all__"

class ServiceBodySerializer(serializers.ModelSerializer):
    service_header_body = ServiceHeaderSerializer(many=True, read_only=True)

    class Meta:
        model = ServiceBody
        fields = "__all__"

class MetaTagsServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaTagsService
        fields = "__all__"