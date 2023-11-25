from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *


@api_view(['GET'])
def get_logo(request):
    data = LogoSerializer(Info.objects.last(), many=False).data
    return Response(data)


@api_view(['GET'])
def get_main_banner(request):
    data = MainBannerSerializer(MainBanner.objects.last(), many=False).data
    return Response(data)


@api_view(['GET'])
def filter_flats_by_region(request, pk):
    data = FlatSerializer(Flat.objects.filter(residence__region_id=pk), many=True).data
    return Response(data)


@api_view(['GET'])
def filter_flats_by_room_quantity(request):
    requested_quantity = request.GET['quantity']
    quantity = int(requested_quantity)
    if quantity in [1, 2, 3]:
        data = FlatSerializer(Flat.objects.filter(room_quantity=quantity), many=True).data
    elif quantity == '4+':
        data = FlatSerializer(Flat.objects.filter(room_quantity__gte=4), many=True).data
    else:
        data = {
            "message": "there are no flats"
        }
    return Response(data)


@api_view(['GET'])
def filter_flats_by_price(request):
    min_price = request.GET['min_price']
    max_price = request.GET['max_price']
    data = FlatSerializer(Flat.objects.filter(price__gte=min_price, price__lte=max_price), many=True).data
    return Response(data)


@api_view(['GET'])
def filter_flats_by_area(request):
    min_area = request.GET['min_area']
    max_area = request.GET['max_area']
    data = FlatSerializer(Flat.objects.filter(area__gte=min_area, area__lte=max_area), many=True).data
    return Response(data)


@api_view(['GET'])
def filter_flats_by_location(request):
    long = request.GET['long']
    lang = request.GET['lang']
    data = FlatSerializer(Flat.objects.filter(residence__lang=lang, residence__long=long), many=True).data
    return Response(data)


@api_view(['GET'])
def get_quantity_of_flats(request):
    flats = Flat.objects.all().count()
    data = {
        "quantity": flats
    }
    return Response(data)


@api_view(['GET'])
def get_popular_residences(request):
    data = AdResidenceSerializer(Residence.objects.filter(is_popular=True).order_by('id')[:6], many=True).data
    return Response(data)


@api_view(['GET'])
def get_payment_banner(request):
    data = PaymentBannerSerializer(PaymentBanner.objects.last(), many=False).data
    return Response(data)


@api_view(['GET'])
def get_payment_types(request):
    data = PaymentTypeSerializer(PaymentType.objects.all(), many=True).data
    return Response(data)


@api_view(['GET'])
def get_all_residences(request):
    data = AdResidenceSerializer(Residence.objects.all().order_by('-id')[:6], many=True).data
    return Response(data)


@api_view(['GET'])
def get_percentage_banner(request):
    data = PercentageBannerSerializer(PercentageBanner.objects.last(), many=False).data
    return Response(data)


@api_view(['GET'])
def get_developers(request):
    data = DeveloperSerializer(Developer.objects.all().order_by('-id')[:4], many=True).data
    return Response(data)


@api_view(['GET'])
def get_phone_number(request):
    data = PhoneNumberSerializer(Info.objects.last(), many=False).data
    return Response(data)


@api_view(['POST'])
def post_appointment(request):
    name = request.POST['name']
    phone_number = request.POST['phone_number']
    email = request.POST['email']
    Appointment.objects.create(name=name, phone_number=phone_number, email=email)
    data = {
        "message": "Success"
    }
    return Response(data)


@api_view(['GET'])
def get_appointment_banner(request):
    data = AppointmentBannerSerializer(AppointmentBanner.objects.last(), many=False).data
    return Response(data)


@api_view(['GET'])
def get_info(request):
    data = InfoSerializer(Info.objects.last(), many=False).data
    return Response(data)


@api_view(['GET'])
def get_room_quantities(request):
    data = RoomQuantitySerializer(RoomQuantity.objects.all(), many=True).data
    return Response(data)


@api_view(['GET'])
def get_all_finishings(request):
    data = FinishingSerializer(Finishing.objects.all(), many=True).data
    return Response(data)


@api_view(['GET'])
def get_residence(request, pk):
    data = ResidenceSerializer(Residence.objects.get(id=pk), many=False).data
    return Response(data)


@api_view(['GET'])
def get_realtor_banner(request):
    data = RealtorBannerSerializer(RealtorBanner.objects.last(), many=False).data
    return Response(data)


@api_view(['GET'])
def find_realtor(request):
    data = FindRealtorSerializer(FindRealtor.objects.all(), many=True).data
    return Response(data)


@api_view(['GET'])
def realtor_benefits(request):
    data = RealtorBenefitsSerializer(RealtorBenefit.objects.all(), many=True).data
    return Response(data)


@api_view(['GET'])
def get_realtors(request):
    data = RealtorSerializer(Realtor.objects.all().order_by('-id')[:8], many=True).data
    return Response(data)


@api_view(['GET'])
def how_it_works(request):
    data = HowItWorkSerializer(HowItWork.objects.all(), many=True).data
    return Response(data)


@api_view(['GET'])
def filter_flats(request):
    project = request.GET['project']
    house_type = request.GET['house_type']
    min_area = request.GET['min_area']
    max_area = request.GET['max_area']
    max_price = request.GET['max_price']
    min_price = request.GET['min_price']
    flats = Flat.objects.filter(residence_id=project, residence__house_type_id=house_type, area__lte=max_area, area__gte=min_area, price__lte=max_price, price__gte=min_price)
    quantity = flats.count()
    data1 = FlatSerializer(flats, many=True).data
    data = {
        "Found flats": quantity,
        "flats": data1
    }
    return Response(data)