from django.db import models

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

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category"]

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


class Blogpost(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.CharField(max_length=255, verbose_name="URL", **NULLABLE)
    content = models.TextField(verbose_name="Контент")
    preview = models.ImageField(upload_to='catalog/', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    publication_sign = models.BooleanField(default=True, verbose_name="Опубликовать")
    number_of_views = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'