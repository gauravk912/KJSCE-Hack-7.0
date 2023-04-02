# -*- coding: utf-8 -*-
"""Player_Country.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qfd4HesAF1AasqcXkq2YsPmQB2Rv44dH
"""

import pandas as pd
import numpy as np

data = pd.read_csv('match_data_3.csv')
data.head()

data = data.dropna()

data.isna().sum()

data.columns

data.dtypes

data = data.astype({'runs_given':'float64'})

data['ECO'] = data['runs_given']/data['overs']

data['ECO'] = data['ECO'].fillna(0)
data.head()

## name and team_name
player_country = data.loc[ : , ['name', 'team_name']]

player_country = player_country.drop_duplicates()

## player_country contains what you need

player_country['name'].value_counts()

player_country.head(30)

player_country.set_index('name')

i = 0
player_country["Average_strike_rate"] = 0.0
print(player_country.columns)


for row in player_country['name']:
  # print(row)
  row = str(row)
  # print(type(row))
  # hi = "Shubman Gill"
  average_strike_rate = cdata.get_group(row)['strike_rate'].mean()
  # print(average_strike_rate)
  # print(player_country.columns)
  player_country['Average_strike_rate'][i] = average_strike_rate
  # print(row, cdata.get_group(row)['ECO'])
  average_ECO = cdata.get_group(row)['ECO'].mean()
  #print(average_ECO)
  player_country['Average_ECO'] = average_ECO

  #if player_country['name']==
  i+=1

# print(player_country.head())

cdata = data.groupby('name')
# print(cdata["ECO"].mean())
xdata = pd.DataFrame({'Average_ECO': cdata['ECO'].mean()})
xdata.head()

# xdata.columns.values[1] = "ECO"

player_country['Average_ECO'] = xdata['Average_ECO'].values

#player_country = player_country.drop(["ECO"], axis = 1)
player_country.head()

# player_country = player_country.astype({'Average_ECO':'float64'})

# player_country["Average_ECO"].unique()

player_country.head()



A = player_country.loc[:,['name','team_name', 'Average_ECO','Average_strike_rate']].values  ## will add ECO here
B = player_country.loc[:,['Average_runs_scored']]