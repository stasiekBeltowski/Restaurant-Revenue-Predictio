from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from numpy import sqrt
import matplotlib.pyplot as plt
from Przygotowanie_Danych import data, x, y


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