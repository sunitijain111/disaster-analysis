import pandas as pd
import numpy

dataset= pd.read_csv("dataset/dataset1.csv")
temp= dataset

drought_set = dataset.loc[dataset["Disaster Type"] == "Drought"]
drought_set.drop(drought_set.columns[0], inplace = True, axis= 1)
drought_set.dropna(axis=0, inplace= True)
import matplotlib.pyplot as plt 

  
plt.plot(drought_set['Year'], drought_set[drought_set.columns[3]]) 
plt.xlabel('year')
plt.ylabel('people affected') 
plt.title('drought in world total damage') 
plt.show() 
## partial code
