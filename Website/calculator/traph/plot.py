import matplotlib.pyplot as plt 
from numpy import * 
plt.style.use('seaborn') 
x = linspace(0, 5, 100) 
y = sin(x) 
plt.plot(x, y) 
plt.axhline(y=0, color='black')
plt.axvline(x=0, color='black') 
file_name = 'graphs/graph34.png' 
plt.savefig(file_name)