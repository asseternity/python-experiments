import pandas as pd

a = [1, 31, 56]

mySeries = pd.Series(a, index = ["x", "y", "z"])

print(mySeries)

calories = { 'day1': 2420, 'day2': 2100, 'day3': 2300}

mySeries2 = pd.Series(calories)

print(mySeries2)