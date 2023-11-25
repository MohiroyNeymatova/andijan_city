from rest_framework import serializers
from .models import *


class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ['logo']


class MainBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainBanner
        fields = "__all__"


class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Flat
        fields = "__all__"


class AdResidenceSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Residence
        fields = ['residence_class', 'is_building', 'price_for_a_meter', 'name', 'address', 'deadline', 'install_payment', 'finishing', 'floors_quantity', 'price', 'images']


class PaymentBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentBanner
        fields = "__all__"


class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = "__all__"


class PercentageBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PercentageBanner
        fields = "__all__"


class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = "__all__"


class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ['phone_number']


class AppointmentBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentBanner
        fields = "__all__"


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ['logo', 'insta', 'yt', 'tg', 'fb']


class RoomQuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomQuantity
        fields = "__all__"


class FinishingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finishing
        fields = "__all__"


class ResidenceSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Residence
        fields = "__all__"


class RealtorBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealtorBanner
        fields = "__all__"


class FindRealtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = FindRealtor
        fields = "__all__"


class RealtorBenefitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealtorBenefit
        fields = "__all__"


class RealtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realtor
        fields = "__all__"


class HowItWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = HowItWork
        fields = "__all__"