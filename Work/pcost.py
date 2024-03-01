# pcost.py
#
# Exercise 1.27

import sys


def portfolio_cost(filename):
    ...
    # Your code here
    ...


if len(sys.argv) == 2:
    filename = sys.argv[1]
    print("Filename:", filename)
else:
    filename = "Data/portfolio.csv"
    print("argv" + sys.argv[0])

cost = portfolio_cost(filename)
print("Total cost:", cost)
