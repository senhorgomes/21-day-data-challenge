# What is the correlation coefficient between Critic_Score and User_Score?
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('video_games.csv')
df.head()
df['Critic_Score'].corr(df['User_Score'])
# Answer: 0.4785731396832123
# Note: You may have to clean some of the columns and fill it with the median value (if numerical).
# Plot the top 5 best selling games released before the year 2000.
filteryear = df['Year_of_Release'] < 2000
newdf = df[filteryear].sort_values(by=['Global_Sales'], ascending=[False])
plt.figure()
plt.bar(x = newdf.head()['Name'], height = newdf.head()['Global_Sales'])
plt.xticks(rotation='vertical')
plt.show()
# Answer: SMB, Pokemon Red/Blue...

# Note: Use Global_Sales
# Create a new column called Aggregate_Score, which returns the proportional average between Critic Score and User_Score based on Critic_Count and User_Count. Plot a horizontal bar chart of the top 5 highest rated games by Aggregate_Score, not published by Nintendo before the year 2000. From this bar chart, what is the highest rated game by Aggregate_Score?
df['Critic_Count'].fillna(df['Critic_Count'].mean(), inplace=True)
df['User_Count'].fillna(df['User_Count'].median(), inplace=True)
df['User_Score'] = df['User_Score']*10
df['Aggregate_Score'] = (df['Critic_Count'] * df['Critic_Score'] + df['User_Count'] * df['User_Score']) / (df['Critic_Count'] + df['User_Count'])
scorefilter = (df['Year_of_Release'] < 2000) & (df['Publisher'] != 'Nintendo')
scoredf = df[scorefilter].sort_values(by=['Aggregate_Score'], ascending = False).head()
plt.figure()
plt.barh(y= scoredf['Name'], width= scoredf['Aggregate_Score'])
plt.show()
# Answer: METAL GEAR SOLID

