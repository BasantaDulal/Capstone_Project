from django.urls import path
from . import views as crop_yield_views

urlpatterns = [
    path('crop_yield_prediction/', crop_yield_views.crop_yield_prediction, name='crop_yield_prediction'),
]
