import matplotlib.pyplot as plt 
from numpy import * 
x = linspace(1, 5, 100) 
y = log(x) 
plt.plot(x, y) 
file_name = 'graphs/graph8.png' 
plt.savefig(file_name)