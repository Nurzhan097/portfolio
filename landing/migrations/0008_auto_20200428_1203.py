# Generated by Django 3.0.5 on 2020-04-28 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0007_auto_20200427_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(blank=True, verbose_name='Коментарий'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.ProductCategory', verbose_name='Желаемый продукт'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(to='landing.ProductCategory', verbose_name='Категории продуктов'),
        ),
    ]
