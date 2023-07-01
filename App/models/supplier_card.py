from django.db import models

class SupplierCard(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    rating_choices = (
        ('low', 'Низкий'),
        ('medium', 'Средний'),
        ('high', 'Высокий')
    )
    rating = models.CharField(max_length=10, choices=rating_choices)
    categories = models.ManyToManyField('Category')
    contacts = models.CharField(max_length=150, default=' ')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return self.name
