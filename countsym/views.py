from django.shortcuts import render
from django.http import HttpResponse

def count(request):
    sumb = list()
    a = 0
    text1 = request.GET.get('type')
    a = text1.replace(('!"№;%:?*()@#$^&'), '')
    print(a)
    return render(request, 'countsym/countsumbol.html')