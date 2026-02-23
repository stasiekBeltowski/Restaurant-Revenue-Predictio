from Model import y_test, y_pred, x_train,model
import pandas as pd
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error, mean_absolute_percentage_error
from numpy import sqrt

'''
#Relacja Miedzy AMP a Location
correlation = x_train[['Good_loc', 'AMP', 'SC']].corr()
print(correlation)
'''

#Moc zmiennych niezależnych
importance = pd.DataFrame({
    'Feature': x_train.columns,
    'Coefficient': model.coef_
})

print(importance)


#scory

print("R2", r2_score(y_test, y_pred))
print("RMSE", sqrt(mean_squared_error(y_test, y_pred)))
print("MAE", mean_absolute_error(y_test, y_pred))
print("MAPE", mean_absolute_percentage_error(y_test, y_pred))


