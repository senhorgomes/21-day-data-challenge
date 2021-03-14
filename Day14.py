import pandas as pd
df = pd.read_csv('winequality-red_2.csv')
df = df.drop(columns = ['Unnamed: 0'])
# How many wines from Stellenbosch are there in the *entire dataset*? 
user_filter = df['region'] == 'Stellenbosch'
filtered_df = df[user_filter]
filtered_df.count()
# Answer = 35
# After filtering with the 2 conditions, what is the average price of wine from the Bordeaux region?
filtered_conditions = (df['region'] == 'Bordeaux') & (df['sulphates'] <= 0.6) & (df['price'] < 20)
price_filter = df[filtered_conditions]
price_filter['price'].mean()
# Answer = 11.30
# *After filtering with the 2 conditions*, what is the least expensive wine that's of the highest quality from the Okanagan Valley?
filtered_conditions = (df['region'] == 'Okanagan Valley') & (df['sulphates'] <= 0.6) & (df['price'] < 20)
price_filter = df[filtered_conditions]
price_filter.sort_values(by=['price','quality'], ascending = [True,False])
# Answer = Wine 1025
