import pandas as pd
import numpy

dataset= pd.read_csv("dataset/dataset1.csv")
temp= dataset

flood_set = dataset.loc[dataset["Disaster Type"] == "Flood"]
flood_set.drop(flood_set.columns[0], inplace = True, axis= 1)
flood_set.dropna(axis=0, inplace= True)
flood_set.sort_values("Year", axis = 0, ascending = True, inplace = True, na_position ='last') 


import matplotlib.pyplot as plt 

  
plt.plot(flood_set['Year'], flood_set[flood_set.columns[3]]) 
plt.xlabel('year')
plt.ylabel('people affected') 
plt.title('flood in world total damage') 
plt.show() 


plt.plot(flood_set['Year'], flood_set[flood_set.columns[4]]) 
plt.xlabel('year')
plt.ylabel('damage in USD') 
plt.title('flood in world total cost in USD') 
plt.show() 

a= flood_set[flood_set.columns[4]]/ flood_set[flood_set.columns[3]]
plt.plot(flood_set['Year'], a) 
plt.xlabel('year')
plt.ylabel('cost per person ') 
plt.title('flood in world cost per person in USD') 
plt.show() 



flood_set["cost per person "] =a

print(flood_set[flood_set.columns[3]].mean()  )
print(flood_set[flood_set.columns[4]].mean()  )
print(flood_set[flood_set.columns[5]].mean()  )
print(flood_set.info())
