# class Admission:
#     pass
# a1 = Admission()
# a1.name="Amir"
# a1.age=29
# a1.education="Bachelors"
# a1.profession="Banking"
# print(a1.name, a1.age, a1.education, a1.profession)

# class Admission:
#     pass
# a1 = Admission()
# a1.name="Amir"
# a1.age=29
# a1.education="Bachelors"
# a1.profession="Banking"
# print(a1.name)
# print(a1.age)
# print(a1.education)
# print(a1.profession)
# functions = methods
# class Ali:
#     def study(Self):
#         print("Ali is studying")
# a2 = Ali()
# a2.study()

# class Ali:
#     def study(a):
#         print("Ali is studying")
# a2 = Ali()
# a2.study()

# class Amir:
#     def play(a):
#         print("Amir is playing")
# a3 = Amir()
# a3.play()

#constructor: assign value to the object (which we will create)
# class student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# s1 = student("Amir", 29)
# s2 = student("Ali", 30)
# s3 = student("Sara", 28)
# s4 = student("Aisha", 27)
# print(s1.name, s1.age)
# print(s2.name, s2.age)
# print(s3.name, s3.age)
# print(s4.name, s4.age)

# class Admission:
#     def __init__(self, name, age, education, profession):
#         self.name = name
#         self.age = age
#         self.education = education
#         self.profession = profession
# a1 = Admission(input("Enter your name: "),
#                int(input("Enter your age: ")),
#                input("Enter your education: "),
#                input("Enter your profession: "))
# print(a1.name)
# print(a1.age)
# print(a1.education)
# print(a1.profession)

# class Admission:
#     def __init__(a, name, age, education, profession):
#         a.name = name
#         a.age = age
#         a.education = education
#         a.profession = profession
# a1 = Admission(name=input("Enter your name: "),
#                age=int(input("Enter your age: ")),
#                 education=input("Enter your education: "),
#                 profession=input("Enter your profession: "))
# print(a1.name, a1.age, a1.education, a1.profession)
# a2 = Admission(name=input("Enter your name: "),
#                age=int(input("Enter your age: ")),
#                 education=input("Enter your education: "),
#                 profession=input("Enter your profession: "))
# print(a2.name, a2.age, a2.education, a2.profession)
# a3 = Admission(name=input("Enter your name: "),
#                age=int(input("Enter your age: ")),
#                 education=input("Enter your education: "),
#                 profession=input("Enter your profession: "))
# print(a3.name, a3.age, a3.education, a3.profession)

# class Student:
#     def __init__(a, name, roll_no, marks):
#         a.name = name
#         a.roll_no = roll_no
#         a.marks = marks
#     def show_details(a):
#         print("Name: ", a.name)
#         print("Roll Number: ", a.roll_no)
#         print("Marks: ", a.marks)
# s1 = Student(name = input("Enter your name: "),
#              roll_no = int(input("Enter your roll number: ")),
#              marks = int(input("Enter your marks: ")))
# s1.show_details()

# class Cars:
#     def __init__(a, make, model, color):
#         a.make = make
#         a.model = model
#         a.color = color
#     def started(a):
#         print("Make", a.make)
#         print("Model", a.model)
#         print("Color", a.color)
#     def stop(b):
#         print("Make", b.make)
#         print("Model", b.model)
#         print("Color", b.color)
# c1 = Cars(make=input("Enter the make of the car: "),
#           model=input("Enter the model of the car: "),
#           color=input("Enter the color of the car: "))
# c1.started()
# c2 = Cars(make=input("Enter the make of the car: "),
#           model=input("Enter the model of the car: "),
#           color=input("Enter the color of the car: "))
# c2.stop()

# class Admission:
#     def __init__(a, name, age, education, profession):
#         a.name = name
#         a.age = age
#         a.education = education
#         a.profession = profession
#     def show_details(a):
#         print("Name: ", a.name)
#         print("Age: ", a.age)
#         print("Education: ", a.education)
#         print("Profession: ", a.profession)
# a1 = Admission(name=input("Enter your name: ?"), age=int(input("Enter your age: ?")), education=input("Enter your education: ?"), profession=input("Enter your profession: ?"))
# # print(a1.name, a1.age, a1.education, a1.profession)
# a1.show_details()