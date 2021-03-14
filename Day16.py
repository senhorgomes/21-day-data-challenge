# Create a boxplot to answer the following questions:

# How many books have over 4000 pages?

# Note: Do not use a fitler, use a boxplot.

# What are the average ratings for books that have over 4000 pages?

# Note: You can use a filter for question 2.

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("books.csv")
df
plt.figure()
plt.boxplot(df['num_pages'])
plt.show
booksOver4000 = df['num_pages'] > 4000
ratingsOver4000 = df[booksOver4000]
ratingsOver4000

# Answer: 2 Books, with an average rating of 4.70 and 4.45