#importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#loading data
df=pd.read_csv('Diwali Sales Data.csv',encoding='latin1')
print(df.head())

#Basic exploration
print('\n The shape of the data is :\n')
print(df.shape)

print("\n The column of the dataset is :\n")
print(df.columns)
print('\n The information of the dataset is :\n')
print(df.info())

print('\nchecking for the null values\n')
print(df.isnull().sum())

#status ,amount and  unmamed1 colum have some null values

#filing the null values into unknown

df['Status']=df['Status'].fillna('unknown')
df['unnamed1']=df['unnamed1'].fillna('unknown')
df['Amount']=df['Amount'].fillna('0')
print(df.isnull().sum())

df['Amount'] = pd.to_numeric(df['Amount'])



gender_count=df['Gender'].value_counts()
print(gender_count)

gender_count.plot(kind='pie',autopct='%1.1f%%')
plt.title('Genders')
plt.ylabel('')
plt.legend()
plt.tight_layout()
plt.savefig('Gender Distribution.png',dpi=300,bbox_inches='tight')
plt.show()

age_group=df['Age Group'].value_counts()
print(age_group)

age_group.plot(kind='bar',color='skyblue',label='Age group')
plt.title('Age group ')
plt.xlabel('Age group')
plt.ylabel('number')
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig('Age_group_distribution.png',dpi=300,bbox_inches='tight')
plt.show()

df['Marital_Status']=df['Marital_Status'].replace({0:'Single',1:'Married'})
marital_status=df['Marital_Status'].value_counts()
print(marital_status)

marital_status.plot(kind='pie',autopct='%1.1f%%')
plt.title('Marital Status')
plt.ylabel('')
plt.legend()
plt.tight_layout()
plt.savefig('marital_status_distribution.png',dpi=300,bbox_inches='tight')
plt.show()


order_by=df.groupby('Marital_Status')['Orders'].sum()
print(order_by)
order_by=order_by.sort_values(ascending=False)
order_by.plot(kind='bar',color='purple')
plt.title('married vs single order ')
plt.xlabel('marital status')
plt.ylabel('order value')
plt.tight_layout()
plt.savefig('orders_based_on_marital_status.png',dpi=300,bbox_inches='tight')
plt.show()

#top states based on orders
states=df.groupby('State')['Orders'].count().sort_values(ascending=False)
print(states)
top_5_states=states.head().sort_values(ascending=True)
top_5_states.plot(kind='barh',color='seagreen')
plt.title('Top 5 states by orders')
plt.xlabel('orders count')
plt.ylabel('States')
plt.tight_layout()
plt.savefig('top_5_states_by_order.png',dpi=300,bbox_inches='tight')
plt.show()

#top customers based on amount
top_customers=df.groupby('Cust_name')['Amount'].sum().sort_values(ascending=False)
print(top_customers)
top_5_customers=top_customers.head().sort_values(ascending=True)
top_5_customers.plot(kind='barh',color='maroon')
plt.title('top 5 customers based on amount')
plt.xlabel('Amount')
plt.ylabel('customers name')
plt.tight_layout()
plt.savefig('top_5_customers_based_on_amount.png',dpi=300,bbox_inches='tight')
plt.show()

#top products generating most revenue
top_revenue=df.groupby('Product_Category')['Amount'].sum().sort_values(ascending=False)
top_5_revenue_product=top_revenue.head().sort_values(ascending=True)
top_5_revenue_product.plot(kind='barh',color='wheat')
plt.title('top 5 revenue generating product')
plt.xlabel('Amount')
plt.ylabel('Products')
plt.tight_layout()
plt.savefig('top_revenue_generating_product.png',dpi=300,bbox_inches='tight')
plt.show()

#average order value based on gender
order_by_gender=df.groupby('Gender')['Amount'].mean()
order_by_gender.plot(kind='pie',autopct='%1.1f%%')
plt.title('Average order value based on gender')
plt.ylabel('')
plt.tight_layout()
plt.savefig('Average_order_on_gender_basis.png',dpi=300,bbox_inches='tight')
plt.show()

#age group that spend the most money
money_spending=df.groupby('Age Group')['Amount'].sum()
money_spending.plot(kind='bar',color='beige')
plt.title("Age group that spends the most money ")
plt.xlabel('Age groups')
plt.ylabel('money')
plt.tight_layout()
plt.savefig('Most_money_spending_agegroup.png',dpi=300,bbox_inches='tight')
plt.show()