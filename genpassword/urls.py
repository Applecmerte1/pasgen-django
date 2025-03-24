from django.contrib import admin
from generator import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('generatedpassword/', views.password, name ='home11'),
    path('me/', views.me,name = 'its me'),
    #все что в name это просто имя которое передается через {%(и тут имя с html%}
]