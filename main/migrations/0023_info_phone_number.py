# Generated by Django 4.1.6 on 2023-11-18 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_alter_residence_developer'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='phone_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
