# Generated by Django 3.0.8 on 2020-07-04 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
