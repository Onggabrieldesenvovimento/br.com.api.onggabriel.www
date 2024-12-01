from django.contrib import admin
from .models import Post, Category, PostSchedule, MediaPost
from django.http import HttpResponse
import csv

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'published')
    search_fields = ('id', 'title', 'category__title', 'published')
    list_filter = ('title','category__title', 'published')

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="postagens.csv"'
        writer = csv.writer(response)
        writer.writerow(['Título', 'Conteúdo', 'Categoria', 'Qtd. Curtidas', 'Qtd. Visualização', 'Data de Criação','Data de Publicação', 'Publicado'])
        for post in queryset:
            writer.writerow([post.title, post.content, post.category, post.likes, post.views, post.created_at, post.published_at, post.published])

        return response
    export_to_csv.short_description = 'Exportar para CSV'
    actions = [export_to_csv]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'created_at')
    list_filter = ('title','created_at')

@admin.register(PostSchedule)
class PostScheduleAdmin(admin.ModelAdmin):
    list_display = ('post__title','scheduled_at', 'status')
    search_fields = ('post__title', 'scheduled_at', 'status')
    list_filter = ('post__title', 'scheduled_at', 'status')
    
admin.site.register(MediaPost)

