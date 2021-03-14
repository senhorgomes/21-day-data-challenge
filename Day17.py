# What are the top 5 rated books in the dataset?

# What are the top 5 books with the highest average rating?

# Note: Filter out books that have low ratings_count, for question 2 filter out books with a ratings_count less than the mean.

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("books.csv")

topbooks = df.sort_values(by=['ratings_count'], ascending = [False])
topfive = topbooks.head()
plt.figure()
plt.bar(x = topfive['title'], height = topfive['ratings_count'])
plt.show()
ratingcount = df['ratings_count'].mean()
filterratingcount = df['ratings_count'] > ratingcount
filteredtable = df[filterratingcount]
topratings = filteredtable.sort_values(by=['average_rating'], ascending = [False])
plt.figure()
plt.bar(x = topratings['title'], height = topratings['average_rating'])
plt.show()
