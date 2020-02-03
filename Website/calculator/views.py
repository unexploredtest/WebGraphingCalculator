from django.shortcuts import render
from django.http import HttpResponse


def calculator(request):
    return render(request, 'calculator/calculator.html')
