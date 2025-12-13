import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from numpy import sqrt
import matplotlib.pyplot as plt

#Dane Kategoryczne 1
def location(l):
    if l == "Downtown":
        return "Good_loc"
    elif l == "Suburban":
        return "Medium_loc"
    elif l == 'Rural':
        return "Bad_loc" 
def parking(p):
    if p == "Yes":
        return 1
    elif p == "No":
        return 0
def cuisine(c):
    if c in ['American', 'Italian']:
        return 1
    else:
        return 0
    

data = pd.read_csv("restaurant_data2.csv")

#Dane Kategoryczne 2
data["PA"] = data['PA'].apply(parking)
data['Location'] = data["Location"].apply(location)
data['Rev2'] = (data['R'] * data['NOR'])/data['SMF']
data['Cuisine_popular'] = data['Cuisine'].apply(cuisine)
columns = data.columns.tolist()
columns.insert(columns.index('Location') + 1, columns.pop(columns.index('Cuisine_popular')))
data = data[columns]



x_num = data[['R', 'SC', 'AMP', 'MB', 'SMF',
              'CEY', 'AS','NOR', 'SQS', 'PA',
               'WENDR', 'WDAYR', 'Rev2' ]]


x_text = pd.get_dummies(data['Location'],drop_first=True)

x = pd.concat([x_num, x_text], axis = 1)
y = data['Revenue']

x_train, x_test = train_test_split(x, test_size=0.2, random_state=43)
y_train, y_test = train_test_split(y, test_size=0.2, random_state=43)


model = LinearRegression()

# Trenowanie modelu na danych treningowych
model.fit(x_train, y_train)

# Przewidywanie wartości zmiennej zależnej dla danych testowych
y_pred = model.predict(x_test)


#scory

print("do 1", r2_score(y_test, y_pred))
print("do 0", sqrt(mean_squared_error(y_test, y_pred)))
print("dp 0", mean_absolute_error(y_test, y_pred))


'''
# Wykres punktowy
plt.scatter(y_test, y_pred, color='blue')

# Prosta na wykresie
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--', label='Idealne dopasowanie')

# Etykiety osi x i y, tytuł, legenda, siatka
plt.xlabel('Wartości obserwowane')
plt.ylabel('Wartości dopasowane')
plt.title('Wykres wartości dopasowanych i obserwowanych modelu regresji liniowej')
plt.legend()
plt.grid()

# Wyświetlenie wykresu
plt.show()
'''