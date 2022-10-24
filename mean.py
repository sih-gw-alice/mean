import pandas as pd
COLUMN="red"
dataframe = pd.read_csv("rgb.csv")

subset = dataframe[COLUMN]
print(subset.means()) 

