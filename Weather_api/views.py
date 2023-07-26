import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from Weather_api.models import Weather_check

API_KEY = "fd1cdd74720b3d5ea9d871a164a2f07b"

# Create your views here.

def reg_fun(request):
    return render(request, 'reg.html')

def save_user(request):
    dict1 = request.POST
    username = dict1['username']
    email = dict1['email']
    password = dict1['password']
    user = User.objects.create_user(username=username, email=email, password=password)
    user.save()
    return redirect('/weather_api/login')

def login_fun(request):
    return render(request, 'login.html')

def sign_fun(request):
    dict1 = request.POST
    username = dict1['username']
    password = dict1['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return render(request, 'login.html')
    else:
        login(request, user)
        return render(request, 'sample.html')

def convert_to_celsius(temperature_kelvin):
    celsius = temperature_kelvin - 273.15
    return round(celsius, 2)

def fetch_weather_data(request):
    if request.method == 'POST':
        location = request.POST.get('city')
        weather_data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}').json()
        try:
            main = weather_data['weather'][0]['main']
            icon_id = weather_data['weather'][0]['icon']
            temp = round(convert_to_celsius(weather_data['main']['temp']))
            icon = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"

            obj = Weather_check(Location=location, main=main, icon=icon, temperature=temp)
            obj.save()

            weather_data = {'main': main, 'icon': icon, 'temp': temp}
            return render(request, 'weather_data.html', {'weather_data': weather_data})

        except KeyError:
            error_message = "Invalid input"
            return render(request, 'sample.html', {'error': error_message})

    return render(request, 'sample.html')

def logout_fun(request):
    logout(request)
    return redirect('/')
