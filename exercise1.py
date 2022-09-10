#1.  Python program to calculate length of a String without using len() function
str =input("Enter a string:")
# counter variable to count the character in a string
count = 0
for s in str:
    count = count+1
print("Length of the input string is:",count)

