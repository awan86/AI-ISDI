# Supervised Learning
# from sklearn.linear_model import LinearRegression
# import numpy as np
# import pandas as pd
# Data Collection
# x = np.array([[1],[2],[3],[4],[5]])
# y = np.array([2,4,6,8,10])
# Model Selection
# model = LinearRegression()
# Model Training
# model.fit(x, y)
# Model Prediction
# prediction=model.predict([[10]])
# print("Prediction for 6 hrs", prediction)

# from sklearn.linear_model import LinearRegression
# import numpy as np
# x = np.array([[1000000],[2000000],[3000000],[4000000],[5000000]])
# y = np.array([1,2,3,4,5])
# model = LinearRegression()
# model.fit(x,y)
# prediction = model.predict([[int(input("Enter the value"))]])
# print("Predicted Value of House:", prediction)

# Un-Supervised Learning
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# import numpy as np
# Data Collection
# x = np.array([[1],[2],[3],[4],[5],[6],[7],[8]])
# y = np.array([15,30,45,60,75,90,105,120])
# Data Cleaning (split data)
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
# Model Selection
# model = LinearRegression()
# Model Training
# model.fit(x_train, y_train)
# Model Prediction
# prediction = model.predict(x_test)
# print("Actual:", y_test)
# print("Prediction:", prediction)

# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# import numpy as np
# x = np.array([[1],[2],[3],[4],[5]])
# y = np.array([20,40,60,80,100])
# model = LinearRegression()
# model.fit(x,y)
# prediction = model.predict([[int(input("Enter the value"))]])
# print("Predicted Marks:", prediction)

# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import r2_score
# import numpy as np
# x = np.array([[1],[2],[3],[4],[5]])
# y = np.array([20,35,70,100,110])
# x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)
# model = LogisticRegression()
# model.fit(x_train, y_train)
# prediction = model.predict(x_test)
# score = r2_score(y_test, prediction)
# print("Actual:", y_test)
# print("Prediction:", prediction)
# print("Score:", score)

# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import r2_score
# import numpy as np
# x = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
# y = np.array([20,35,50,65,80,95,110,125,140,155])
# x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)
# model = LogisticRegression()
# model.fit(x_train, y_train)
# prediction = model.predict(x_test)
# score = r2_score(y_test, prediction)
# print("Actual:", y_test)
# print("Prediction:", prediction)
# print("Score:", score)

# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import r2_score
# import numpy as np
# x = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
# y = np.array([0,1,1,1,1,1,0,0,0,0])
# x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)
# model = LogisticRegression()
# model.fit(x_train, y_train)
# prediction = model.predict(x_test)
# score = r2_score(y_test, prediction)
# print("Actual:", y_test)
# print("Prediction:", prediction)
# print("Score:", score)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np
x = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
y = np.array([0,1,1,1,1,1,0,0,0,0])
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(x_train, y_train)
prediction = model.predict(x_test)
score = r2_score(y_test, prediction)
print("Actual:", y_test)
print("Prediction:", prediction)
print("Score:", score)