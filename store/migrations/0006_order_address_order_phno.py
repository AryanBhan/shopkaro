# Generated by Django 4.1.1 on 2022-10-08 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0005_order"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="address",
            field=models.CharField(default="New,Delhi", max_length=500),
        ),
        migrations.AddField(
            model_name="order",
            name="phno",
            field=models.CharField(default="9419102342", max_length=13),
        ),
    ]
