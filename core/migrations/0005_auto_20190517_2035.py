# Generated by Django 2.2.1 on 2019-05-17 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190513_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='diagnostico',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='temperatura',
            field=models.DecimalField(decimal_places=2, max_digits=2),
        ),
    ]
