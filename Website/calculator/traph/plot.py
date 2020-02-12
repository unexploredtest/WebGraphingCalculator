import matplotlib.pyplot as plt 
from numpy import * 
x = linspace(1, 5, 100) 
y = sqrt(x) 
plt.plot(x, y) 
file_name = 'graphs/graph2.png' 
plt.savefig(file_name)