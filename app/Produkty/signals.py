from django.db.models.signals import post_save, post_delete, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import *



@receiver(post_save, sender=Promocje)
def save_new_promo(sender, instance, created, **kwargs):
    if created:
        #print('sender', sender)
        #print('instance', instance.oferta)
        #print('created', created)
        oferta_do_zmiany = instance.oferta
        oferta_do_zmiany.promocyjna_cena = instance.nowa_cena #wysyła do bazy danych oferty informacje o przecenie
        oferta_do_zmiany.save()

        produkt_oferta = oferta_do_zmiany.produkt
        user_produkty = produkt_oferta.konto_set.all() #wszystkie konta obserwujące produkt


        if user_produkty:
            for elem in user_produkty:
                #print(elem)
                a = Powiadomienia.objects.create(konto = elem)
                a.oferta = instance.oferta
                a.treść = f'Produkt jest teraz na promocji. Oferta ważna do {instance.data_zakonczenia}'
                a.status = False
                a.save()



        user_oferty = oferta_do_zmiany.konto_set.all() #wszystkie konta obserwujące oferte

        if user_oferty:
            for elem in user_oferty:
                a = Powiadomienia.objects.create(konto = elem)
                a.oferta = instance.oferta
                a.treść = f'Produkt jest teraz na promocji. Oferta ważna do {instance.data_zakonczenia}'
                a.status = False
                a.save()


#@receiver(post_save, sender=Promocje)
# delete _promo(sender, instance, created, **kwargs):
    #if instance.data_zakonczenia == datetime.now():
        #print(instance.data_zakonczenia)


@receiver(pre_delete, sender=Promocje)
def delete_promo(sender, instance, **kwargs):
    print('instance', instance)
    oferta_do_zmiany = instance.oferta
    oferta_do_zmiany.promocyjna_cena = None  # kasuje informacje o przecenie z bazy ofert
    oferta_do_zmiany.save()


    Promo_usun = Powiadomienia.objects.filter(oferta=oferta_do_zmiany)
    for elem in Promo_usun:
        elem.delete()



@receiver(pre_delete, sender=Produkty)
def delete_produkt(sender, instance, **kwargs):
    print('instance', instance)


    obserwujacy = instance.konto_set.all()
    if obserwujacy:
        for elem in obserwujacy:
            print(elem)
            a = Powiadomienia_produkt.objects.create(konto=elem)
            a.zdjecie = instance.zdjecie
            a.treść = f'Przepraszamy. Produkt {instance.nazwa}, którym byłeś zainteresowany nie jest już dostępny na naszej stronie.'
            a.status = False
            a.save()




@receiver(pre_delete, sender=Oferty)
def delete_oferta(sender, instance, **kwargs):
    print('instance', instance)


    obserwujacy = instance.konto_set.all()
    if obserwujacy:
        for elem in obserwujacy:
            print(elem)
            a = Powiadomienia_produkt.objects.create(konto=elem)
            a.zdjecie = instance.produkt.zdjecie
            a.treść = f'Przepraszamy. Oferta sklepu {instance.sklep}, dotycząca produktu {instance.produkt}, którą byłeś zainteresowany nie jest już dostępna na naszej stronie.'
            a.status = False
            a.save()

    produkt = instance.produkt
    obserwujacy_produkt = produkt.konto_set.all()
    if obserwujacy_produkt:
        for elem in obserwujacy_produkt:
            print(elem)
            a = Powiadomienia_produkt.objects.create(konto=elem)
            a.treść = f'Przepraszamy. Oferta sklepu {instance.sklep}, dotycząca produktu {instance.produkt}, którą byłeś zainteresowany nie jest już dostępna na naszej stronie.'
            a.status = False
            a.save()

















