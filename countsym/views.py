from django.shortcuts import render
from django.http import HttpResponse

def count(request):
    return render(request, 'countsym/countsumbol.html')
    a = list()
    if request.GET.get('comment') != 0:
        pass