from django.urls import path
from . import views as irrigation_views

urlpatterns = [
    path('irrigation_planning/', irrigation_views.fertilizer_requirement, name='fertilizer_requirement'),
]
