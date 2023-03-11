"""crop_recommendation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts import views as accounts_views
from recommendation_model import views as recommendation_views
from fertilizer_req import views as fertilizer_views
from irrigation import views as irrigation_views
from crop_yield import views as crop_yield_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accounts_views.login_page, name='login'),
    path('signup/', accounts_views.signup_page, name='signup'),
    path('home/', accounts_views.home_page, name='home'),
    path('logout/', accounts_views.logout_page, name='logout'),
    path('crop_recommend/', recommendation_views.crop_recommend, name='crop_recommend'),
    path('fertilizer_requirement/', fertilizer_views.fertilizer_requirement, name='fertilizer_requirement'),
    path('irrigation_planning/', irrigation_views.irrigation_planning, name='irrigation_planning'),
    path('crop_yield_prediction/', crop_yield_views.crop_yield_prediction, name='crop_yield_prediction'),
]
