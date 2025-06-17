from django.shortcuts import render
from rest_framework import generics
from .models import BlogCategory,Blogs,BlogHeading,MetaTagsBlog,BlogInnerPage
from .serializers import BlogCategorySerializer,BlogsSerializer,BlogHeadingSerializer,MetaTagsBlogSerializer,BlogInnerPageSerializer
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

class BlogCategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer
    pagination_class = CustomPagination

class BlogCategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer

class BlogHeadingListCreateAPIView(generics.ListCreateAPIView):
    queryset = BlogHeading.objects.all()
    serializer_class = BlogHeadingSerializer

class BlogHeadingRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogHeading.objects.all()
    serializer_class = BlogHeadingSerializer

class BlogsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerializer
    pagination_class = CustomPagination

class BlogsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerializer

class BlogInnerPageListCreateAPIView(generics.ListCreateAPIView):
    queryset = BlogInnerPage.objects.all()
    serializer_class = BlogInnerPageSerializer
    pagination_class = CustomPagination

class BlogInnerPageRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogInnerPage.objects.all()
    serializer_class = BlogInnerPageSerializer

class MetaTagsBlogListCreateAPIView(generics.ListCreateAPIView):
    queryset = MetaTagsBlog.objects.all()
    serializer_class = MetaTagsBlogSerializer

class MetaTagsBlogRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MetaTagsBlog.objects.all()
    serializer_class =MetaTagsBlogSerializer
    