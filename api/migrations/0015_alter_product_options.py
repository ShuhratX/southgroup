# Generated by Django 4.0.3 on 2022-04-13 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_alter_product_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('id',), 'verbose_name': 'Maxsulot', 'verbose_name_plural': 'Maxsulotlar'},
        ),
    ]