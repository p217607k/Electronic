# Generated by Django 4.1.2 on 2022-10-21 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='statu',
            field=models.CharField(choices=[('Public', 'Public'), ('Draft', 'Draft')], default=1, max_length=200),
            preserve_default=False,
        ),
    ]
