import pandas as pd
import numpy

dataset= pd.read_csv("dataset/dataset1.csv")
temp= dataset

flood_set = dataset.loc[dataset['Country'] == "India"]
flood_set = flood_set.loc[flood_set["Disaster Type"] == "Flood"]
flood_set.drop(flood_set.columns[0], inplace = True, axis= 1)
flood_set.dropna(axis=0, inplace= True)

import matplotlib.pyplot as plt 
#partial code
