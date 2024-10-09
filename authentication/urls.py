from django.urls import path
from .views import CustomUserCreateListView


urlpatterns = [
    path('user/', CustomUserCreateListView.as_view(), name='user-create-list'),
] 
