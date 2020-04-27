# Generated by Django 3.0.5 on 2020-04-26 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_auto_20200426_0855'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('phone', models.CharField(blank=True, max_length=13, verbose_name='Phone')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
                'ordering': ('name',),
            },
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ('name',), 'verbose_name': 'Название доступных продуктов', 'verbose_name_plural': 'Названиия доступных продуктов'},
        ),
        migrations.AddField(
            model_name='products',
            name='slug',
            field=models.SlugField(default='', verbose_name='Краткое название'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='desired_contact_method',
            field=models.CharField(choices=[('email', 'E-mail'), ('phone', 'Телефон'), ('wapp', 'WhatsApp'), ('teleg', 'Telegram')], max_length=10, verbose_name='Предпочитаемый метод связи'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.Products', verbose_name='Продукты'),
        ),
    ]
