import numpy as np
import matplotlib.pyplot as plt 

a=[]
b=[]

for x in range(1,100,1):
    y=(100/x)+x
    a.append(x)
    b.append(y)

fig= plt.figure()
axes=fig.add_subplot(111)
axes.plot(a,b)
plt.show()
