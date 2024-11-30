import os
from django.db import models
from authentication.models import CustomUser
from uuid import uuid4
import hashlib
from django.utils import timezone

"""Classe das Categorias do Blog"""
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title.upper()} - {self.created_at}"


"""Classe principal do Blog"""
class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user_id = models.ForeignKey(CustomUser, related_name='blog_users' , on_delete=models.PROTECT)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    description = models.TextField()
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)  
    published_at = models.DateTimeField(null=True, blank=True) 

    def __str__(self):
        return f"{self.title.upper()} - {self.created_at}"

    """Função para publicar o post"""
    def publish(self):
        self.published = True
        self.published_at = timezone.now()
        self.save()

    """Função para agendar a publicação do post"""
    def schedule(self, schedule_time):
        self.published = False 
        self.published_at = schedule_time
        self.save()


"""Classe resnponsável por agendar a publicação de um post"""
class PostSchedule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    blog = models.OneToOneField(Blog, related_name="schedule", on_delete=models.CASCADE)
    scheduled_at = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[('scheduled', 'Scheduled'), ('published', 'Published')], default='scheduled')
    
    def __str__(self):
        return f"Agendamento para {self.blog.title} em {self.scheduled_at}"

    """Função para publicar o post e alterar o status do agendamento"""
    def publish(self):
        self.blog.publish() 
        self.status = 'published' 
        self.save()


"""Função responsável por criptografar e salvar os arquivos no servidor"""
def upload_media(instance, filename):
    instance_id = instance.id or uuid4().hex
    hash_instance = hashlib.sha256(str(instance_id).encode())
    
    _, ext = os.path.splitext(filename)
    sanitized_filename = hash_instance.hexdigest() + ext 
    return f"blog/{sanitized_filename}"


"""Classe responsável por armazenar os arquivos do blog"""
class MediaBlog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    MEDIA_TYPES = (
        ('image', 'Image'),
        ('video', 'Video'),
    )

    blog = models.ForeignKey(Blog, related_name='media', on_delete=models.CASCADE)
    file = models.FileField(upload_to=upload_media)
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    description = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return f"{self.media_type} - {self.blog.title}"