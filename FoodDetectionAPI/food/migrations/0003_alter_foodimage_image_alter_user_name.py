# Generated by Django 4.2.3 on 2023-07-18 07:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("food", "0002_rename_title_food_name_foodimage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="foodimage",
            name="image",
            field=models.ImageField(
                upload_to=datetime.datetime(2023, 7, 18, 16, 34, 46, 595176)
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="name",
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
