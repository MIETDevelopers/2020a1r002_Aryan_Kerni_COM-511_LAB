#7. Write a Python program to print the even numbers from a given list
list1 = [11, 23, 45, 23, 64, 22, 11, 24]
# iteration
for num in list1:
# check
    if num % 2 == 0:
       print(num, end=" ")