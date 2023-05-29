#%%
import pandas as pd

#%% Create sample table
data = {
    'Name': ['Zhang San', 'Li Si', 'Wang Wu', 'Zhang San', 'Li Si', 'Wang Wu'],
    'Region': ['Beijing', 'Beijing', 'Shanghai', 'Shanghai', 'Shanghai', 'Beijing'],
    'Sales': [10, 8, 12, 5, 7, 6]
}
df = pd.DataFrame(data)
df

#%% Question 1: Rearrange the table using the pivot function
pivot_table = df.pivot(index='Name', columns='Region', values='Sales')
print(pivot_table)

#%% Question 2: Rearrange the table using the melt function
melted_table = df.melt(id_vars=['Name', 'Region'], value_vars='Sales')
print(melted_table)
# %%
