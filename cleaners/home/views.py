from django.shortcuts import render, redirect
from .forms import EstimateForm
from .models import Quotation


def home(request):
    context = {
        'modalform': EstimateForm
    }

    return render(request, "home.html", context)


def addQuotation(request):
    form = EstimateForm(request.POST)

    if form.is_valid():
        form.save(Quotation)

    return redirect('home')

# Create your views here.


def cor(request):
    return render(request, 'courosels.html')