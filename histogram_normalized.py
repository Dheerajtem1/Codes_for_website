import numpy as np
import matplotlib.pyplot as plt
from math import*
import random as rd
d=[rd.randint(0,10) for i in range(1000)]

def histogram_normalized(x,number_of_bin):                                                   
    y=np.histogram(x,number_of_bin)
    quan=[]
    quan_h=[]                                                                          #This function here takes a list x and no. of bins and gives a normalized data which
    for i in range(1,len(y[1])):                                                       #can be used to plot a histogram.
        quan.append(y[1][i]-y[1][i-1])
        quan_h.append((y[1][i]+y[1][i-1])/2)
    q_arr=np.array(quan)
    q_h_array=np.array(quan_h)
    new_var=q_arr*y[0]
    area=np.sum(new_var)
    dummy_y=[y[0][i]/area for i in range(len(y[0]))]
    outp=[quan_h,dummy_y]
    return outp

term=histogram_normalized(d,10)
x=term[0]
y=term[1]
plt.plot(x,y,"go")
Y=[x[i] for i in range(len(x))]
plt.show()
