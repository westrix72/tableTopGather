# Generated by Django 4.2.3 on 2023-07-26 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabletopgatherAPP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='number',
            field=models.CharField(default='', max_length=100),
        ),
    ]