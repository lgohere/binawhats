from django.db import models
from django.utils import timezone

class Chamada(models.Model):
    numero = models.CharField(max_length=20)
    # data_hora = models.DateTimeField(default=timezone.now)
    # data_hora = models.DateTimeField(time=True)
    # novo = models.BooleanField()
    def __str__(self):
        return self.numero


# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# class MyUserManager(BaseUserManager):
#     def create_user(self, telefone, senha=None, **extra_fields):
#         if not telefone:
#             raise ValueError('O telefone é obrigatório')

#         user = self.model(
#             telefone=telefone,
#             **extra_fields
#         )

#         user.set_password(senha)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, telefone, senha, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         return self.create_user(telefone, senha, **extra_fields)


# class MyUser(AbstractBaseUser):
#     telefone = models.CharField(max_length=20, unique=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)

#     USERNAME_FIELD = 'telefone'

#     objects = MyUserManager()

#     def __str__(self):
#         return self.telefone


# Create your models here.

# Criar uma claa com nome Chamada significa criar um objeto no banco de dados, asssim chamado.
# dentro estão os atributos.