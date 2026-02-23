from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from numpy import exp
from Przygotowanie_Danych import x, y
import pandas as pd


x_train, x_test = train_test_split(x, test_size=0.2, random_state=43)
y_train, y_test = train_test_split(y, test_size=0.2, random_state=43)


model = LinearRegression()

# Trenowanie modelu na danych treningowych
model.fit(x_train, y_train)

# Przewidywanie wartości zmiennej zależnej dla danych testowych
y_pred = model.predict(x_test)
y_pred = pd.Series(y_pred)


y_test = y_test.apply(exp)
y_pred = y_pred.apply(exp)


