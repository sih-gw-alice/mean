import pandas as pd
COLUMN = "blue"
dataframe = pd.read_csv("rgb.csv")


subset = dataframe[COLUMN]
print(subset.means()) 
