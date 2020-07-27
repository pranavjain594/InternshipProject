# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 15:38:28 2020

@author: KIIT
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

##STEP 1###
#importing dataset as data
data=pd.read_csv('data.csv')

#getting data information
data.describe()
data.head()
data.tail()
data.info()
data.shape

#getting non null data
data[data.notnull()]

#checking for the null values as a boolean series
bool_series = pd.isnull(data)  
print(bool_series)

#getting the number of null values in each column
data.isnull().values.any()
data.isnull().sum()

##STEP 2###
#dropping irrelevant columns
data.drop(['Market Category', 'Engine Fuel Type', 'Number of Doors'], axis=1,inplace=True)

##STEP 3###
#renaming the columns
data.rename(columns = {'Engine HP':'HP','Engine Cylinders':'Cylinders','Transmission Type':'Transmission','Driven_Wheels':'Drive Mode','highway MPG':'MPG-H','city mpg':'MPG-C','MSRP':'Price'}, inplace = True) 
print(data.columns)

##STEP 4###
#checking for the duplicate data and dropping the duplicates by just keeping the first row
len(data.duplicated())
data[data.duplicated()]
data.drop_duplicates(keep="first", inplace=True)

#check if there's any duplicate column
data.columns.duplicated()

#imputing missing values with the mean value
data.fillna(data.mean(), inplace=True)
print(data.mean())
data.isnull().sum()
data.count()

##STEP 5###
#Plotiing graph to check for outliers in each column
  
sns.boxplot(x=data['Year'])
sns.boxplot(x=data['HP'])
sns.boxplot(x=data['Cylinders'])
sns.boxplot(x=data['MPG-H'])
sns.boxplot(x=data['MPG-C'])
sns.boxplot(x=data['Popularity'])
sns.boxplot(x=data['Price'])

#Removing outliers using IQR method    

#printing IQR values of different columns
Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)
IQR = Q3 - Q1
print(IQR)

print((data < (Q1 - 1.5 * IQR)) |(data > (Q3 + 1.5 * IQR)))

#Eliminating the outliers
data = data[~((data < (Q1 - 1.5 * IQR)) |(data > (Q3 + 1.5 * IQR))).any(axis=1)]
data.shape

##STEP 6###
#FInding Car brand with maximum count in data
data['Make'].value_counts()

#Finding average(mean) of price of the different car brands
data.groupby('Make')['Price'].mean()

#Plotting the above calculated mean for each brand
data.groupby('Make')['Price'].mean().plot(kind='bar')
plt.show()

