from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('boards/<int:board_id>/', views.boards_topics, name='board_topic'),
path('boards/<int:board_id>/new', views.new_topic, name='new_topic'),
]