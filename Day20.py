# What kind of correlation is there between the weight and avg_rating?
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('boardgames.csv')
plt.figure()
plt.scatter(x = df['weight'], y = df['avg_rating'])
plt.show()
# What is the correlation coefficient between the two columns?
df['weight'].corr(df['avg_rating'])
