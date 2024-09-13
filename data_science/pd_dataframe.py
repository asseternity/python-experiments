import pandas as pd

myDataSet = {
    'animals': ['bear', 'koala', 'kitty'],
    'numbers': [1, 3, 13]
}

myDataFrame = pd.DataFrame(myDataSet)

print(myDataFrame)

myDataFrame2 = pd.DataFrame(myDataSet, index = ['x', 'y', 'z'])

print(myDataFrame2)

print(myDataFrame.loc[1])

print(myDataFrame2.loc['x'])