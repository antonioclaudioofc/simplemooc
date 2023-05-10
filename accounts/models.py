from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField('Nome de Usuário', max_length=30, unique=True)
    email = models.EmailField('E-mail', unique=True)
    name = models.CharField('Nome', max_length=100, blank=True)
    is_active = models.BooleanField('Está ativo?', blank=True, default=False)
    is_staff = models.BooleanField('É da equipe?', blank=True, default=False)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self) -> str:
        return self.name or self.username
    
    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'