# Generated by Django 4.1.5 on 2023-02-15 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainApp", "0003_checkout_checkoutproducts"),
    ]

    operations = [
        migrations.AddField(
            model_name="checkoutproducts",
            name="pid",
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name="checkout",
            name="orderStatus",
            field=models.IntegerField(
                choices=[
                    (0, "Order Placed"),
                    (1, "Not Packed"),
                    (2, "Packed"),
                    (3, "Ready to Dispatch"),
                    (4, "Dispatched"),
                    (5, "Out For Delivery"),
                    (6, "Delivered"),
                    (7, "Cancelled"),
                ],
                default=0,
            ),
        ),
        migrations.AlterField(
            model_name="checkout",
            name="paymentMode",
            field=models.IntegerField(
                choices=[(0, "COD"), (1, "Net Banking")], default=0
            ),
        ),
        migrations.AlterField(
            model_name="checkout",
            name="paymentStatus",
            field=models.IntegerField(choices=[(0, "Pending"), (1, "Done")], default=0),
        ),
    ]
