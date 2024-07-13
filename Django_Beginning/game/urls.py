from django.urls import path
from . import views
from .views import Index

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница приложения
    path('game/', Index.as_view(), name='game'),
]
