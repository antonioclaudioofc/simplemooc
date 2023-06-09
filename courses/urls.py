from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('<int:pk>/', views.details, name='details'),
    path('<slug:slug>/', views.details, name='details'),
    path('<slug:slug>/inscricao', views.enrollment, name='enrollment'),
    path('<slug:slug>/anuncios', views.announcements, name='announcements'),
]
