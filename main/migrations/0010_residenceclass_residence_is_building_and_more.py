# Generated by Django 4.1.6 on 2023-11-16 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_residence_lang_residence_long'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResidenceClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='residence',
            name='is_building',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='residence',
            name='is_popular',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='residence',
            name='residence_class',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.residenceclass'),
            preserve_default=False,
        ),
    ]
