# Generated by Django 3.2.4 on 2021-07-05 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0003_remove_order_seller_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='seller_id',
            field=models.IntegerField(default=0),
        ),
    ]
