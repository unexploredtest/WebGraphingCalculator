from django.shortcuts import render
from django.http import HttpResponse
from .forms import TextEquation
from .traph import grapher, file_numberer    # The functions that will graph the equation and tell us the number


def calculator(request):

    if request.method == 'POST':

        form = TextEquation(request.POST)
        if form.is_valid():
            equation = form.cleaned_data.get('equation') # Getting the equation that the user had written
            image_number = file_numberer.get_number()    # Getting the number
            grapher.graph_it(equation)                   # Graphing the function

    else:
        form = TextEquation()
        equation = 'null'
        image_number = 3



    return render(request, 'calculator/calculator.html', {'form': form, "equation": equation, 'image_number': image_number})


def login(request):

    return render(request, 'calculator/login.html')
