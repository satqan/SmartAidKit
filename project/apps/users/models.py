from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, password, **extra_fields):
        user = self.model(**extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('users.custom_user_manager.value_error.not_staff'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('users.custom_user_manager.value_error.not_superuser'))
        return self.create_user(password, **extra_fields)


class User(AbstractUser):
    username = models.CharField(
        verbose_name=_('Username'),
        max_length=20,
        unique=True
    )
    email = models.EmailField(
        verbose_name=_('email'),
        blank=True
    )
    first_name = models.CharField(
        verbose_name=_('First name'),
        max_length=30
    )
    last_name = models.CharField(
        verbose_name=_('Last name'),
        max_length=30,
        blank=True
    )
    middle_name = models.CharField(
        verbose_name=_('Middle name'),
        max_length=30,
        blank=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
