import pandas as pd

myDataSet = {
    'animals': ['bear', 'koala', 'kitty'],
    'numbers': [1, 3, 13]
}

myDataFrame = pd.DataFrame(myDataSet)

print(myDataFrame)