# Generated by Django 3.0.5 on 2020-04-28 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0008_auto_20200428_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='desired_contact_method',
            field=models.CharField(choices=[('email', 'E-mail'), ('phone', 'Телефон'), ('wapp', 'WhatsApp'), ('teleg', 'Telegram')], default='email', max_length=10, verbose_name='Предпочитаемый метод связи'),
        ),
    ]
