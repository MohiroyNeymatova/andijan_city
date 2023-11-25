from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import m2m_changed


class Info(models.Model):
    logo = models.ImageField(upload_to='info/')
    phone_number = models.IntegerField()
    tg = models.URLField()
    insta = models.URLField()
    yt = models.URLField()
    fb = models.URLField()


class MainBanner(models.Model):
    image = models.ImageField(upload_to='banners/')
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Region(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class ResidenceClass(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Finishing(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class DeveloperImage(models.Model):
    image = models.ImageField(upload_to='developers/')


class Developer(models.Model):
    name = models.CharField(max_length=250)
    logo = models.ImageField(upload_to='logos/')
    image = models.ManyToManyField(DeveloperImage)

    @property
    def adverts(self):
        adverts = Flat.objects.filter(residence__developer=self).count()
        return adverts

    def __str__(self):
        return self.name


class HouseType(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class ParkingType(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class BalconyType(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class HeatingSystem(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Territory(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class ResidenceFeature(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='residences/')

    def __str__(self):
        return self.title


class PlacesNearby(models.Model):
    image = models.ImageField(upload_to='residences/')
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class ResidenceImage(models.Model):
    image = models.ImageField(upload_to='residences/')


class Residence(models.Model):
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    is_building = models.BooleanField(default=True)
    is_popular = models.BooleanField(default=False)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    lang = models.TextField()
    long = models.TextField()
    residence_class = models.ForeignKey(ResidenceClass, on_delete=models.CASCADE)   #tip
    price_for_a_meter = models.IntegerField()
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    deadline = models.CharField(max_length=250)
    install_payment = models.CharField(max_length=250)
    finishing = models.ForeignKey(Finishing, on_delete=models.CASCADE)
    floors_quantity = models.IntegerField()
    price = models.CharField(max_length=250)
    flats_quantity = models.IntegerField()
    size_up_to_ceiling = models.IntegerField()
    house_type = models.ForeignKey(HouseType, on_delete=models.CASCADE)
    parking_type = models.ForeignKey(ParkingType, on_delete=models.CASCADE)
    balcony_type = models.ForeignKey(BalconyType, on_delete=models.CASCADE)
    heating_system = models.ForeignKey(HeatingSystem, on_delete=models.CASCADE)
    territory = models.ForeignKey(Territory, on_delete=models.CASCADE)
    phone_number = models.IntegerField()
    features = models.ManyToManyField(ResidenceFeature)
    places_nearby = models.ManyToManyField(PlacesNearby)
    bg_image = models.ImageField(upload_to='residences/')
    about = models.TextField()
    images = models.ImageField(upload_to='residences/')

    def __str__(self):
        return self.name


class RoomQuantity(models.Model):
    quantity = models.IntegerField()

    def __int__(self):
        return self.quantity


class Flat(models.Model):
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE)
    room_quantity = models.ForeignKey(RoomQuantity, on_delete=models.CASCADE)
    price = models.CharField(max_length=250)
    area = models.IntegerField()


class PaymentBanner(models.Model):
    image = models.ImageField(upload_to='banners/')


class PaymentType(models.Model):
    name = models.CharField(max_length=250)
    text = models.CharField(max_length=250)
    icon = models.ImageField(upload_to='icons/')

    def __str__(self):
        return self.name


class PercentageBanner(models.Model):
    bg_image = models.ImageField(upload_to='banners/')
    title = models.CharField(max_length=250)
    text = models.CharField(max_length=250)
    percent = models.IntegerField()
    percentage_name = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Appointment(models.Model):
    name = models.CharField(max_length=250)
    phone_number = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name


class AppointmentBanner(models.Model):
    bg_image = models.ImageField(upload_to='banners/')
    image = models.ImageField(upload_to='images/')


class RealtorBanner(models.Model):
    image = models.ImageField(upload_to='banners/')


class FindRealtor(models.Model):
    icon = models.ImageField(upload_to='icons/')
    title = models.CharField(max_length=250)
    text = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class RealtorBenefit(models.Model):
    icon = models.ImageField(upload_to='icons/')
    title = models.CharField(max_length=250)
    text = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Realtor(models.Model):
    name = models.CharField(max_length=250)
    rating = models.FloatField()
    review_quantity = models.IntegerField()
    photo = models.ImageField(upload_to='realtors/')

    def __str__(self):
        return self.name


class HowItWork(models.Model):
    title = models.CharField(max_length=250)
    text = models.CharField(max_length=250)

    def __str__(self):
        return self.title
