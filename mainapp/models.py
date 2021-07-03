from django.db import models

class Colors(models.Model):
    colors = models.TextField(verbose_name='Цвет')

    def __str__(self):
        return self.colors


    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'
