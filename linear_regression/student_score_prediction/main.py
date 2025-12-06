from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split

df = pd.read_csv("./student_exam_scores.csv", dtype="str")


X = df[['hours_studied', 'sleep_hours', 'attendance_percent', 'previous_scores']]

y = df['exam_score']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.2, shuffle=True)

lr = LinearRegression()

lr.fit(X_train, y_train)

lr_test_pred = lr.predict(X_test)

y_test_numeric = y_test.astype(float)
lr_test_pred_numeric = lr_test_pred.astype(float)

plt.figure(figsize=(6,6))
plt.scatter(y_test_numeric, lr_test_pred_numeric)
plt.plot([0, 100], [0, 100], linestyle='--')  # diagonal line
plt.xlabel("Actual Exam Score")
plt.ylabel("Predicted Exam Score")
plt.title("Actual vs Predicted Exam Scores")
plt.grid(True)
plt.show()