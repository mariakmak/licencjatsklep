from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Producent(models.Model):
    def __str__(self):
        return self.nazwa

    nazwa = models.CharField(max_length=100)

    class Meta():
        verbose_name = "Producent"
        verbose_name_plural = "Producenci"




class Kategoria(models.Model):
    def __str__(self):
        return self.nazwa

    nazwa = models.CharField(max_length=100)

    class Meta():
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"





class Sklepy(models.Model):
    def __str__(self):
        return self.nazwa

    nazwa = models.CharField(max_length=100)

    class Meta():
        verbose_name = "Sklep"
        verbose_name_plural = "Sklepy"





class Produkty(models.Model):
    #wyświetlanie nazwy
    def __str__(self):
        return self.nazwa

    zdjecie = models.ImageField(null=True, blank=True)
    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE, null=True)
    producent = models.ForeignKey(Producent, on_delete=models.CASCADE, null=True)
    nazwa = models.CharField(max_length=100)
    sklepy = models.ManyToManyField(Sklepy, through='Oferty')

#poprawki do nazwy tabeli
    class Meta():
        verbose_name = "Produkt"
        verbose_name_plural = "Produkty"


class Oferty(models.Model):


    produkt = models.ForeignKey(Produkty, on_delete=models.CASCADE, null=True)
    sklep = models.ForeignKey(Sklepy, on_delete=models.CASCADE, null=True)
    cena = models.DecimalField(max_digits=12, decimal_places=2)
    promocyjna_cena = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)


    def __str__(self):
        return f"{self.produkt.nazwa}- {self.sklep.nazwa}"



    class Meta():
        verbose_name = "Oferta"
        verbose_name_plural = "Oferty"





class Promocje(models.Model):
    oferta = models.ForeignKey(Oferty, on_delete=models.CASCADE, null=True)
    nowa_cena = models.DecimalField(max_digits=12, decimal_places=2)
    data_rozpoczecia = models.DateTimeField(auto_now_add=True)
    data_zakonczenia = models.DateTimeField()

    def __str__(self):
        return f"{self.oferta}-{self.nowa_cena}"



    class Meta():
        verbose_name = "Promocja"
        verbose_name_plural = "Promocje"












class Konto(models.Model):
    #wyświetlanie nazwy

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    produkty = models.ManyToManyField(Produkty)
    oferty = models.ManyToManyField(Oferty)
    #imie = models.CharField(max_length=100)
    #nazwisko = models.CharField(max_length=100)
    #email = models.EmailField()
    #data_dolaczenia = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


#poprawki do nazwy tabeli
    class Meta():
        verbose_name = "Konto"
        verbose_name_plural = "Konta"



class Powiadomienia(models.Model):
    konto = models.ForeignKey(Konto, null=True, on_delete=models.CASCADE)
    oferta = models.ForeignKey(Oferty, null=True, on_delete=models.CASCADE)
    treść = models.TextField(blank=False)
    status = models.BooleanField(null=True)
    data = models.DateTimeField(auto_now_add=True)



#poprawki do nazwy tabeli
    class Meta():
        verbose_name = "Powiadomienie"
        verbose_name_plural = "Powiadomienia"


class Powiadomienia_produkt(models.Model):
    zdjecie = models.ImageField(null=True, blank=True)
    konto = models.ForeignKey(Konto, null=True, on_delete=models.CASCADE)
    treść = models.TextField(blank=False)
    status = models.BooleanField(null=True)
    data = models.DateTimeField(auto_now_add=True)



#poprawki do nazwy tabeli
    class Meta():
        verbose_name = "Powiadomienie_Produkt"
        verbose_name_plural = "Powiadomienia_Produkt"


