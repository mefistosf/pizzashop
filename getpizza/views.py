from django.shortcuts import render_to_response
#from django.http import HttpResponse
from getpizza.models import Pizza
#from getpizza.models import Wallet

def index(request):
    all_pizza = Pizza.objects.all()
#    total_price = Wallet.objects.all()
    print list(all_pizza)
    return render_to_response('index.html', ('pizza_data': all_pizza})


