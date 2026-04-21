# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression, LogisticRegression
# from sklearn.metrics import r2_score, accuracy_score, confusion_matrix
# import numpy as np
# x=np.array([[st_hour==int(input("Enter your studied hours")),attendance==int(input("Enter your attendance score?")),assignment_score==int(input("Enter your assignment score?"))],
#             [st_hour==int(input("Enter your studied hours")),attendance==int(input("Enter your attendance score?")),assignment_score==int(input("Enter your assignment score?"))],
#             [st_hour==int(input("Enter your studied hours")),attendance==int(input("Enter your attendance score?")),assignment_score==int(input("Enter your assignment score?"))],
#             [st_hour==int(input("Enter your studied hours")),attendance==int(input("Enter your attendance score?")),assignment_score==int(input("Enter your assignment score?"))],
#             [st_hour==int(input("Enter your studied hours")),attendance==int(input("Enter your attendance score?")),assignment_score==int(input("Enter your assignment score?"))],
#             [st_hour==int(input("Enter your studied hours")),attendance==int(input("Enter your attendance score?")),assignment_score==int(input("Enter your assignment score?"))],
#             [st_hour==int(input("Enter your studied hours")),attendance==int(input("Enter your attendance score?")),assignment_score==int(input("Enter your assignment score?"))],
#             [st_hour==int(input("Enter your studied hours")),attendance==int(input("Enter your attendance score?")),assignment_score==int(input("Enter your assignment score?"))],
#             [st_hour==int(input("Enter your studied hours")),attendance==int(input("Enter your attendance score?")),assignment_score==int(input("Enter your assignment score?"))],
#             [st_hour==int(input("Enter your studied hours")),attendance==int(input("Enter your attendance score?")),assignment_score==int(input("Enter your assignment score?"))],
#             [st_hour==int(input("Enter your studied hours")),attendance==int(input("Enter your attendance score?")),assignment_score==int(input("Enter your assignment score?"))]
# ])
# y=np.array([0,1,1,1,1,1,0,0,0,0])
# x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)
# model = LogisticRegression()
# model.fit(x_train, y_train)
# prediction = model.predict(x_test)
# score = r2_score(y_test, prediction)
# print("Actual:", y_test)
# print("Prediction:", prediction)
# print("Score:", score)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import r2_score, accuracy_score, confusion_matrix
import numpy as np
x=np.array([[1,10,20],[2,20,30],[3,30,40],[4,40,50],[5,50,60],[6,60,70],[7,70,80],[8,80,90],[9,90,100],[10,100,110]])
y=np.array([0,1,1,1,1,1,0,0,0,0])
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3, random_state=42)
model = LogisticRegression()
model.fit(x_train, y_train)
prediction = model.predict(x_test)
cm = confusion_matrix(y_test, prediction)
accuracy = accuracy_score(y_test, prediction)
print("Confusion Matrix:", cm)
print("Accuray:", y_test)
print("Prediction:", prediction)

hours = int(input("Enter your Studied Hours: "))
attendance = int(input("Enter your Attendance: "))
assignment = int(input("Enter your Assignment: "))
# conversion of input into array
user_data = np.array([[hours, attendance, assignment]])
# prediction
prediction = model.predict(user_data)
print("Prediction:", prediction)

if prediction[0] == 1:
    print("You are Pass")
else:
    print("You are Fail")