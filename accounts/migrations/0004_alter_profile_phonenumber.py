# Generated by Django 3.2.3 on 2021-06-19 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_emailcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phonenumber',
            field=models.CharField(max_length=12, verbose_name='Телефон'),
        ),
    ]
