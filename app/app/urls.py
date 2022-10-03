"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#moje

from Produkty.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('kategoria/<id>', kategoria, name='kategoria'),
    path('produkt/<id>/', produkt, name='produkt'),
    path('search/', szukaj, name='szukaj'),
    path('logowanie/', log, name='login'),
    path('rejestracja/', register, name='rejestracja'),
    path('wyloguj/', logout_view, name='wyloguj'),
    path('profil/<id>/', profil, name='profil'),
    path('save/<id>/', zapisz, name='zapisz'),
    path('delete/<id>/', usun_produkt, name='usun'),
    path('promocje/<id>/', promocje, name='promocje'),
    path('save_offert/<id>/', zapisz_oferta, name='zapisz_oferta'),
    path('delete_offert/<id>/', usun_oferta, name='usun_oferta'),
    path('delete_all/<id>/', usun_oferty_all, name='usun_oferty_all'),
    path('twoje_promocje/<id>/', promocje_stare, name='twoje_promocje'),
    path('powiadomienia/<id>/', powiadomienia, name='powiadomienia'),
    path('twoje_powiadomienia/<id>/', powiadomienia_stare, name='powiadomienia_stare'),
    path('dziekujemy_za_zaufanie/', dziekujemy, name='dziekujemy'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
