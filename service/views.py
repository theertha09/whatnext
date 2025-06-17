from django.shortcuts import render
from rest_framework import generics
from .models import ServiceHeader,ServiceBody,MetaTagsService
from .serializers import ServiceHeaderSerializer,ServiceBodySerializer,MetaTagsServiceSerializer
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


class ServiceHeaderListCreateAPIView(generics.ListCreateAPIView):
    queryset = ServiceHeader.objects.all()
    serializer_class = ServiceHeaderSerializer
    pagination_class = CustomPagination

class ServiceHeaderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceHeader.objects.all()
    serializer_class = ServiceHeaderSerializer


class ServiceBodyListCreateAPIView(generics.ListCreateAPIView):
    queryset = ServiceBody.objects.all()
    serializer_class = ServiceBodySerializer
    pagination_class = CustomPagination

class ServiceBodyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceBody.objects.all()
    serializer_class = ServiceBodySerializer

class MetaTagsServiceListCreateAPIView(generics.ListCreateAPIView):
    queryset = MetaTagsService.objects.all()
    serializer_class = MetaTagsServiceSerializer

class MetaTagsServiceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MetaTagsService.objects.all()
    serializer_class = MetaTagsServiceSerializer
    