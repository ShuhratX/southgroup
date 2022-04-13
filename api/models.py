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
    image = models.CharField(max_length=100, verbose_name="Rasmi")
    header_image = models.CharField(max_length=100, verbose_name="Karusel rasmi")


    def __str__(self) -> str:
        return self.name


class Product(models.Model):

    class Meta:

        db_table = 'products'

        ordering = ('id',)

        verbose_name = "Maxsulot"
        verbose_name_plural = "Maxsulotlar"

    title = models.CharField(max_length=50, verbose_name="Nomi")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    price = models.PositiveIntegerField(verbose_name="Narxi")
    image01 = models.CharField(max_length=100, verbose_name="Rasm1")
    image02 = models.CharField(max_length=100, verbose_name="Rasm2")
    image03 = models.CharField(max_length=100, verbose_name="Rasm3")
    image04 = models.CharField(max_length=100, verbose_name="Rasm4")
    description = ArrayField(
        models.CharField(max_length=255, blank=True),
        size=15, null=True, verbose_name="Qisqacha")
    big_description = ArrayField(
        models.CharField(max_length=455, blank=True),
        size=100, null=True
    )

    def __str__(self) -> str:
        return self.title
