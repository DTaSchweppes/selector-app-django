from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    parent_category_id = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.name