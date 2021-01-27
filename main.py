import csv
import sys

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline

plt.ioff()  # deactivate interactive
plt.figure(figsize=(15, 6))

filecount = len(sys.argv) - 4

# subtract count due to the nature of range starting at 0 and sys.argv starting at 1
for currentFile in range(filecount-1):
    x = []
    y = []
    with open(sys.argv[currentFile+5]) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if int(row['Iteration']) != 0:
                x.append(int(row['Iteration']))
                y.append(float(row[sys.argv[1]]))
    
    #to beautify the graph (reacting on "SkipFirstIteration" argument)
    if "true" == sys.argv[4]:
        x.pop(0)
        y.pop(0)
    # define spline
    spl = CubicSpline(x, y)
    arr = np.arange(np.amin(x), np.amax(x), 0.1)
    plt.plot(arr, spl(arr), marker='')  # plot said spline

plt.xlabel("Generation")
plt.ylabel(sys.argv[2])
plt.title("History of a Conway simulation")
plt.savefig(sys.argv[3])
