from rest_framework import serializers
from django.utils import timezone
from .models import Blog, Category, PostSchedule, MediaBlog
from django.core.exceptions import ValidationError


class MediaBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaBlog
        fields = "__all__"

class BlogSerializer(serializers.ModelSerializer):
    media = MediaBlogSerializer(many=True, read_only=True) 
    class Meta:
        model = Blog
        fields = ['id', 'user_id', 'category', 'title', 'description', 'created_at', 'updated_at', 'published', 'published_at', 'media']

    #TODO: Adicionar os dados de ['likes', 'views'] na resposta da api
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class PostScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostSchedule
        fields = "__all__"

    # Validação para garantir que o agendamento não seja no passado
    def validate_scheduled_at(self, value):
        if value < timezone.now():
            raise ValidationError("A data de agendamento não pode ser no passado.")
        return value

    # Alternativamente, você pode usar o método `validate` para validar globalmente
    def validate(self, data):
        if data['scheduled_at'] < timezone.now():
            raise ValidationError("A data de agendamento não pode ser no passado.")
        return data

        