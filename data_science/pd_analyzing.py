import pandas as pd

myDataFrame = pd.read_csv('data_science/data.csv')

# print(myDataFrame.head(5))
# print(myDataFrame.tail(5))

print(myDataFrame.info()) # tells: (1) how many rows and columns (2) name of each column, with data type (3) how many noon null values
