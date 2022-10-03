from django.shortcuts import render, redirect, get_object_or_404
#moje
from .models import Produkty, Kategoria,Oferty, Producent, Sklepy, Konto, Powiadomienia, Promocje, Powiadomienia_produkt
from django.http import HttpResponse, HttpResponseRedirect
from .forms import Search, Register, LoginAuthForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from .decorators import unauthentcated_user
from django.contrib.auth.models import User
from django.urls import reverse



# Create your views here.


def index(request):
    #zapytanie = Produkty.objects.all()
    kategorie = Kategoria.objects.all()
    search = Search()
    dane = {'kategorie': kategorie, 'search': search, }

    if request.user.is_authenticated: #licznik powiadomień
        konto = Konto.objects.get(user=request.user)
        promo = Powiadomienia.objects.filter(status=False, konto=konto)
        #for obiekt in promo:
            #print(obiekt)
        dane['promo'] = promo #licznik promocji
        powiadomienia = Powiadomienia_produkt.objects.filter(status=False, konto=konto)
        dane['powiadomienia'] = powiadomienia #licznik powiadomień

    return render(request, 'start.html', dane)









def kategoria(request, id):
    kategoria_user = Kategoria.objects.get(pk=id)
    kategoria_produkt = Produkty.objects.filter(kategoria = kategoria_user)
    kategorie = Kategoria.objects.all()
    search = Search()
    dane = { 'kategoria_user': kategoria_user, 'kategoria_produkt': kategoria_produkt, 'kategorie': kategorie, 'search': search, }

    if request.user.is_authenticated:
        konto = Konto.objects.get(user=request.user)
        promo = Powiadomienia.objects.filter(status=False, konto=konto)
        dane['promo'] = promo  #licznik promocji
        powiadomienia = Powiadomienia_produkt.objects.filter(status=False, konto=konto)
        dane['powiadomienia'] = powiadomienia #licznik powiadomień

    return render(request, 'kategoria_produkt.html', dane)








def produkt(request, id):
    produkt_user = Produkty.objects.get(pk=id)
    #print(produkt_user)
    kategorie = Kategoria.objects.all()
    oferty = Oferty.objects.filter(produkt = produkt_user)
    search = Search()
    dane = {'produkt_user': produkt_user, 'kategorie': kategorie, 'oferty': oferty, 'search': search, }


    if request.user.is_authenticated: #dla zalogowanego użytkownika
        konto = Konto.objects.get(user=request.user)
        produkt_konto = produkt_user.konto_set.filter(user=request.user) #sprawdza, czy PRODUKT jest obserwowany przez zalogowanego uzytkownika
        #for prod in produkt_konto:
            #print(prod)
        dane['konto'] = konto
        dane['produkt_konto'] = produkt_konto

        if not produkt_konto: #jeśli produkt nie jest obserwowany, to mogą być oferty. Sprawdzenie, czy sa jakieś obserwowane OFERTY.
            oferty_konto = Oferty.objects.filter(konto=konto, produkt=produkt_user).prefetch_related('konto_set').prefetch_related('produkt')
            #for of in oferty_konto:
                #print(of)
            dane['oferty_konto'] = oferty_konto

         # licznik promocji
        promo = Powiadomienia.objects.filter(status=False, konto=konto)
        dane['promo'] = promo


        powiadomienia = Powiadomienia_produkt.objects.filter(status=False, konto=konto)
        dane['powiadomienia'] = powiadomienia #licznik powiadomień




    return render(request, 'produkt.html', dane)






def szukaj(request): #WYSZUKIWARKA!!!!!
    if request.method == "GET":
        search = Search(request.GET)
        form = request.GET['wyszukaj']
        #search = Search(request.POST)
        #form = request.POST.get('wyszukaj')
        kategorie = Kategoria.objects.all()
        if search.is_valid():                            #Dane do wyszukiwarki.Filtrowanie po:
            nazwy = Produkty.objects.filter(nazwa__contains=form) #nazwie produktu
            producenci = Produkty.objects.filter(producent__nazwa__contains=form).select_related('producent') #nazwie producenta
            categories = Produkty.objects.filter(kategoria__nazwa__contains=form).select_related('kategoria') #nazwach kategorii
            sklepy = Oferty.objects.filter(sklep__nazwa__contains=form).select_related('sklep').select_related('produkt') #nazwie sklepu



            dane = {'search': search, 'nazwy': nazwy, 'producenci': producenci, 'categories': categories, 'sklepy': sklepy, 'kategorie':kategorie, 'form': form,}
            return render(request, 'wyszukiwanie.html', dane)
            #return HttpResponse(search)







@unauthentcated_user
def log(request): #LOGOWANIE!!!!
    dane = {}
    if request.method == "POST":
        log = LoginAuthForm(request, data=request.POST)
        if log.is_valid():
            username = log.cleaned_data.get('username')
            password = log.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
        else:
            dane['log'] = log #wysyła błędy formularza


    else:
        log = LoginAuthForm()
        dane['log'] = log

    return render(request, 'logowanie.html', dane )






@unauthentcated_user
def register(request):  #REJESTRACJA!!!!!
    dane = {}
    if request.method == "POST":
        register = Register(request.POST)
        if register.is_valid():
            user = register.save()
            username = register.cleaned_data.get('email')
            password = register.cleaned_data.get('password1')
            account = authenticate(username=username, password=password)
            login(request, account)
            Konto.objects.create(user=user,)

            messages.success(request, 'Rejestracja przebiegła pomyślnie')
            #username = request.POST['username']
            #password = request.POST['password']
            #zaloguj = authenticate(request, username=username, password=password)
            #if zaloguj is not None:
                #login(request, zaloguj)
            return redirect("/dziekujemy_za_zaufanie")

        else:
            dane['register'] = register #wysyła błędy formularza



    else:
        register = Register()
        dane['register'] = register
    return render(request, 'rejestracja.html', dane )



@login_required
def dziekujemy(request):
    return render(request, 'dziekujemy.html', {})







@login_required
def logout_view(request): #WYLOGUJ!!!!!!!
    logout(request)
    return redirect("/")




@login_required
def profil(request, id):
    #user = get_username(User)
    kategorie = Kategoria.objects.all()
    search = Search()
    #obserwuj=obserwuj()

    #rzeczy dotyczące konta
    konto = Konto.objects.get(user=request.user)
    print(konto.user.first_name)
    produkty = konto.produkty.all()
    oferty = konto.oferty.all().select_related('produkt')
    #user = request.user
    #konto = Konto.objects.filter(user= user)
    #konto = Konto.objects.filter(user=user).select_related('user').select_related('produkty').select_related('oferty')
    dane = {'kategorie':kategorie, 'search': search, 'produkty': produkty, 'oferty': oferty, }

     #licznik promocji
    promo = Powiadomienia.objects.filter(status=False, konto=konto)
    dane['promo'] = promo

    powiadomienia = Powiadomienia_produkt.objects.filter(status=False, konto=konto)
    dane['powiadomienia'] = powiadomienia  # licznik powiadomień

    return render(request, 'profil.html', dane )





@login_required
def zapisz(request, id):
    produkt_zapisz = get_object_or_404(Produkty, id=request.POST.get('produktid'))
    konto = Konto.objects.get(user=request.user)
    oferty_konto = Oferty.objects.filter(konto=konto, produkt=produkt_zapisz).prefetch_related('konto_set').prefetch_related('produkt')
    if oferty_konto:
        for oferta in oferty_konto:
            print(oferta)
        for oferta in oferty_konto:
            konto.oferty.remove(oferta)
    konto.produkty.add( produkt_zapisz )
    print(produkt_zapisz)

    #return HttpResponse('<h1>Page was found</h1>')
    return HttpResponseRedirect(reverse('produkt', args=[str(id)]))





@login_required
def usun_produkt(request, id):
    produkt_usun = get_object_or_404(Produkty, id=request.POST.get('produktid'))
    konto = Konto.objects.get(user=request.user)
    print(produkt_usun )
    konto.produkty.remove( produkt_usun )
    return HttpResponseRedirect(reverse('produkt', args=[str(id)]))

    #return HttpResponse('<h1>Page was found</h1>')




@login_required
def promocje(request, id):
    kategorie = Kategoria.objects.all()
    search = Search()
    konto = Konto.objects.get(user=request.user)
    promo = Powiadomienia.objects.filter(status=False, konto=konto)
    powiadomienia = Powiadomienia_produkt.objects.filter(status=False, konto=konto)



    for elem in promo: #po wyświetleniu strony zapisuje informacje, ze powiadomienie zostalo wyświetlone.
        elem.status = True
        elem.save()



    powiadomienia_stare = Powiadomienia.objects.filter(status=True, konto=konto)


    dane = {'kategorie': kategorie, 'search': search, 'promo': promo, 'powiadomienia_stare':powiadomienia_stare, 'powiadomienia ': powiadomienia, }
    return render(request, 'promocje.html', dane )


@login_required
def powiadomienia(request, id):
    kategorie = Kategoria.objects.all()
    search = Search()
    konto = Konto.objects.get(user=request.user)
    promo = Powiadomienia.objects.filter(status=False, konto=konto)
    powiadomienia = Powiadomienia_produkt.objects.filter(status=False, konto=konto)


    for elem in powiadomienia: #po wyświetleniu strony zapisuje informacje, ze powiadomienie zostalo wyświetlone.
        elem.status = True
        elem.save()

    powiadomienia_stare = Powiadomienia_produkt.objects.filter(status=True, konto=konto)


    dane = {'kategorie': kategorie, 'search': search, 'promo': promo,'powiadomienia_stare':powiadomienia_stare, 'powiadomienia': powiadomienia  }
    return render(request, 'powiadomienia.html', dane )




@login_required
def promocje_stare(request, id):
    kategorie = Kategoria.objects.all()
    search = Search()
    konto = Konto.objects.get(user=request.user)
    powiadomienia_stare = Powiadomienia.objects.filter(status=True, konto=konto)
    powiadomienia = Powiadomienia_produkt.objects.filter(status=False, konto=konto)



    dane = {'kategorie': kategorie, 'search': search, 'powiadomienia_stare': powiadomienia_stare, 'powiadomienia': powiadomienia,}
    return render(request, 'promocje_stare.html', dane )

@login_required
def powiadomienia_stare(request, id):
    kategorie = Kategoria.objects.all()
    search = Search()
    konto = Konto.objects.get(user=request.user)
    promo = Powiadomienia.objects.filter(status=False, konto=konto)
    powiadomienia_stare = Powiadomienia_produkt.objects.filter(status=True, konto=konto)


    dane = {'kategorie': kategorie, 'search': search, 'powiadomienia_stare': powiadomienia_stare, 'promo':promo, }
    return render(request, 'powiadomienia_stare.html', dane )








@login_required
def zapisz_oferta(request, id):
    produkt_zapisz = get_object_or_404(Oferty, id=request.POST.get('produktid'))
    konto = Konto.objects.get(user=request.user)
    konto.oferty.add( produkt_zapisz )

    #return HttpResponse('<h1>Page was found</h1>')
    return HttpResponseRedirect(reverse('produkt', args=[str(id)]))

@login_required
def usun_oferta(request, id):
    produkt_usun = get_object_or_404(Oferty, id=request.POST.get('produktid'))
    konto = Konto.objects.get(user=request.user)
    print(produkt_usun )
    konto.oferty.remove( produkt_usun )
    return HttpResponseRedirect(reverse('produkt', args=[str(id)]))

@login_required
def usun_oferty_all(request, id):

    produkt_zapisz = get_object_or_404(Produkty, id=request.POST.get('produktid'))
    konto = Konto.objects.get(user=request.user)
    oferty_konto = Oferty.objects.filter(konto=konto, produkt=produkt_zapisz).prefetch_related(
        'konto_set').prefetch_related('produkt')
    if oferty_konto:
        for oferta in oferty_konto:
            print(oferta)
        for oferta in oferty_konto:
            konto.oferty.remove(oferta)
    return HttpResponseRedirect(reverse('produkt', args=[str(id)]))

