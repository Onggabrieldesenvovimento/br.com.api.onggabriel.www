from django.contrib import admin
from .models import Blog, Category, PostSchedule, MediaBlog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'category', 'created_at')
    search_fields = ('id', 'title', 'category')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'created_at')
    search_fields = ('id', 'title')

@admin.register(PostSchedule)
class PostScheduleAdmin(admin.ModelAdmin):
    list_display = ('id','scheduled_at', 'status')
    search_fields = ('id', 'scheduled_at', 'status')

    
admin.site.register(MediaBlog)