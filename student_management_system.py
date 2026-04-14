# import numpy as np
# student_marks = np.array([["Amir",85, 90, 58],
#                           ["Ali", 42, 80, 65],
#                           ["Ahsan", 80, 45, 52],
#                           ["Sara", 90, 95, 88],
#                           ["Zara", 70, 75, 80]])
# print(student_marks)
# student_marks_mean = np.mean(student_marks)
# print("Mean: ", student_marks_mean)
# student_marks_median = np.median(student_marks)
# print("Median: ", student_marks_median)
# student_marks_avg = np.average(student_marks)
# print("Average: ", student_marks_avg)
# student_marks_min = np.min(student_marks)
# print("Minimum: ", student_marks_min)
# student_marks_max = np.max(student_marks)
# print("Maximum: ", student_marks_max)
# print("Data Type: ", student_marks.dtype)
# if student_marks_min>=50:
#     print("Pass")
# else:
#     print("Fail")

# import numpy as np
# student_marks = {"Amir": [85, 90, 58],
#                  "Ali": [42, 80, 65],
#                  "Ahsan": [80, 45, 52],
#                  "Sara": [90, 95, 88],
#                  "Zara": [70, 75, 80]}
# student_marks_array = np.array(list(student_marks.values()))
# print(student_marks_array)
# student_marks_mean = np.mean(student_marks_array)
# print("Mean: ", student_marks_mean)
# student_marks_median = np.median(student_marks_array)
# print("Median: ", student_marks_median)
# student_marks_avg = np.average(student_marks_array)
# print("Average: ", student_marks_avg)
# student_marks_min = np.min(student_marks_array)
# print("Minimum: ", student_marks_min)
# student_marks_max = np.max(student_marks_array)
# print("Maximum: ", student_marks_max)
# print("Data Type: ", student_marks_array.dtype)
# if student_marks_array.all() >= 70:
#     print("Pass")
# else:
#     print("Fail")

# Budget Tracker
# import numpy as np
# expenses = np.array(rent=int(input("Enter your rent: ")),
#                     bill=int(input("Enter your bill: ")),
#                     fuel=int(input("Enter your fuel expenses: ")))
# total_expenses = np.sum(expenses)
# print("Total Expenses: ", total_expenses)

import numpy as np
rent = int(input("Enter your rent: "))
bill = int(input("Enter your bill: "))
fuel = int(input("Enter your fuel: "))
expenses = np.array([rent, bill, fuel])
total_expenses = np.sum(expenses)
print("Total Expenses: ", total_expenses)
salary = int(input("Enter your salary: "))
if total_expenses > salary:
    print("You are over budget!")
else:
    print("You are within budget.")
expenses_max = np.max(expenses)
print("Maximum Expense: ", expenses_max)
expenses_min = np.min(expenses)
print("Minimum Expense: ", expenses_min)
expenses_mean = np.mean(expenses)
print("Average Expense: ", expenses_mean)
expenses_max_index = np.argmax(expenses)
print("Maximum Expense Index: ", expenses_max_index)