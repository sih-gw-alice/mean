import pandas as pd
COLOUR="red"
dataframe = pd.read_csv("rgb.csv")


coloured = dataframe[COLOUR]
print(coloured.means())
