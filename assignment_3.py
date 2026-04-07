class Accounts:
    def __init__(a, name, roll_no, fee):
        a.name = name
        a.roll_no = roll_no
        a.fee = fee
    def display(a):
        print("Name:", a.name)
        print("Roll No:", a.roll_no)
        print("Fee:", a.fee)
a1 = Accounts(name=input("Enter your name? "),
              roll_no=int(input("Enter your roll no? ")),
              fee=int(input("Enter your fee?")))
a1.display()

class Result:
    def __init__(b, name, roll_no, marks):
        b.name = name
        b.roll_no = roll_no
        b.marks = marks
    def display(b):
        print("Name:", b.name)
        print("Roll no:", b.roll_no)
        print("Marks:", b.marks)
b1 = Result(name=input("Enter your name? "),
            roll_no=int(input("Enter your roll no? ")),
            marks=int(input("Enter your marks? ")))
b1.display()