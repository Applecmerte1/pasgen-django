from django.contrib import admin
from generator import views as views_gen
from django.urls import path
from countsym import views as views_sym

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views_gen.main),
    path('countword/',views_sym.count),
    path('genpassword/', views_gen.home),
    path('genpassword/generatedpassword/', views_gen.password, name ='home11'),
    path('me/', views_gen.me,name = 'its me'),
    #все что в name это просто имя которое передается через {%(и тут имя с html%}
]