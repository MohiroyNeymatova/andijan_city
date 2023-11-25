# Generated by Django 4.1.6 on 2023-11-18 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_paymentbanner'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('text', models.CharField(max_length=250)),
                ('icon', models.ImageField(upload_to='icons/')),
            ],
        ),
    ]
