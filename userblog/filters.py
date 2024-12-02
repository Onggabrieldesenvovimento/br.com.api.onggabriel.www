import django_filters
from .models import Post

class PostFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'], 
            'description': ['icontains'],
            'content': ['icontains'],
            'category': ['exact'],
            'category__title': ['icontains'],
            'published_at': ['exact', 'gte', 'lte'],
            'published': ['exact'],
        }
