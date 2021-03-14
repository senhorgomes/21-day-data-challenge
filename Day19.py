import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# What type of distribution does the column avg_time have?

df = pd.read_csv('boardgames.csv')
df.head(3)
plt.figure()
plt.hist(df['avg_time'], bins = 40, range=(0, 1000))
plt.show()

# Do games that have a great avg_rating have longer play times?
filterrating = df[df['avg_rating'] >= 9.0]
plt.figure()
plt.hist(filterrating['avg_time'], bins = 100, range=(0, 500))
plt.show()