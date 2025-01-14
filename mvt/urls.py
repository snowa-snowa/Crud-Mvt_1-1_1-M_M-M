from django.urls import path
from . import views

urlpatterns = [
    path('mvt/', views.mvt),

    path('people/', views.person_list, name='person_list'),
    path('people/<pk>/', views.person_detail, name='person_detail'),
    path('passport/', views.passport_list, name='passport_list'),
    path('passport/<pk>/', views.passport_detail, name='passport_detail'),

    path('reporters/', views.reporter_list, name='reporter_list'),
    path('reporters/<pk>/', views.reporter_detail, name='reporter_detail'),
    path('articles/', views.article_list, name='article_list'),
    path('articles/<pk>/', views.article_detail, name='article_detail'),

    path('cars/', views.car_list, name='car_list'),
    path('car/<pk>/', views.car_detail, name='car_detail'),
    path('fuel/', views.fuel_list, name='fuel_list'),
    path('fuel/<pk>/', views.fuel_detail, name='fuel_detail'),
]
