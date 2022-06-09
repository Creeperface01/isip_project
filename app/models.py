from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Item(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    rented = models.BooleanField(default=False)
    place = models.CharField(max_length=100)


class RentItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    rented_at = models.DateField()
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        verbose_name="the related poll",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="the related user",
    )

