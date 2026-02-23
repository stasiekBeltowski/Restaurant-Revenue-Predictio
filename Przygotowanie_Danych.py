from Funkcje_Pomocnicze import location, cuisine, parking
import pandas as pd 
from numpy import log
data = pd.read_csv("restaurant_data2.csv")

#Dane Kategoryczne 
data["PA"] = data['PA'].apply(parking)
data['Location'] = data["Location"].apply(location)
data['Rev2'] = (data['R'] * data['NOR'])/data['SMF']
data['Cuisine_popularity'] = data['Cuisine'].apply(cuisine)
columns = data.columns.tolist()
columns.insert(columns.index('Location') + 1, columns.pop(columns.index('Cuisine_popularity')))
data = data[columns]



x_num = data[['R', 'SC', 'AMP', 'MB', 'SMF',
              'CEY', 'AS','NOR', 'SQS', 'PA',
               'WENDR', 'WDAYR', 'Rev2' ]]


x_text = pd.get_dummies(data['Location'],drop_first=True)

x = pd.concat([x_num, x_text], axis = 1)
y = data['Revenue'].apply(log)
