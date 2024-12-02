from django.urls import path
from .views import PostCreateListView, CategoryCreateListView, PostRetrieverUpdateView, PostScheduleCreateListView, MediaPostCreateListView

urlpatterns = [
    path('posts/', PostCreateListView.as_view(), name='post-create-list'),
    path('posts/<uuid:pk>', PostRetrieverUpdateView.as_view(), name='post-update'),
    path('category/', CategoryCreateListView.as_view(), name='categories-create-list'),
    path('postschedule/', PostScheduleCreateListView.as_view(), name='postschedule-create-list'),
    path('media/', MediaPostCreateListView.as_view(), name='media-create-list'),
]



