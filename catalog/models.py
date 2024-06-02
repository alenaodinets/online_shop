from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class Product(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Наименование",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание",
        help_text="Введите описание продукта",
    )
    image_preview = models.ImageField(
        upload_to="products/photo",
        blank=True,
        null=True,
        verbose_name="Изображение(превью)",
        help_text="Загрузите фото продукта",
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите категорию",
        blank=True,
        null=True,
        related_name="products",
    )
    price = models.IntegerField(verbose_name="Цена", help_text="Введите цену")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(
        auto_now=True, verbose_name="Дата последнего изменения"
    )
    views_counter = models.IntegerField(default=0, verbose_name="Счетчик просмотров")
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Владелец', **NULLABLE)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category"]
        permissions = [
            ('set_published', 'Can publish product'),
            ('change_description', 'Can change description'),
            ('change_category', 'Can change category'),
        ]

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Наименование",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание", help_text="Введите описание"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Version(models.Model):
    product = models.ForeignKey(Product, verbose_name="Продукт",
                                on_delete=models.SET_NULL, **NULLABLE, )
    number_of_version = models.PositiveIntegerField(verbose_name="Номер версии")
    name_of_versions = models.CharField(max_length=150, verbose_name="Название версии")
    is_active_version = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.product}"

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"