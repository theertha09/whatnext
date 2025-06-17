from django.shortcuts import render
from rest_framework import generics
from .models import VoiceOfSuccess,StudentReview,MetaTagsHome
from .serializers import VoiceOfSuccessSerializer,StudentReviewSerializer,MetaTagsHomeSerializer

class VoiceOfSuccessListCreateAPIView(generics.ListCreateAPIView):
    queryset = VoiceOfSuccess.objects.all()
    serializer_class = VoiceOfSuccessSerializer

class VoiceOfSuccessListView(generics.ListAPIView):
    queryset = VoiceOfSuccess.objects.order_by('order')
    serializer_class = VoiceOfSuccessSerializer

class VoiceOfSuccessRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VoiceOfSuccess.objects.all()
    serializer_class = VoiceOfSuccessSerializer

class StudentReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = StudentReview.objects.all()
    serializer_class = StudentReviewSerializer

class StudentReviewRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentReview.objects.all()
    serializer_class = StudentReviewSerializer

class MetaTagsHomeListCreateAPIView(generics.ListCreateAPIView):
    queryset = MetaTagsHome.objects.all()
    serializer_class = MetaTagsHomeSerializer

class MetaTagsHomeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MetaTagsHome.objects.all()
    serializer_class = MetaTagsHomeSerializer
    