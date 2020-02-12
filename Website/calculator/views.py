from django.shortcuts import render
from django.http import HttpResponse
from .forms import TextEquation
from .traph import grapher                  # The function that will grapg the equation


def calculator(request):

    if request.method == 'POST':

        form = TextEquation(request.POST)
        if form.is_valid():
            equation = form.cleaned_data.get('equation') # Getting the equation that the user had written
            grapher.graph_it(equation)

    else:
        form = TextEquation()
        equation = 'null'



    return render(request, 'calculator/calculator.html', {'form': form, "equation": equation})
