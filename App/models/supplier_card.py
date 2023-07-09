from django.db import models
from django.urls import reverse

class SupplierCard(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="Наименование карточки поставщика",
        unique=True,
        error_messages={
            'unique': "Поставщик с таким наименованием уже существует!"
        })
    address = models.CharField(max_length=255, verbose_name="Адрес поставщика")
    rating_choices = (
        ('low', 'Низкий'),
        ('medium', 'Средний'),
        ('high', 'Высокий')
    )
    rating = models.CharField(max_length=10, choices=rating_choices, verbose_name="Ценовой рейтинг поставщика")
    categories = models.ManyToManyField('Category', verbose_name="Категория")
    contacts = models.CharField(max_length=150, default=' ', verbose_name="Контактная информация")
    description = models.TextField(verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Карточка поставщика"
        verbose_name_plural = "Карточка поставщика"