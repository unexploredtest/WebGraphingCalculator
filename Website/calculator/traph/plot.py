import matplotlib.pyplot as plt 
from numpy import * 
plt.style.use('seaborn') 
x = linspace(1, 5, 100) 
y = cos(x) 
plt.plot(x, y) 
file_name = 'graphs/graph24.png' 
plt.savefig(file_name)