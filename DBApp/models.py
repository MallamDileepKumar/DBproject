from django.db import models

# Create your models here.
class Product(models.Model):
    Id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=50)
    Cost = models.FloatField()
    Mft = models.DateField()
    Exp = models.DateField()

    def __str__(self):
        return self.Name
