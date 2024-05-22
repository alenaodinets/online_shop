from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")

    avatar = models.ImageField(
        upload_to="users/avatar",
        blank=True,
        null=True,
        verbose_name="Аватар",
        help_text="Загрузите ваше фото", )
    phone = models.CharField(max_length=30, verbose_name="Номер телефона", blank=True, null=True,
                             help_text="Введите номер телефона")
    country = models.CharField(max_length=30, verbose_name="Страна", blank=True, null=True,
                               help_text="Введите страну проживания")

    verification_code = models.CharField(max_length=100, verbose_name='код', blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


    def __str__(self):
        return self.email
