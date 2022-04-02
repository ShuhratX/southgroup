# Generated by Django 4.0.3 on 2022-04-01 11:18

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_product_big_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='big_description',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=455), null=True, size=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=300, verbose_name='Qisqacha'),
        ),
    ]