# Generated by Django 4.1.5 on 2023-01-19 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Brand",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=20, unique=True)),
                ("pic", models.ImageField(upload_to="brand")),
            ],
        ),
        migrations.CreateModel(
            name="Buyer",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=30)),
                ("username", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=50)),
                ("phone", models.CharField(max_length=15)),
                ("addressline1", models.CharField(max_length=50)),
                ("addressline2", models.CharField(max_length=50)),
                ("addressline3", models.CharField(max_length=50)),
                ("pin", models.CharField(max_length=10)),
                ("city", models.CharField(max_length=30)),
                ("state", models.CharField(max_length=30)),
                ("pic", models.ImageField(upload_to="user")),
            ],
        ),
        migrations.CreateModel(
            name="Maincategory",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Subcategory",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50)),
                ("color", models.CharField(max_length=20)),
                ("size", models.CharField(max_length=10)),
                ("baseprice", models.IntegerField()),
                ("discount", models.IntegerField()),
                ("finalprice", models.IntegerField()),
                ("stock", models.BooleanField(default=True)),
                ("description", models.TextField()),
                (
                    "pic1",
                    models.ImageField(
                        blank=True, default="", null=True, upload_to="product"
                    ),
                ),
                (
                    "pic2",
                    models.ImageField(
                        blank=True, default="", null=True, upload_to="product"
                    ),
                ),
                (
                    "pic3",
                    models.ImageField(
                        blank=True, default="", null=True, upload_to="product"
                    ),
                ),
                (
                    "pic4",
                    models.ImageField(
                        blank=True, default="", null=True, upload_to="product"
                    ),
                ),
                (
                    "brand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="mainApp.brand"
                    ),
                ),
                (
                    "maincategory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mainApp.maincategory",
                    ),
                ),
                (
                    "subcategory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mainApp.subcategory",
                    ),
                ),
            ],
        ),
    ]
