from django.shortcuts import render

from shop.models import Shop, Laptops, Rassrochka, Background, Karusel, About, Service, Serivce2, Kontakty, Otzyvy


def home(requests):
    shop = Shop.objects.all()
    context = {
        'shop': shop,
    }

    return render(requests, 'base.html', context)


def laptop(requests):
    laptop = Laptops.objects.all()
    context = {
        'laptop': laptop
    }

    return render(requests, 'main/laptop.html', context)


def rassrochka(requests):
    rassrochka = Rassrochka.objects.all()
    context = {
        'rassrochka': rassrochka
    }

    return render(requests, 'main/rassrochka.html', context)

def background(requests):
    background = Background.objects.all()
    context = {
        'background': background
    }

    return render(requests, 'main/rassrochka.html', context)

def karusel(requests):
    karusel = Karusel.objects.all()
    context = {
        'karusel': karusel
    }

    return render(requests, 'main/base.html', context)

def about(requests):
    about = About.objects.all()
    context = {
        'about': about
    }

    return render(requests, 'main/about.html', context)

def service(requests):
    service = Service.objects.all()
    context = {
        'service': service
    }

    return render(requests, 'main/service.html', context)

def serivce(requests):
    serivce = Serivce2.objects.all()
    context = {
        'serivce': serivce
    }

    return render(requests, 'main/service.html', context)

def kontakty(requests):
    kontakty = Kontakty.objects.all()
    context = {
        'kontakty': kontakty
    }

    return render(requests, 'main/kontakty.html', context)

def otzyvy(requests):
    otzyvy = Otzyvy.objects.all()
    context = {
        'otzyvy': otzyvy
    }

    return render(requests, 'main/otzyvy.html', context)
