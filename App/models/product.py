from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category_id = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    suppliers_id = models.ManyToManyField('SupplierCard')
    objects = models.Manager()

    def __str__(self):
        return self.name