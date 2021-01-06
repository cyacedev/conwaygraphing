import matplotlib.pyplot as plt
import numpy as np
import csv
from scipy.interpolate import make_interp_spline, BSpline

x=[]
y=[]

plt.ioff()
with open('maxsim.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if int(row['Iteration'])!= 0:
            x.append(int(row['Iteration']))
            y.append(int(row['CellCount']))

#define spline
xnew = np.linspace(1, len(x), int(len(x)/10)) 
spl = make_interp_spline(x, y)
ynew = spl(xnew)

plt.plot(xnew,ynew, marker='')
plt.xlabel("Iteration")
plt.ylabel("Anzahl Zellen")
plt.title("Verlauf von einer Conway-Simulation")
plt.show()