# Generated by Django 2.0.1 on 2018-02-01 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_remove_photo_filename'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='caption',
            field=models.TextField(blank=True, max_length=2048, null=True),
        ),
    ]
