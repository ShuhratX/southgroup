from email.mime import image
from statistics import mode
from unicodedata import category
from django.db import models
from django.contrib.postgres.fields import ArrayField


class Category(models.Model):

    class Meta:

        db_table = 'categories'

        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"

    name = models.CharField(max_length=50, verbose_name="Nomi")
    image = models.ImageField(verbose_name="Rasmi")


    def __str__(self) -> str:
        return self.name


class Product(models.Model):

    class Meta:

        db_table = 'products'

        verbose_name = "Maxsulot"
        verbose_name_plural = "Maxsulotlar"

    title = models.CharField(max_length=50, verbose_name="Nomi")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(verbose_name="Narxi")
    image = models.ImageField(verbose_name="Rasmi", blank=True, null=True)
    description = models.CharField(max_length=255, verbose_name="Qisqacha")
    big_description = ArrayField(
        models.CharField(max_length=255, blank=True),
        size=100, null=True
    )

    def __str__(self) -> str:
        return self.title
