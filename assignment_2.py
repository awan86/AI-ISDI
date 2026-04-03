# Write a Python program to print the following pattern using a loop:

# rows = 5
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

# rows = 10
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

# rows = 10
# for i in range(1,10,1):
#     print(i)

# rows = 10
# for i in range(0, rows + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print(i)

# Write a program tha takes a number from the user and calculates its factorial using a loop

# num = int(input("Enter a number: "))
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i
# print(factorial)

# Create a simple login system where:
# User has 3 attempts to enter correct password

# for i in range(3):
#     username = input("Enter your username: ")
#     if username == "awan86":
#         print("Enter your password?")
#         password = input("Enter your password: ")
#         if password == "1234":
#             print("Access Granted")
#             break
#         else: print("Account is locked")

# rows = 5
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

# num = int(input("Enter your number?"))
# factorial = 1
# for i in range(1, num + 1):
#     factorial = factorial * i
# print(factorial)

# correct_username = "awan86"
# correct_password = "1234"

# for i in range(5):
#     username = input("Enter your username?")
#     password = input("Enter your password?")
#     if username == correct_username and password == correct_password:
#         print("Access Granted")
#         break
#     else:
#         print("Account is locked")
#         print("Attempts left:", 5 - i)
# else:
#     print("Account is locked")

# correct_username = "awan86"
# correct_password = "1234"

# attempts = 3
# for i in range(1,attempts):
#     username = input("Enter your username?")
#     password = input("Enter your password?")
#     if username == correct_username and password == correct_password:
#         print("Access Granted")
#         break
#     else:
#         print("Account is locked")
#         print("Attempts left:", attempts - i)
# else:
#     print("Account is locked")

# correct_username = "awan86"
# correct_password = "0789"

# attempts = 3
# for i in range(attempts):
#     username = input("Enter your username?")
#     password = input("Enter your password?")
#     if username == correct_username and password == correct_password:
#         print("Welcome")
#         break
#     else:
#         print("Incorrect username or password")
#         print("Attempts left:", attempts - i - 1)

# i = 1
# while i<=3:
#     username=input("Enter your username?")
#     if username=="admin":
#         print("correct")
#         break
#     else:
#         print("Incorrect username")
#         i += 1

# i = 1
# while True:
#     username = input("Enter your username?")
#     if username == "admin":
#         print("correct")
#         break
#     else:
#         print("Incorrect username")
#         i += 1
#         if i > 3:
#             print("Account is locked")

# for i in range(1,20,2):
#     print(i)

# i = 1
# while i < 20:
#     print(i)
#     i = i + 2

# for i in range(0, 20, 2):
#     print(i)

# i = 0
# while i < 20:
#     print(i)
#     i = i + 2

# secret = 7
# attempts = 3
# while secret != 7:
#     guess = int(input("Guess the number?"))
#     if guess == secret:
#         print("Congratulations! You guessed the number.")
#         break

# secret = 27
# guess = None
# while guess !=27:
#     guess = int(input("Guess the number?"))
#     if guess == secret:
#         print("Congratulations! You guessed the number.")
#         break
#     else:
#         print("Better Luck Next Time")

# secret = 44
# guess = None
# while guess !=secret:
#     guess = int(input("Guess the number?"))
#     attempts = 1
#     if guess == secret:
#         print("Congratulations! You guessed the number.")
#         break
#     else:
#         print("Better Luck Next Time")
#         print("Attempts left:", 3 - attempts)

# secret = 44
# count = 0
# guess = None
# while guess !=secret:
#     guess = int(input("Guess the number?"))
#     count += 1
#     if guess == secret:
#         print("Congratulations! You guessed the number.")
#         break
#     else:
#         print("Better Luck Next Time")
# print("Total attempts:", count)

secret = 11
guess = None
count = 0
while guess !=secret:
    guess = int(input("Guess the number?"))
    count += 1
    if guess == secret :
        print("Congratulations! You guessed the number.")
        break
    else:
        print("Better Luck Next Time")
print("Total Attempts:", count)