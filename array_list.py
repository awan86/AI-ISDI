# marks = ['A', 'B', 'C', 'D', 'E']
# print(marks[0:])

# marks_1 = ['A, B, C, D, E']
# print(marks_1[0])

# marks = ['20', '30', '40', '50', '60', '70', '80', '90', '100', '110', '120', '130', '140', '150', '160', '170', '180', '190', '200']
# print(marks[0:])
# print(marks[9:])
# print(marks[9:19])
# print(marks[:19])

# marks = ['20', '30', '40', '50', '60', '70', '80', '90', '100', '110', '120', '130', '140', '150', '160', '170', '180', '190', '200']
# def marks(start, end):
#     return marks[start:end]
# start = 0
# end = 19
# print(marks(start, end))

# def marks():
#     start = int(input("Enter the starting index: "))
#     end = int(input("Enter the ending index: "))
#     return marks[start:end]
# print(marks())

# marks = [10,20,30,40,50,60,70,80,90,100]
# print("maximum value is:", max(marks))
# print("minimum value is:", min(marks))
# print("sum of all values is:", sum(marks))
# print("average value is:", sum(marks)/len(marks))
# if sum(marks)/len(marks)>80:
#     print("You have done an excellent job")
# else:
#     print("You need to work harder")

# marks = [10,20,30,40,50,60,70,80,90,100]
# marks.sort(reverse=True)
# print("Top 3 Students are:", marks[0:3])

# marks = [10,20,30,40,50,60,70,80,90,100]
# marks.sort(reverse=False)
# print("Bottom 3 Students are:", marks[0:3])

# fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon']
# print(fruits[4:7])
# print(fruits[-6:-3])
# fruits.append('mango')
# print(fruits)
# fruits.remove('banana')
# print(fruits)
# fruits.insert(2, 'guawa')
# fruits.insert(2, 'orange')
# print(fruits)

marks=[20,40,48,59]
# marks.append(60)
# print(marks)
# marks.remove(20)
# print(marks)
# marks.insert(2,60)
# print(marks)
marks.insert(3,68)
marks[1]=42
print(marks)