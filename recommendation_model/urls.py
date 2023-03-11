from django.urls import path
from . import views as recommendation_views

urlpatterns = [
    path('crop_recommend/', recommendation_views.crop_recommend, name='crop_recommend')
]
