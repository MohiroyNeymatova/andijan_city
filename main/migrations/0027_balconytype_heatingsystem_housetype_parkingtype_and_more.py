# Generated by Django 4.1.6 on 2023-11-18 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_info_fb_info_insta_info_tg_info_yt'),
    ]

    operations = [
        migrations.CreateModel(
            name='BalconyType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='HeatingSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='HouseType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='ParkingType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='PlacesNearby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='residences/')),
                ('title', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='ResidenceFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='residences/')),
            ],
        ),
        migrations.CreateModel(
            name='Territory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='residence',
            name='about',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='residence',
            name='bg_image',
            field=models.ImageField(default=1, upload_to='residences/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='residence',
            name='flats_quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='residence',
            name='phone_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='residence',
            name='size_up_to_ceiling',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='residence',
            name='balcony_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.balconytype'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='residence',
            name='features',
            field=models.ManyToManyField(to='main.residencefeature'),
        ),
        migrations.AddField(
            model_name='residence',
            name='heating_system',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.heatingsystem'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='residence',
            name='house_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.housetype'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='residence',
            name='parking_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.parkingtype'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='residence',
            name='places_nearby',
            field=models.ManyToManyField(to='main.placesnearby'),
        ),
        migrations.AddField(
            model_name='residence',
            name='territory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.territory'),
            preserve_default=False,
        ),
    ]
