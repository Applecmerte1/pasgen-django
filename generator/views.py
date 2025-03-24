from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')
def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase') == 'on':
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    if request.GET.get('special') == 'on':
        characters.extend('!"№;%:?*()@#$^&')

    if request.GET.get('numbers') == 'on':
        characters.extend('1234567890')
        
    lenght = int(request.GET.get('length'))
    thepassword = ''

    for i in range(lenght):
        thepassword+=random.choice(characters)

    return render(request, 'generator/password.html',{'password':thepassword})
def me(request):
    return render(request, 'generator/me.html')