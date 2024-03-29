# Generated by Django 5.0.1 on 2024-01-14 10:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="WorkType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("product_is_required", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="ActionType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Title")),
                ("estimated_time", models.TimeField(verbose_name="Estimated time")),
                ("price", models.FloatField(verbose_name="Price")),
                ("number", models.FloatField(verbose_name="Number")),
                ("units", models.CharField(max_length=3, verbose_name="Units")),
                (
                    "work_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="price.worktype"
                    ),
                ),
            ],
        ),
    ]
