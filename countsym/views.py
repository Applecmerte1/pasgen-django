from django.shortcuts import render
from django.http import HttpResponse

def count(request): 
    text1 = request.GET.get('type')
    sumb = list()
    if text1!=None:
        for i in text1:
            if i.isalpha()==True:
                sumb.append(i)
    print(len(sumb))
    return render(request, 'countsym/countsumbol.html')