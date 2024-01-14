# Generated by Django 5.0.1 on 2024-01-14 11:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("price", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="actiontype",
            options={
                "verbose_name": "action type",
                "verbose_name_plural": "action types",
            },
        ),
        migrations.AlterField(
            model_name="actiontype",
            name="estimated_time",
            field=models.DurationField(verbose_name="Estimated time"),
        ),
        migrations.AlterField(
            model_name="actiontype",
            name="units",
            field=models.CharField(
                choices=[("PCS", "Pieces"), ("HRS", "Hours")],
                max_length=3,
                verbose_name="Units",
            ),
        ),
        migrations.AlterField(
            model_name="actiontype",
            name="work_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="price.worktype",
                verbose_name="Work type",
            ),
        ),
    ]
