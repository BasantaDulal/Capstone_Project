from django.urls import path
from . import views as fertilizer_views

urlpatterns = [
    path('fertilizer_requirement/', fertilizer_views.fertilizer_requirement, name='fertilizer_requirement'),
]
