from django.shortcuts import render
from rest_framework import generics
from .serializers import ContactSerializer,MetaTagsContactSerializer
from .models import Contact,MetaTagsContact

class ContactListCreateAPIView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class MetaTagsContactlistCreateAPIView(generics.ListCreateAPIView):
    queryset = MetaTagsContact.objects.all()
    serializer_class = MetaTagsContactSerializer

class MetaTagsContactRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MetaTagsContact.objects.all()
    serializer_class = MetaTagsContactSerializer