# Generated by Django 4.1.6 on 2023-11-18 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_findrealtor'),
    ]

    operations = [
        migrations.CreateModel(
            name='RealtorBenefit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='icons/')),
                ('title', models.CharField(max_length=250)),
                ('text', models.CharField(max_length=250)),
            ],
        ),
    ]