from django.urls import path
from .views import *


urlpatterns = [
    path('get_logo/', get_logo),
    path('get_main_banner/', get_main_banner),
    path('filter_flats_by_region/<int:pk>/', filter_flats_by_region),
    path('filter_flats_by_room_quantity/', filter_flats_by_room_quantity),
    path('filter_flats_by_price/', filter_flats_by_price),
    path('filter_flats_by_area/', filter_flats_by_area),
    path('filter_flats_by_location/', filter_flats_by_location),
    path('get_quantity_of_flats/', get_quantity_of_flats),
    path('get_popular_residences/', get_popular_residences),
    path('get_payment_banner/', get_payment_banner),
    path('get_payment_types/', get_payment_types),
    path('get_all_residences/', get_all_residences),
    path('get_percentage_banner/', get_percentage_banner),
    path('get_developers/', get_developers),
    path('get_phone_number/', get_phone_number),
    path('post_appointment/', post_appointment),
    path('get_appointment_banner/', get_appointment_banner),
    path('get_info/', get_info),
    path('get_room_quantities/', get_room_quantities),
    path('get_all_finishings/', get_all_finishings),
    path('get_residence/<int:pk>/', get_residence),
    path('get_realtor_banner/', get_realtor_banner),
    path('find_realtor/', find_realtor),
    path('realtor_benefits/', realtor_benefits),
    path('get_realtors/', get_realtors),
    path('how_it_works/', how_it_works),
    path('filter_flats/', filter_flats)
]