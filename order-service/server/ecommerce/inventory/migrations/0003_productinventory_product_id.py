# Generated by Django 3.1.5 on 2021-01-09 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_remove_productinventory_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinventory',
            name='product_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
