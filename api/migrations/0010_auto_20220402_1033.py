# Generated by Django 3.1.2 on 2022-04-02 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_product_big_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='image01',
            field=models.CharField(default=1, max_length=100, verbose_name='Rasm1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image02',
            field=models.CharField(default=1, max_length=100, verbose_name='Rasm2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image03',
            field=models.CharField(default=1, max_length=100, verbose_name='Rasm3'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image04',
            field=models.CharField(default=1, max_length=100, verbose_name='Rasm4'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
