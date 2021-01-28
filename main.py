import csv
import sys
from optparse import OptionParser

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline

args = []
options = None


def parse():
    global args
    global options
    parser = OptionParser(
        "usage: %prog [options] <statToPlot> <output> <file/s>")
    parser.add_option("-c", "--cubic", dest="cubic", default=True,
                      action="store_false", help="deactivate cubic spline")
    parser.add_option("-S", "--show", dest="show", default=False,
                      action="store_true", help="Show graph in matplotlib display")
    parser.add_option("-s", "--skip", dest="skip", default=False, action="store_true",
                      help="Skips first iteration (extreme skews if false)")
    (options, args) = parser.parse_args()
    if (len(args) < 3 or (args[0] == "Heat" and len(args) != 3)):
        parser.error("incorrect number of arguments")


def plot_cell():
    filecount = len(args) - 2
    for currentFile in range(filecount):
        x = []
        y = []
        with open(args[currentFile+2]) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if int(row['Iteration']) != 0:
                    x.append(int(row['Iteration']))
                    y.append(float(row['CellCount']))
        # to beautify the graph (reacting on "SkipFirstIteration" argument)
        if options.skip == True:
            x.pop(0)
            y.pop(0)
        if options.cubic == True:
            # define spline
            spl = CubicSpline(x, y)
            arr = np.arange(np.amin(x), np.amax(x), 0.1)
            plt.plot(arr, spl(arr), marker='')  # plot said spline
        else:
            plt.plot(x, y, marker='')

    plt.xlabel("Generation")
    plt.ylabel("Count of cells")
    plt.title("History of a Conway simulation")
    plt.savefig(args[1])
    if options.show == True:
        plt.show()


def plot_density():
    filecount = len(args) - 2
    for currentFile in range(filecount-1):
        x = []
        y = []
        with open(args[currentFile+2]) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if int(row['Iteration']) != 0:
                    x.append(int(row['Iteration']))
                    y.append(float(row['IterationDensity']))
        # to beautify the graph (reacting on "SkipFirstIteration" argument)
        if options.skip == True:
            x.pop(0)
            y.pop(0)
        if options.cubic == True:
            # define spline
            spl = CubicSpline(x, y)
            arr = np.arange(np.amin(x), np.amax(x), 0.1)
            plt.plot(arr, spl(arr), marker='')  # plot said spline
        else:
            plt.plot(x, y, marker='')
    plt.xlabel("Generation")
    plt.ylabel("Density")
    plt.title("History of a Conway simulation")
    plt.savefig(args[1])
    if options.show == True:
        plt.show()


def plot_heat():
    xPos = []
    yPos = []
    xNeg = []
    yNeg = []
    with open(args[2]) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if int(row['Iteration']) != 0:
                xPos.append(int(row['Iteration']))
                yPos.append(float(row['PositiveHeat']))
                xNeg.append(int(row['Iteration']))
                yNeg.append(float(row['NegativeHeat']))
    # to beautify the graph (reacting on "SkipFirstIteration" argument)
    if options.skip == True:
        xPos.pop(0)
        yPos.pop(0)
        xNeg.pop(0)
        yNeg.pop(0)
    if options.cubic == True:
        # define spline
        spl = CubicSpline(xPos, yPos)
        arr = np.arange(np.amin(xPos), np.amax(xPos), 0.1)
        plt.plot(arr, spl(arr), marker='',
                 label="Positive Heat")  # plot said spline

        spl = CubicSpline(xNeg, yNeg)
        arr = np.arange(np.amin(xNeg), np.amax(xNeg), 0.1)
        plt.plot(arr, spl(arr), marker='',
                 label="Negative Heat")
    else:
        plt.plot(xPos, yPos, marker='',
                 label="Positive Heat")
        plt.plot(xNeg, yNeg, marker='',
                 label="Negative Heat")
    plt.xlabel("Generation")
    plt.ylabel("Heat")
    plt.title("History of a Conway simulation")
    plt.legend()
    plt.savefig(args[1])
    if options.show == True:
        plt.show()


plt.ioff()  # deactivate interactive
plt.figure(figsize=(15, 6))

parse()

if args[0] == "CellCount":
    plot_cell()
elif args[0] == "Density":
    plot_density()
elif args[0] == "Heat":
    plot_heat()
else:
    print("Please enter a valid stat to plot (CellCount, Density, Heat")
