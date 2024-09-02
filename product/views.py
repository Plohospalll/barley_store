from itertools import product

from django.shortcuts import render
from django.http import HttpResponse

from product.models import Product, ProductCategory



# Create your views here.
def index(request):
    productcategory = ProductCategory.objects.all()
    products = Product.objects.all()
    context = {'productCategory': productcategory, 'products': products}
    return render(request, 'index.html', context)
def menu(request):
    productcategory = ProductCategory.objects.all()
    products = Product.objects.all()
    context = {'productCategory': productcategory, 'products': products}
    return render(request, 'menu.html', context)
def about(request):
    return render(request, 'about.html')
def service(request):
    return render(request, 'service.html')
def team(request):
    return render(request, 'team.html')
def testimonial(request):
    return render(request, 'testimonial.html')
