# Generated by Django 3.0.8 on 2020-08-02 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20200802_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='end',
            field=models.DateTimeField(verbose_name='end date'),
        ),
        migrations.AlterField(
            model_name='work',
            name='start',
            field=models.DateTimeField(verbose_name='start date'),
        ),
    ]
