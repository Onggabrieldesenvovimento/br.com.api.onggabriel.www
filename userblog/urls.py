from django.urls import path
from .views import BlogCreateListView, CategoryCreateListView, PostScheduleCreateListView, MediaBlogCreateListView

urlpatterns = [
    path('posts/', BlogCreateListView.as_view(), name='blogs-create-list'),
    path('categories/', CategoryCreateListView.as_view(), name='categories-create-list'),
    path('postschedule/', PostScheduleCreateListView.as_view(), name='postschedule-create-list'),
    path('media/', MediaBlogCreateListView.as_view(), name='media-create-list'),
]



