# Generated by Django 3.2.18 on 2023-05-04 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recebezap', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chamada',
            name='receptor',
            field=models.CharField(default='', max_length=20),
        ),
    ]