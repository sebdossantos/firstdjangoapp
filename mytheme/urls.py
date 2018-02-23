from django.urls import path

from . import views

app_name = 'mytheme'

urlpatterns = [
    path('blank/', views.blank, name='blank'),
    path('cards/', views.cards, name='cards'),
    path('charts/', views.charts, name='charts'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('navbar/', views.navbar, name='navbar'),
    path('register/', views.register, name='register'),
    path('tables/', views.tables, name='tables'),
]
