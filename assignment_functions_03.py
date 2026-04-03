# # def addition():
# #     print(a+b)
# # a = int(input("Enter your first number?"))
# # b = int(input("Enter your second number?"))
# # addition()

def addition(a, b):
    print(a+b)
a = int(input("Enter your first number?"))
b = int(input("Enter your second number?"))
addition(a=a,b=b)

# # def subtraction():
# #     print(c-d)
# # c = int(input("Enter your first number?"))
# # d = int(input("Enter your second number?"))
# # subtraction()

def subtraction(c,d):
    print(c-d)
c = int(input("Enter your first number?"))
d = int(input("Enter your second number?"))
subtraction(c=c,d=d)

# # def multiplication():
# #     print(e*f)
# # e = int(input("Enter your first number?"))
# # f = int(input("Enter your second number?"))
# # multiplication()

def multiplication(e,f):
    print(e*f)
e = int(input("Enter your first number?"))
f = int(input("Enter your second number?"))
multiplication(e=e,f=f)

# # def division():
# #     print(g/h)
# # g = int(input("Enter your first number?"))
# # h = int(input("Enter your second number?"))
# # division()

def division(g,h):
    print(g/h)
g = int(input("Enter your first number?"))
h = int(input("Enter your second number?"))
division(g=g,h=h)

# # def exponential():
# #     print(i**j)
# # i = int(input("Enter your first number?"))
# # j = int(input("Enter your second number?"))
# # exponential()

def exponential(i,j):
    print(i**j)
i = int(input("Enter your first number?"))
j = int(input("Enter your second number?"))
exponential(i=i,j=j)

# # def modulous():
# #     print(k%l)
# # k = int(input("Enter your first number?"))
# # l = int(input("Enter your second number?"))
# # modulous()

def modulous(k,l):
    print(k%l)
k = int(input("Enter your first number?"))
l = int(input("Enter your second number?"))
modulous(k=k,l=l)

# correct_username = "admin"
# correct_password = "1234"
# attempts = 4
# for i in range(1,attempts):
#     username = input("Enter your username?")
#     password = input("Enter your password?")
#     if username == correct_username and password == correct_password:
#         print("Login Successful")
#         break
#     else:
#         print("Invalid Credentials")
#         print("Attempts left:", attempts - i - 1)

correct_username = "admin"
correct_password = "1234"
attempts = 3
for i in range(0,attempts):
    username = input("Enter your username?")
    password = input("Enter your password?")
    if username == correct_username and password == correct_password:
        print("Login Successful")
        break
    else:
        print("Invalid Credentials")
        print("Attempts left:", attempts - i - 1)