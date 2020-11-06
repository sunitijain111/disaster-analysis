import pandas as pd
import numpy

dataset= pd.read_csv("dataset/dataset1.csv")
temp= dataset

drought_set = dataset.loc[dataset["Disaster Type"] == "Drought"]
drought_set.drop(drought_set.columns[0], inplace = True, axis= 1)
drought_set.dropna(axis=0, inplace= True)
drought_set.sort_values("Year", axis = 0, ascending = True, inplace = True, na_position ='last') 
import matplotlib.pyplot as plt 

  
plt.plot(drought_set['Year'], drought_set[drought_set.columns[3]]) 
plt.xlabel('year')
plt.ylabel('people affected') 
plt.title('drought in world total damage') 
plt.show() 


plt.plot(drought_set['Year'], drought_set[drought_set.columns[4]]) 
plt.xlabel('year')
plt.ylabel('damage in USD') 
plt.title('drought in world total cost in USD') 
plt.show() 

a= drought_set[drought_set.columns[4]]/ drought_set[drought_set.columns[3]]

plt.plot(drought_set['Year'], a) 
plt.xlabel('year')
plt.ylabel('cost per person ') 
plt.title('drought in world per person cost in USD') 
plt.show() 


drought_set["cost per person "]= a

print(drought_set[drought_set.columns[3]].mean()  )
print(drought_set[drought_set.columns[4]].mean()  )
print(drought_set[drought_set.columns[5]].mean()  )
print(drought_set.info())
#121