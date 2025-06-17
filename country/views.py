from django.shortcuts import render
from rest_framework import generics
from .serializers import CountriesSerializer,UniversitySerializer,WhyChooseSerializer,MetaTagsCountrySerializer
from .models import Countries,University,WhyChoose,MetaTagsCountry
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size_query_param = 'limit'
    page_query_param = 'page'

    def get_paginated_response(self, data):
        return Response({
            "code": 200,
            "message": "",
            "data": data,
            "pagination": {
                "total": self.page.paginator.count,
                "page": self.page.number,
                "limit": self.get_page_size(self.request),
                "totalPages": self.page.paginator.num_pages
            }
        })

class CountriesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer
    pagination_class = CustomPagination

class CountriesRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer

class UniversityListCreateAPIView(generics.ListCreateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    pagination_class = CustomPagination

class UniversityRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

class WhyChooseListCreateAPIView(generics.ListCreateAPIView):
    queryset = WhyChoose.objects.all()
    serializer_class = WhyChooseSerializer
    pagination_class = CustomPagination

class WhyChooseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WhyChoose.objects.all()
    serializer_class = WhyChooseSerializer

class MetaTagsCountryListCreatAPIView(generics.ListCreateAPIView):
    queryset = MetaTagsCountry.objects.all()
    serializer_class = MetaTagsCountrySerializer

class MetaTagsCountryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MetaTagsCountry.objects.all()
    serializer_class = MetaTagsCountrySerializer