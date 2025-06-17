from django.urls import path
from .views import BlogCategoryListCreateAPIView,BlogCategoryRetrieveUpdateDestroyAPIView,BlogsListCreateAPIView,BlogsRetrieveUpdateDestroyAPIView,MetaTagsBlogListCreateAPIView,MetaTagsBlogRetrieveUpdateDestroyAPIView,BlogHeadingListCreateAPIView,BlogHeadingRetrieveUpdateDestroyAPIView,BlogInnerPageListCreateAPIView,BlogInnerPageRetrieveUpdateDestroyAPIView

urlpatterns =[
    path('blog-category/',BlogCategoryListCreateAPIView.as_view(),name= "blog-category-list-create"),
    path('blog-category/<int:pk>/',BlogCategoryRetrieveUpdateDestroyAPIView.as_view(),name= "blog-category-retrieve-update-destroy"),
    path('blogs/',BlogsListCreateAPIView.as_view(),name="blogd-list-create"),
    path('blogs/<int:pk>/',BlogsRetrieveUpdateDestroyAPIView.as_view(),name="blogs-retrieve-update-destroy"),
    path('blogmeta/',MetaTagsBlogListCreateAPIView.as_view(),name="metablog-list-create"),
    path('blogmeta/<int:pk>/',MetaTagsBlogRetrieveUpdateDestroyAPIView.as_view(),name="metablog-retrieve-update-destroy"),
    path('blog-heading/',BlogHeadingListCreateAPIView.as_view(),name="blog-heading-list-create"),
    path('blog-heading/<int:pk>/',BlogHeadingRetrieveUpdateDestroyAPIView.as_view(),name="blog-heading-retrieve-update-destroy"),
    path('blog-inner/',BlogInnerPageListCreateAPIView.as_view(),name="blog-inner-list-create"),
    path('blog-inner/<int:pk>/',BlogInnerPageRetrieveUpdateDestroyAPIView.as_view(),name="blog-inner-retrieve-update-destroy")
]