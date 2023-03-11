from django.urls import path
from .views import signup_page, login_page, home_page


urlpatterns = [
    path('', login_page, name='login'),
    path('signup/', signup_page, name='signup'),
]
