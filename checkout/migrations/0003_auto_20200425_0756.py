# Generated by Django 2.2.12 on 2020-04-25 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20200424_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='street_address2',
            field=models.CharField(max_length=40),
        ),
    ]
