from django.urls import path
from Weather_api.views import *

urlpatterns = [
    path('register',reg_fun),
    path('save', save_user),
    path('login', login_fun),
    path('sign_in', sign_fun),
    path('fetch_data', fetch_weather_data),
    path('logout', logout_fun)
    
]

# path('logout', logout_fun)