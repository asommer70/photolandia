# Generated by Django 2.0.1 on 2018-03-12 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0005_auto_20180203_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='local_path',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
