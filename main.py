import matplotlib.pyplot as plt
import numpy as np
import csv
from scipy.interpolate import CubicSpline
import sys

x=[]
y=[]

plt.ioff() #deactivate interactive
plt.figure(figsize=(15, 6))
with open(sys.argv[1]) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if int(row['Iteration'])!= 0:
            x.append(int(row['Iteration']))
            y.append(int(row['CellCount']))

#define spline
spl = CubicSpline(x, y)
arr = np.arange(np.amin(x), np.amax(x), 0.1)

plt.plot(arr, spl(arr), marker='') #plot said spline
plt.xlabel("Iteration")
plt.ylabel("Anzahl Zellen")
plt.title("Verlauf von einer Conway-Simulation")
plt.savefig(sys.argv[2])