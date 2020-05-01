from django.shortcuts import render
from django.http import HttpResponse
from .models import Products,Offer


def index(request):
    products=Products.objects.all()
    return render(request,'index.html',{'products':products})


def offers(request):
    offers = Offer.objects.all()
    return render(request, 'offers.html', {'offers': offers})


def wishlist(request):
    products=Products.objects.all
    return render(request,'wishlist.html',{'products':products})


def my_orders(request):
    return HttpResponse('These are the products that you have ordered')


def transactions(request):
    return HttpResponse('The transactions that has done so far ')


def filters(request):
    return HttpResponse('Filters that you needed')


def homepage(request):
    return render(request,'homepage.html')