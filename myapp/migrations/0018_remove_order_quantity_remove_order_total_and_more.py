# Generated by Django 4.1.2 on 2022-10-28 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_remove_orderitem_payment_id_order_payment_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='paid',
        ),
        migrations.AddField(
            model_name='order',
            name='paid',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='additional_info',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='pincode',
            field=models.IntegerField(null=True),
        ),
    ]
