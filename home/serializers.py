from rest_framework import serializers
from .models import VoiceOfSuccess,StudentReview,MetaTagsHome

class VoiceOfSuccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoiceOfSuccess
        fields = ['id', 'name', 'video', 'thumbnail', 'order','is_active']

class StudentReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentReview
        fields = '__all__'

class MetaTagsHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaTagsHome
        fields = "__all__"