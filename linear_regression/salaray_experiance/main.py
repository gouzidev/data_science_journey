import pandas as pd
from random import randint
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import  StandardScaler


df  = pd.read_csv("./Salary_Data.csv")
# detect missing values 
# print(df.isna().sum()) # must give 0

sc = StandardScaler()

X = df[["YearsExperience"]]

y = df[["Salary"]]

X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=True, random_state=randint(0, 100))

X_train_scaled = sc.fit_transform(X_train)

X_test_scaled = sc.transform(X_test)

lr = LinearRegression()

lr.fit(X_train_scaled, y_train)

res = lr.predict(X_test_scaled)

validYoEx = False

while not validYoEx:
    try:
        yoex = input("please enter your years of experiance to get the prediction -> ")
        yoex = float(yoex)
        validYoEx = True

    except:
        print(">> your years of experiance must be a valid float.")


new_data = pd.DataFrame({'YearsExperience': [yoex]})

new_pred = lr.predict(sc.transform(new_data))

salary_pred  = float(new_pred[0][0]) / 1000

print(f"your salary for your {yoex} years of experiance will be ${salary_pred:.2f}k")