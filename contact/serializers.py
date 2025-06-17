from rest_framework import serializers
from .models import Contact,MetaTagsContact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

class MetaTagsContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaTagsContact
        fields = "__all__"