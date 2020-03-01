from os import chdir, getcwd     # needed to specify where the pictures should go
from . import file_numberer      # Used to name the images of plots [graph(number).png]
import matplotlib.pyplot as plt
from numpy import *

path = getcwd()
chdir(path+'//calculator//traph')
# file_number = file_numberer.get_number() the current image number

def plot_it(equation):                                           # ploting the function using matplotlib
    file_number = file_numberer.get_number()

    plt.style.use('seaborn')

    plt.cla()

    x = linspace(0, 5, 100)
    y = eval(equation)

    plt.plot(x, y)
    plt.axhline(y=0, color='black')
    plt.axvline(x=0, color='black')
    plt.ylabel("y")
    plt.xlabel("x")
    plt.title(equation)
    file_name = f'static/calculator/graphs/graph{file_number}.png'
    plt.savefig(file_name)


def graph_it(equation):
    file_number = file_numberer.get_number()

    chdir(path+'//calculator')                   # Changing the placement


    plot_it(equation)                    # making and saving the graph

    file_number += 1                     # Increasing the number for the fututre image

    with open('traph/file_numberer.py', 'w') as numberer:                       # Saving the future number
        text = f"def get_number():\n    number = {file_number}\n    return number"
        numberer.write(text)
