# Generated by Django 2.2.12 on 2020-04-23 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_product_photo_1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='farm',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, related_name='products', to='farm.Farm'),
        ),
    ]
