# Generated by Django 2.2.1 on 2019-05-20 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20190518_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='temperatura',
            field=models.DecimalField(decimal_places=5, max_digits=5),
        ),
    ]
