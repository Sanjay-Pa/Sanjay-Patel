import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#import superstore dataset
superstore_df=pd.read_csv(r'C:\Users\Sanjay patel\Downloads\SampleSuperstore.csv')
superstore_df
superstore_df.head()
superstore_df.shape
superstore_df.columns
superstore_df.info()
superstore_df.isnull().sum()
print(superstore_df['Category'].unique())
print(superstore_df['State'].unique())
no_of_states=superstore_df['State'].nunique()
print("There are %d states in this df."%no_of_states)
print(superstore_df['Sub-Category'].unique())
no_of_subcategory=superstore_df['Sub-Category'].nunique()
print("Categories are divided into %d subcategories"%no_of_subcategory)
superstore_df['Segment'].value_counts()
loss_df = superstore_df[superstore_df['Profit'] < 0]
loss_df
loss_df.shape
loss_df.describe()
Total_loss=np.negative(loss_df['Profit'].sum())
print("Total loss = %.2f" %Total_loss)
loss_df.groupby(by='Segment').sum()
loss_df.groupby(by='Sub-Category').sum()
loss_df['Sub-Category'].value_counts()
loss_df.groupby(by='City').sum().sort_values('Profit',ascending=True).head(10)
loss_df.sort_values(['Sales'],ascending=True).groupby(by='Category').mean()
superstore_df.groupby(['State']).sum()['Sales'].nsmallest(10)
superstore_df.sort_values(['Segment'],ascending=True).groupby('Segment').sum()
superstore_df.groupby(by='Region').sum()
plt.rcParams['figure.figsize']=(15,3)
plt.bar(loss_df['Sub-Category'],loss_df['Sales']);
plt.rcParams.update({'font.size':10});
plt.xlabel('Sub_Category');
plt.ylabel('Sales');
plt.rcParams['figure.figsize']=(28,8)
plt.bar(superstore_df['Sub-Category'],superstore_df['Sales']);
plt.rcParams.update({'font.size':14});
plt.xlabel('Sub_Category');
plt.ylabel('Sales');
plt.rcParams['figure.figsize']=(28,8)
plt.bar(superstore_df['Sub-Category'],superstore_df['Discount']);
plt.rcParams.update({'font.size':14});
plt.xlabel('Sub_Category');
plt.ylabel('Discount');
plt.rcParams['figure.figsize']=(10,8)
plt.bar(superstore_df['Ship Mode'],superstore_df['Sales']);
plt.rcParams.update({'font.size':14});
plt.xlabel('Ship Mode');
plt.ylabel('Sales');
plt.rcParams['figure.figsize']=(10,5)
sns.countplot(x=superstore_df.Segment)
plt.show();
plt.rcParams['figure.figsize']=(20,5)
plt.rcParams.update({'font.size':12})
sns.countplot(x='Sub-Category',data=superstore_df)
plt.show()
plt.rcParams['figure.figsize']=(20,5)
plt.rcParams.update({'font.size':12})
sns.countplot(x='Region',data=superstore_df)
plt.show()
superstore_df.corr()
sns.heatmap(superstore_df.corr(),cmap='Reds',annot=True);
plt.rcParams['figure.figsize']=(10,5)

