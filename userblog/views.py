from rest_framework import generics
from .models import Post, Category, PostSchedule, MediaPost
from .serializers import PostSerializer, CategorySerializer, PostScheduleSerializer, MediaPostSerializer
from rest_framework.response import Response
from rest_framework import status


class MediaPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaPost
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    media = MediaPostSerializer(many=True, read_only=True) 
    class Meta:
        model = Post
        fields = ['id', 'user_id', 'category', 'title', 'content', 'created_at', 'updated_at', 'published', 'published_at', 'media']

    #TODO: Adicionar os dados de ['likes', 'views'] na resposta da api
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class PostScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostSchedule
        fields = "__all__"

    def validate_scheduled_at(self, value):
        if value < timezone.now():
            raise ValidationError("A data de agendamento não pode ser no passado.")
        return value

    def validate(self, data):
        if data['scheduled_at'] < timezone.now():
            raise ValidationError("A data de agendamento não pode ser no passado.")
        return data

