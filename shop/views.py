from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from shop.models import Product

# Create your views here.

def index(request):
  products = Product.objects.all()
  item_name = request.GET.get('item-name')
  if item_name != '' and item_name is not None:
    products = Product.objects.filter(name__icontains=item_name)
  paginator = Paginator(products, 4)
  page = request.GET.get('page')
  products = paginator.get_page(page)
  return render(request, 'shop/index.html', context={'products': products})