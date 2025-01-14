from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_view),
    path('crud/', views.crud),

    path('products/list/', views.product_list, name='product_list'),
    path('products/add/', views.product_create, name='product_create'),
    path('products/detail/<int:pk>/', views.product_detail, name='product_detail'),
    path('products/edit/<int:pk>/', views.product_update, name='product_update'),
    path('products/delete/<int:pk>/', views.product_delete, name='product_delete'),
    path('books/', views.book_list, name='book_list'),
    path('detail/<int:pk>/', views.book_detail, name='book_detail'),
    path('add/', views.book_create, name='book_create'),
    path('delete/<int:pk>/', views.book_delete, name='book_delete'),
    path('edit/<int:pk>/', views.book_update, name='book_update'),

    path('courses/', views.course_list, name='course_list'),
    path('courses/create/', views.course_create, name='course_create'),
    path('courses/<int:pk>/', views.course_detail, name='course_detail'),
    path('courses/<int:pk>/edit/', views.course_edit, name='course_edit'),
    path('courses/<int:pk>/delete/', views.course_delete, name='course_delete'),
    path('students/', views.student_list, name='student_list'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/<int:pk>/', views.student_detail, name='student_detail'),
    path('students/<int:pk>/edit/', views.student_edit, name='student_edit'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),

    path('participants/', views.participant_list, name='participant_list'),
    path('participants/create/', views.participant_create, name='participant_create'),
    path('participants/<int:pk>/update/', views.participant_update, name='participant_update'),
    path('participants/<int:pk>/', views.participant_detail, name='participant_detail'),
    path('participants/<int:pk>/delete/', views.participant_delete, name='participant_delete'),
    path('events/', views.event_list, name='event_list'),
    path('events/<int:pk>/', views.event_detail, name='event_detail'),
    path('events/create/', views.event_create, name='event_create'),
    path('events/<int:pk>/update/', views.event_update, name='event_update'),
    path('events/<int:pk>/delete/', views.event_delete, name='event_delete'),
]
