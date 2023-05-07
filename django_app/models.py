from django.db import models
from django.utils import timezone


class Ad(models.Model):
    seller = models.CharField(verbose_name="Продавец", max_length=150)
    title = models.CharField(verbose_name="Наименование товара", max_length=300)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        app_label = "django_app"
        ordering = ('-created',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title


