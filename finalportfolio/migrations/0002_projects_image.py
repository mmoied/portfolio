# Generated by Django 3.0.1 on 2020-08-25 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalportfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='image',
            field=models.ImageField(default='', upload_to='static/finalportfolio/images'),
        ),
    ]
