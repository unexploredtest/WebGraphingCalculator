from django.shortcuts import render
from django.http import HttpResponse
from .forms import TextEquation


def calculator(request):

    if request.method == 'POST':

        form = TextEquation(request.POST)
        if form.is_valid():
            equation = form.cleaned_data.get('equation') # Getting the equation that the user had written
            # Here would go the function that will graph the equation

    else:
        form = TextEquation()
        equation = 'null'



    return render(request, 'calculator/calculator.html', {'form': form, "equation": equation})
