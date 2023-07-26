from django.shortcuts import render

def home_fun(request):
    return render(request, 'home.html')