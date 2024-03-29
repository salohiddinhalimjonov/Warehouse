# Generated by Django 4.2.11 on 2024-03-08 23:12

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Material",
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
                ("title", models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("title", models.CharField(max_length=256)),
                ("guid", models.UUIDField(default=uuid.uuid4, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Warehouse",
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
                ("remainder", models.CharField(blank=True, max_length=16)),
                (
                    "remainder_type",
                    models.CharField(
                        choices=[
                            ("MT", "Meter"),
                            ("MTSQ", "Meter Square"),
                            ("PC", "Piece"),
                        ],
                        default="PC",
                        max_length=32,
                    ),
                ),
                ("price", models.IntegerField()),
                (
                    "material_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="warehouse.material",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductMaterial",
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
                ("quantity", models.CharField(blank=True, max_length=16)),
                (
                    "quantity_type",
                    models.CharField(
                        choices=[
                            ("MT", "Meter"),
                            ("MTSQ", "Meter Square"),
                            ("PC", "Piece"),
                        ],
                        default="PC",
                        max_length=32,
                    ),
                ),
                (
                    "material_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="warehouse.material",
                    ),
                ),
                (
                    "product_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="warehouse.product",
                    ),
                ),
            ],
        ),
    ]
