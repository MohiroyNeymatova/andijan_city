# Generated by Django 4.1.6 on 2023-11-16 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_roomquantity_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomquantity',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
