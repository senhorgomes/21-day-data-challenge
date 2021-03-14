# Create a bar graph with Matplotlib that shows each vegetable and the size of the potential harvest that Dot can expect from them.
# Which of Dot's seeds will produce the largest harvest?
import pandas as pd
import matplotlib.pyplot as plt
seeds = {
    'Vegetable' : ['Carrots', 'Tomatoes', 'Potatoes', 'Eggplant', 'Cucumbers'],
    'Seeds_Count' : [300,10,90,100,15],
    'Each_Seed_Produces': [1,140,10,5, 90]
}

df = pd.DataFrame(seeds)
df['potential_harvest'] = df['Seeds_Count'] * df['Each_Seed_Produces']
plt.figure()
plt.bar(x = df['Vegetable'], height = df['potential_harvest'])
plt.show()

# Answer: Tomatoes