# Generated by Django 4.1.6 on 2023-11-18 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_percentagebanner'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeveloperImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='developers/')),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('logo', models.ImageField(upload_to='logos/')),
                ('image', models.ManyToManyField(to='main.developerimage')),
            ],
        ),
        migrations.AddField(
            model_name='residence',
            name='developer',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='main.developer'),
        ),
    ]
