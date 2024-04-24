from django.urls import path

from shop import views
from shop.views import home, laptop, rassrochka, background, karusel, about, service, serivce, kontakty, otzyvy

app_name = 'main'

urlpatterns = [
    path('', views.karusel, name='home'),
    path('laptop', views.laptop, name='laptop'),
    path('rassrochka', views.rassrochka, name='rassrochka'),
    path('background', views.background, name='background'),
    path('about', views.about, name='about'),
    path('service', views.service, name='service'),
    path('serivce', views.serivce, name='serivce'),
    path('kontakty', views.kontakty, name='kontakty'),
    path('otzyvy', views.otzyvy, name='otzyvy')
]