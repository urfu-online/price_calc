# Generated by Django 5.0.1 on 2024-01-14 11:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("work", "0002_alter_task_project"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="product",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="work.product",
            ),
        ),
    ]