# -*- coding: utf-8 -*-
"""
EDIT - EXPLORATORY FACTOR ANALYSIS
ANDRÉ AREOSA - FINAL VERSION
"""

# PART I

# 1 - (c)
# 2 - (b)
# 3 - (a)
# 4 - (b)

# PART II 

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# READ CSV FILE ON PYTHON
imported_file = r'C:\Users\andre\Downloads\amazonas.csv'
data = pd.read_csv(imported_file)
print(data.head())

# Number = Number of fires by state 

# DATA SHAPE
data.shape

# CHECK FOR MISSING VALUES
data.info()

# Exercise 1 : To check minimum and maximum of ‘year’ column
data_min = data["year"].min()
data_max = data["year"].max()

print(f'Min: {data_min}')
print(f'Max: {data_max}')


# Exercise 2 :To find out total number of fires in ‘Acre’ state and 
# visualizing data based on each ‘year’
acre_state = data[data['state'] == 'Acre']
acre_year = acre_state.groupby('year', as_index=False)['number'].sum()
print(acre_year)

sns.barplot(x='year', y='number', data=acre_year, color='blue')
plt.xticks(rotation='vertical')
plt.show()

# Exercise 3: To find out total number of fires in all states
all_states = data.groupby(['state'])['number'].count()
print(all_states)

# Exercise 4 : To find out total number of fires in 2017 and visualizing 
# data based on each ‘month’
data_2017 = data[data['year'] == 2017]
month_fires = data_2017.groupby('month', as_index=False).agg({'number': 'sum'})
print(month_fires)

sns.barplot(x='month', y='number', data=month_fires, color='blue', order=['Janeiro', 'Fevereiro', 'Marco', 'Abril',
                   'Maio', 'Junho', 'Julho', 'Agosto',
                  'Setembro', 'Outubro', 'Novembro', 'Dezembro'])
plt.xticks(rotation='vertical')
plt.show()

# Exercise 5 : To find out average number of fires occurred
data_mean = data["number"].mean()

print('Mean: {d:1.0f} fires'.format(d = data_mean))


#  Exercise 6 : To find out the state names where fires occurred in 
# ‘December’ month
december_fire_states = []

for index, row in data.iterrows():
    if row["month"] == 'Dezembro':
        december_fire_states.append(row["state"])
  
state_names_december = sorted(set(december_fire_states))
print(state_names_december)
      


















