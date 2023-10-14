import pandas as pd
import re

# read in our data
df = pd.read_csv('data.csv')

# drop any duplicates caused by different types tags
df = df.drop_duplicates('name', ignore_index=True)

# make sure the column types are casted as booleans
df['serves_breakfast'] = df['serves_breakfast'].astype(dtype=bool)
df['serves_dinner'] = df['serves_dinner'].astype(dtype=bool)

# Drop any false values to create DataFrames for each meal
breakfast = df[df['serves_breakfast'] == True]
lunch = df[df['serves_lunch'] == True]
dinner = df[df['serves_dinner'] == True]

breakfast = breakfast.sort_values(by=['rating'])
lunch = lunch.sort_values(by=['rating'])
dinner = dinner.sort_values(by=['rating'])


# Write them to their own files
breakfast.to_csv('breakfast.csv')
lunch.to_csv('lunch.csv')
dinner.to_csv('dinner.csv')

print(lunch)