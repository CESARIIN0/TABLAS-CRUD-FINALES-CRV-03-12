# Generated by Django 5.1 on 2024-12-03 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plato_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plato',
            name='Cuantos_Platos',
            field=models.IntegerField(),
        ),
    ]
