from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello")

def shop_home(request, *args, **kwargs):
    return render(request, template_name='shop/shop_home.html')

def shop_item_details(request, *args, **kwargs):
    return render(request, template_name='shop/shop_item_details.html')