from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.contrib.auth.hashers import make_password
from uuid import uuid4


class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, password=None, cpf=None):
        if not email:
            raise ValueError('O campo de e-mail é obrigatório')
        if not name:
            raise ValueError('O campo de nome é obrigatório')
        if not cpf:
            raise ValueError('O campo de CPF é obrigatório')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name,cpf=cpf)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None, cpf=None):
        user = self.create_user(email, name, password, cpf)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, verbose_name='ID')
    email = models.EmailField(unique=True, verbose_name='Email')
    name = models.CharField(max_length=255, verbose_name='Nome')
    cpf = models.CharField(max_length=11, unique=True, verbose_name='CPF')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    is_staff = models.BooleanField(default=False, verbose_name='Administrador')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última atualização')
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'cpf']

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='customuser_groups', 
        related_query_name='customuser_group',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='customuser_user_permissions', 
        related_query_name='customuser_user_permission',
    )

    class Meta:
        ordering = ['name', 'email'] 
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários' 

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


