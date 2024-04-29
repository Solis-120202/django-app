from django.shortcuts import render
from django.shortcuts import render

# Create your views here.from django.shortcuts import render
from .models import client
from .models import transaction

# Create your views here.

def client_list(request):
    clients = client.objects.all()
    return render(request, "finance/clients.html", {"clients": clients})

def transactions_list(request):
    transactions = transaction.objects.all()
    return render(request, "finance/transactions.html", {"transactions":transactions})