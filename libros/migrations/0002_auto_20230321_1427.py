# Generated by Django 3.1.3 on 2023-03-21 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='anio',
            field=models.IntegerField(default=0),
        ),
    ]
