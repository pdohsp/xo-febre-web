# Generated by Django 2.2.1 on 2019-05-20 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20190519_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='temperatura',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]
