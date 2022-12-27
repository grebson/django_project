from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='articles'),
    path('create/', views.create_view, name='create-article'),
    path('<str:pk>/', views.detail_view, name='article'),
    path('<str:pk>/update/', views.update_view, name='update-article'),
    path('<str:pk>/delete/', views.delete_view, name='delete-article'),

    path('category/create/', views.category_create_view, name='create-category'),
    path('category/<str:pk>/', views.category_view, name='category'),
]
