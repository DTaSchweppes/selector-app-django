from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="Наименование категории",
        unique=True,
        error_messages={
            'unique': "Категория с таким наименованием уже существует!"
        })
    parent_category_id = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категория"