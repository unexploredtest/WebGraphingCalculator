import matplotlib.pyplot as plt 
from numpy import * 
x = linspace(1, 5, 100) 
y = 55*x 
plt.plot(x, y) 
file_name = 'graphs/graph12.png' 
plt.savefig(file_name)