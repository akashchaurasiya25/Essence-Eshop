# Generated by Django 4.1.5 on 2023-01-25 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainApp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="pic1",
            field=models.ImageField(default=None, upload_to="product"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="product",
            name="pic2",
            field=models.ImageField(default=None, upload_to="product"),
            preserve_default=False,
        ),
    ]