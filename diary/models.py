from django.db import models

from config.settings import AUTH_USER_MODEL

NULLABLE = {'null': True, 'blank': True}


class Entry(models.Model):
    """Класс, описывающий информацию о записях в дневнике"""
    title = models.CharField(max_length=150, verbose_name='заголовок')
    body = models.TextField(verbose_name='cодержимое')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания', **NULLABLE)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения', **NULLABLE)
    image = models.ImageField(verbose_name='изображение', **NULLABLE)
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'записи'
