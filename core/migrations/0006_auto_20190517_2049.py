# Generated by Django 2.2.1 on 2019-05-17 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20190517_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='temperatura',
            field=models.IntegerField(),
        ),
    ]
