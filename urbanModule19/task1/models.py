from django.db import models


# Create your models here.

class Buyer(models.Model):
    name = models.TextField(default=None)
    balance = models.DecimalField(default=0, decimal_places=10, max_digits=19)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Game(models.Model):
    title = models.TextField(default=None)
    cost = models.DecimalField(default=None, decimal_places=10, max_digits=19)
    size = models.DecimalField(default=None, decimal_places=10, max_digits=19)
    description = models.TextField(default=None)
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')
