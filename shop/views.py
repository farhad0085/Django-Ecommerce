from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    return HttpResponse("Hello")

def shop_home(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, template_name='shop/shop_home.html', context=context)

def shop_item_details(request, *args, **kwargs):
    return render(request, template_name='shop/shop_item_details.html')