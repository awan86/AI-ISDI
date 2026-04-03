# to repeat a value in no of times, we use functions:
#()= parameters
# def admission(name, age):
#     print("Your name is ", name)
#     print("Your age is ", age)
# admission("Amir", 12)
#admission(name="Amir", age=12)

# def admission(name, age):
#     print("Your name is", 
#           input("Enter your name: "))
#     print("Your age is",
#           int(input("Enter your age: ")))
# admission(name="Amir", age=12)

# def admission(name, age):
#     print("Your name is", name)
#     print("Your age is", age)
# x= input("Enter your name: ")
# y=int(input("Enter your age: "))
# admission(x,y)

# correct_username = "admin"
# correct_password = "1234"
# attempts = 3
# def registration(username, password):
#     for i in range(0,attempts):
#         if username == correct_username and password == correct_password:
#             print("You are logged-in")
#             break
#         else:
#             print("Invalid username or password. Please try again.")
#             print("Attempt left:", attempts - 1)
# username = input("Enter your username: ")
# password = input("Enter your password: ")
# registration(username=username, password=password)

# def login():
#     correct_username = "admin"
#     correct_password = "0789"
#     attempts = 1
#     while attempts <=3:
#         username = input("Enter your username:")
#         password = input("Enter your password:")
#         # for i in range(0,attempts):
#         if username == correct_username and password == correct_password:
#             print("You are logged-in")
#             break
#         else:
#             print("Wrong password or username. Please try again.")
#             attempts +=1
#             # print("Attempts left:", attempts - 1)
# login()

def login():
    correct_username = "amir"
    correct_password = "1122"
    attempts = 1
    while attempts<=3:
        username = input("Enter your username:")
        password = input("Enter your password:")
        if username == correct_username and password == correct_password:
            print("Login Successful")
            break
        else:
            print("Incorrect username or password")
            attempts +=1
login()