import pandas as pd
import matplotlib.pyplot as plt
from Model import y_test, y_pred


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
