import os                     # needed to specify where the pictures should go
from . import file_numberer   # Used to name the images of plots [graph(number).png]
from shutil import copy       # to get copied to static/calculator/graphs
# getting the path (if you found a better way, tell me)
path = os.getcwd()
os.chdir(path+'//calculator//traph')

def graph_it(equation):

    file_number = file_numberer.get_number() # the current image number

    # Because the equation is in string, it'll be written on a plot.py so that it would be unstringed
    # Sorry for the complexity and mess, happen you found a better way, I'll be grateful if you tell me

    with open('plot.py', 'w') as ploter:
        text = f"import matplotlib.pyplot as plt \nfrom numpy import * \nx = linspace(1, 5, 100) \ny = {equation} \nplt.plot(x, y) \nfile_name = 'graphs/graph{file_number}.png' \nplt.savefig(file_name)"
        ploter.write(text)

    from . import plot                   # Running the plot.py

    file_number += 1                     # Increasing the number for the fututre image

    with open('file_numberer.py', 'w') as numberer:                       # Saving the future number
        text = f"def get_number():\n    number = {file_number}\n    return number"
        numberer.write(text)

    os.chdir(path+'//calculator')                   # Changing the placement
    copy(f'traph/graphs/graph{file_number-1}.png', 'static/calculator/graphs')
