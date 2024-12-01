import os
from django.db import models
from authentication.models import CustomUser
from uuid import uuid4
import hashlib
from django.utils import timezone

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, verbose_name='ID')
    title = models.CharField(max_length=255, verbose_name='Título')
    description = models.TextField(verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última atualização')

    class Meta:
        ordering = ['title', 'created_at'] 
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias' 
           
    def __str__(self):
        return f"{self.title.upper()}"

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, verbose_name='ID')
    user_id = models.ForeignKey(CustomUser, related_name='blog_users' , on_delete=models.PROTECT, verbose_name='ID do usuário')
    category = models.ManyToManyField(Category, related_name='posts', verbose_name='Categorias')
    title = models.CharField(max_length=255, verbose_name='Título')
    description = models.TextField(verbose_name='DEscrição')
    content = models.TextField(verbose_name='Conteúdo')
    likes = models.IntegerField(default=0, verbose_name='Curtidas')
    views = models.IntegerField(default=0, verbose_name='Visualisações')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última atualização')
    published = models.BooleanField(default=False, verbose_name='Publicado')  
    published_at = models.DateTimeField(null=True, blank=True, verbose_name='Data de publicação') 

    class Meta:
        ordering = ['title', 'created_at', 'published']
        verbose_name = 'Publicação'
        verbose_name_plural = 'Publicações'

    def __str__(self):
        return f"{self.title.upper()} - {self.created_at}"

    def publish(self):
        self.published = True
        self.published_at = timezone.now()
        self.save()

    def schedule(self, schedule_time):
        self.published = False 
        self.published_at = schedule_time
        self.save()

class PostSchedule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, verbose_name='ID')
    post = models.OneToOneField(Post, related_name="schedule", on_delete=models.CASCADE, verbose_name='ID do agendamento')
    scheduled_at = models.DateTimeField(verbose_name='Data de publicação')
    status = models.CharField(max_length=20, choices=[('scheduled', 'Scheduled'), ('published', 'Published')], default='scheduled', verbose_name='Status do agendamento')
    
    class Meta:
        ordering = ['post__title', 'scheduled_at', 'status']
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'

    def __str__(self):
        return f"Agendamento para {self.blog.title} em {self.scheduled_at}"

    def publish(self):
        self.blog.publish() 
        self.status = 'published' 
        self.save()

def upload_media(instance, filename):
    instance_id = instance.id or uuid4().hex
    hash_instance = hashlib.sha256(str(instance_id).encode())
    
    _, ext = os.path.splitext(filename)
    sanitized_filename = hash_instance.hexdigest() + ext 
    return f"blog/{sanitized_filename}"

class MediaPost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, verbose_name='ID')
    MEDIA_TYPES = (
        ('image', 'Image'),
        ('video', 'Video'),
    )

    post = models.ForeignKey(Post, related_name='media', on_delete=models.CASCADE, verbose_name='ID da publicação')
    file = models.FileField(upload_to=upload_media, verbose_name='Arquivo')
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES, verbose_name='Tipo de mídia')
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name='Descrição')

    class Meta:
        ordering = ['post__title', 'media_type', 'file']
        verbose_name = 'Mídia'
        verbose_name_plural = 'Mídias'

    def __str__(self):
        return f"{self.media_type} - {self.blog.title}"