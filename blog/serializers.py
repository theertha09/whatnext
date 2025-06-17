from rest_framework import serializers
from .models import BlogCategory,Blogs,BlogHeading,MetaTagsBlog,BlogInnerPage
from datetime import datetime

class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = "__all__"

class BlogHeadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogHeading
        fields = "__all__"

class BlogsSerializer(serializers.ModelSerializer):
    blog_categories = BlogCategorySerializer(read_only=True)
    blog_headings = BlogHeadingSerializer(read_only=True)

    class Meta:
        model = Blogs
        fields = "__all__"
    

class BlogInnerPageSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='blog.title', read_only=True)
    author = serializers.CharField(source='blog.author', read_only=True)
    blog_image = serializers.ImageField(source='blog.blog_image', read_only=True)
    date = serializers.DateField(source='blog.date', read_only=True)
    time = serializers.TimeField(source='blog.time', read_only=True)
    blog_category = BlogCategorySerializer(source= 'blog.blog_category', read_only=True)

    class Meta:
        model = BlogInnerPage
        fields = ['id', 'blog', 'title', 'author', 'blog_image', 'date', 'time', 'blog_category','description','slug']


class MetaTagsBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaTagsBlog
        fields = "__all__"