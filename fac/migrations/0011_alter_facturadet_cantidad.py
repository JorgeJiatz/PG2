# Generated by Django 4.1.5 on 2023-10-21 04:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fac", "0010_alter_facturadet_cantidad"),
    ]

    operations = [
        migrations.AlterField(
            model_name="facturadet",
            name="cantidad",
            field=models.FloatField(default=0),
        ),
    ]
