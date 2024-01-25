#This program will write out a table of the function sin(x) vs x, where x is tabulated between 0 and 2pi with a thousand entries.
import numpy as np
from astropy.table import Table
from tabulate import tabulate

def main():
    x = np.linspace(0.0, np.pi * 2, 1000)
    y = np.sin(x)
    data = Table()
    data["0-2pi"] = x
    data["sin(x)"] = y

    data["0-2pi"].format = "{:.3f}"
    data["sin(x)"].format = "{:.3f}"

    print(data)


if __name__ == "__main__":
    main()

    #fix