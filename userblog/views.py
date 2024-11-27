from rest_framework import generics
from .models import Blog, Category, PostSchedule, MediaBlog
from .serializers import BlogSerializer, CategorySerializer, PostScheduleSerializer, MediaBlogSerializer
from rest_framework.response import Response
from rest_framework import status


class BlogCreateListView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class CategoryCreateListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostScheduleCreateListView(generics.ListCreateAPIView):
    queryset = PostSchedule.objects.all()
    serializer_class = PostScheduleSerializer

    def perform_create(self, serializer):
        serializer.save()

class MediaBlogCreateListView(generics.ListCreateAPIView):
    queryset = MediaBlog.objects.all()
    serializer_class = MediaBlogSerializer
    