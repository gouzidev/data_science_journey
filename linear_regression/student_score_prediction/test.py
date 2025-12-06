from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

data = [
    {"size": 50, "bedrooms": 1, "age": 10, "price": 120000},
    {"size": 60, "bedrooms": 2, "age": 8,  "price": 150000},
    {"size": 80, "bedrooms": 2, "age": 5,  "price": 200000},
    {"size": 100,"bedrooms": 3, "age": 2,  "price": 260000},
    {"size": 120,"bedrooms": 3, "age": 1,  "price": 300000},
    {"size": 70, "bedrooms": 2, "age": 15, "price": 140000},
    {"size": 90, "bedrooms": 3, "age": 12, "price": 210000},
    {"size": 110,"bedrooms": 4, "age": 3,  "price": 310000},
]

df = pd.DataFrame(data)


X = df[['size', 'bedrooms', 'age']]

y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.25, shuffle=True)

lr = LinearRegression()

lr.fit(X_train, y_train)

lr_test_pred = lr.predict(X_test)


mse = mean_squared_error(y_test, lr_test_pred)

r2 = r2_score(y_test, lr_test_pred)

print("mse -> ", mse)
print("r2 -> ", r2)

# plt.show()

plt.scatter(y_test, lr_test_pred)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted House Prices")
plt.show()