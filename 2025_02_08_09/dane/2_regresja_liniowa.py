import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('dane\\otodom.csv')
print(df)

print(df.describe().T.to_string())

print(df.iloc[:,1:].corr())
sns.heatmap(df.iloc[:,2:].corr(),annot=True)
plt.show()

sns.histplot(df.price)
plt.show()
plt.scatter(df.space,df.price)
plt.show()

q3 = df.describe().loc['price','75%']
print(q3)

df1 = df[df.price <= q3]
plt.hist(df1.price, bins=50)
plt.show()