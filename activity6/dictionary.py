'''Write a program to create a list of student’s records and search a student record using a
dictionary.'''
#Creating Dictionary

students = dict()
n = int(input("Enter number of students :"))
for i in range(n):
    sname = input("Enter names of student :")
    marks= []
    for j in range(5):
        mark = float(input("Enter marks :"))
        marks.append(mark)
    students[sname] = marks
print("Dictionary of student created :")
print(students)
