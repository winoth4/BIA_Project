import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Step: 1 Load the dataset
df=pd.read_csv('mumbai-monthly-rains.csv')
print(df.info())
print("Data heads:")
print(df.head())

# Step 2: Data cleaning
 # check for missing values 
print("Null values in the dataset before preprocessing:")
print(df.isnull().sum())

 # handling missing values (example: fill with mean)
print("Filling null values with mean of that particular column")
df.fillna(df.mean(),inplace=True)
print("Mean of data:")
print(np.mean(df))
print("Null values in the dataset after preprocessing:")
print(df.isnull().sum())
print("\n\nShape: ",df.shape)

df.Year.unique()
#Step: 3 Exploratory data analyzes EDA
# sns.pairplot(df)

# plt.figure(figsize=(15,6))
# sns.heatmap(df.corr(),cmap='RdBu',vmin=-1,vmax=1,annot=True)
# plt.show()
# #correlation:
# print("Co-Variance =",df.cov())
# print("Co-Relation =",df.corr())
# corr=df.corr()
# print(corr['Total'])

# print("Scatter plot of annual and january attributes")
# plt.scatter(df.Total,df.Aug)
# plt.show()

# print("Box Plot of annual rainfall data in years 1901-2015")
# df['Total'].plot(kind='box',sharex=False,sharey=False)

# simple historical graphs to see which period has most rainfall
df.hist(figsize=(13,13))
plt.show()

#Yearwise variation from june to september
variation_jun_sep = df.groupby('YEAR')[['Jun-Sep']].plot(figsize=(13,13))