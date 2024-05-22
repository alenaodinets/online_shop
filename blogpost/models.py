from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Blogpost(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.CharField(max_length=255, verbose_name='slug', null=True, blank=True)
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
        ordering = ('created_at',)

