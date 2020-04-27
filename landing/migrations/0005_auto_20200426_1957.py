# Generated by Django 3.0.5 on 2020-04-26 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0004_auto_20200426_1856'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcategory',
            options={'ordering': ('name',), 'verbose_name': 'Категория продуктов', 'verbose_name_plural': 'категорий продуктов'},
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='name',
            field=models.CharField(max_length=40, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='slug',
            field=models.SlugField(help_text='Ссылка', verbose_name='Краткое название'),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Название')),
                ('slug', models.SlugField(help_text='Ссылка', verbose_name='Краткое название')),
                ('image', models.ImageField(upload_to='site_preview')),
                ('url', models.URLField()),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.ProductCategory')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ('name',),
            },
        ),
    ]
