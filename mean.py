import pandas as pd
dataframe = pd.read_csv("rgb.csv")
means = dataframe.mean()

blues = dataframe["blue"]
print(blue.means()) 
