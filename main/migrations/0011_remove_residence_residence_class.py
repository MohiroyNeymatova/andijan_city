# Generated by Django 4.1.6 on 2023-11-16 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_residenceclass_residence_is_building_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='residence',
            name='residence_class',
        ),
    ]
