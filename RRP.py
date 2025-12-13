import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from numpy import sqrt
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error


data = pd.read_csv("Restaurant_data.csv")
x = data[['Rating', 'Seating Capacity',  'Marketing Budget' ,
         'Social Media Followers',
         'Ambience Score',  'Weekend Reservations',
         'Weekday Reservations' 
          ]]

y = data['Revenue']

x_train, x_test = train_test_split(x, test_size=0.19, random_state=42)
y_train, y_test = train_test_split(y, test_size=0.19, random_state=42)


lr_model = LinearRegression()

# Trenowanie modelu na danych treningowych
lr_model.fit(x_train, y_train)

# Przewidywanie wartości zmiennej zależnej dla danych testowych
y_pred_lr = lr_model.predict(x_test)


#scory

print("do 1", r2_score(y_test, y_pred_lr))
print("do 0", sqrt(mean_squared_error(y_test, y_pred_lr)))
print("dp 0", mean_absolute_error(y_test, y_pred_lr))



