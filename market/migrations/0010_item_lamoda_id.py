# Generated by Django 3.2.3 on 2021-06-14 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0009_images_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='lamoda_id',
            field=models.CharField(default=2, max_length=20),
            preserve_default=False,
        ),
    ]
