# Generated by Django 4.1.2 on 2022-10-28 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_rename_order_orderitem_order_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='order_id',
            new_name='order',
        ),
    ]