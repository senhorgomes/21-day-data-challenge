# What are the top 5 boardgame categories in this dataset that are not targeted for young children?
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('boardgames.csv')
filterage = df['age'] >= 13
grouped = df[filterage].groupby('category').count().sort_values(by=['names'], ascending=[False])
grouped.head()
plt.figure()
plt.bar(x = grouped.head().index, height = grouped.head()['names'])
plt.xticks(rotation = 'vertical')
plt.show()
# Which categories of boardgames that are not targeted for young children are the same compared to the top 5 boardgames categories in the overall dataset?

unfiltered = df.groupby('category').count().sort_values(by=['names'], ascending=[False])
plt.bar(x = unfiltered.head().index, height = unfiltered.head()['names'])
plt.xticks(rotation = 'vertical')
plt.show()
