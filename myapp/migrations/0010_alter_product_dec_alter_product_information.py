# Generated by Django 4.1.2 on 2022-10-25 17:01

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_product_dec_alter_product_statu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='dec',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='information',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
