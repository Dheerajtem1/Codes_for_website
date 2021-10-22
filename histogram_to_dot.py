import numpy as np
import matplotlib.pyplot as plt
from math import*
import random as rd

name_of_file=str(input("Enter name of file = "))
y=np.loadtxt(name_of_file)

y_array=np.array(y)

sorted_y=np.sort(y_array)
min_y=sorted_y[0]
max_y=sorted_y[-1]
bins=int(input("Enter number of bins = "))

bin_width=(max_y-min_y)/bins
X=[min_y+(i*(bin_width/2)) for i in range(1,2*bins,2)]

Y=[]
dummy_var=0
for i in range(len(X)):
    for j in range(dummy_var,len(sorted_y)):
        if sorted_y[j]>min_y+(i*bin_width):
            Y.append(j-dummy_var)
            dummy_var=j
            break

dummy_x=[X[i] for i in range(1,len(X)-1)]
dummy_y=[Y[i] for i in range(2,len(Y))]
#plt.hist(y,bins)
plt.plot(dummy_x,dummy_y)
plt.show()
