from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('boards/<int:id>', views.board_topics, name='board_topics'),
]