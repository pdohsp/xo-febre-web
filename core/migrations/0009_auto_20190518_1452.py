# Generated by Django 2.2.1 on 2019-05-18 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20190518_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='temperatura',
            field=models.IntegerField(),
        ),
    ]
