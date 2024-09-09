from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('team/<int:team_id>/', views.team_detail, name='team_detail'),
    path('matches/', views.match_results, name='match_results'),
    path('news/', views.news, name='news'),
]
