
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('game/', views.game, name='game'),
    path('slider/', views.slider, name='slider'),
    path('lk/', views.lk, name='lk'),

]
