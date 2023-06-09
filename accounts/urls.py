from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    path('entrar', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('cadastre-se', views.register, name='register'),
    path('sair', LogoutView.as_view(next_page='/'), name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('editar', views.edit, name='edit'),
    path('editar-senha', views.edit_password, name='edit_password')
]
