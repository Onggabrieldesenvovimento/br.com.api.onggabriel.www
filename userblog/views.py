from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import Post, Category, PostSchedule, MediaPost
from .serializers import PostSerializer, CategorySerializer, PostScheduleSerializer, MediaPostSerializer
from .filters import PostFilter


class PostCreateListView(generics.ListCreateAPIView):
    queryset = Post.objects.filter(state_type = 'active').all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostFilter

class PostRetrieverUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CategoryCreateListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostScheduleCreateListView(generics.ListCreateAPIView):
    queryset = PostSchedule.objects.all()
    serializer_class = PostScheduleSerializer

    def perform_create(self, serializer):
        serializer.save()

class MediaPostCreateListView(generics.ListCreateAPIView):
    queryset = MediaPost.objects.all()
    serializer_class = MediaPostSerializer
    