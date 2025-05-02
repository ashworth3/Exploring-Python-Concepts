# TASK 1

name = "Andre Ashworth"
age = 20
height = 5.9


print("Task 1:")
print("Hi, my name is " + name + "! I am " + str(age) + " years old and " + str(height) + " feet tall.\n")

# TASK 2

num1 = 22
num2 = 79

print("Task 2:")
print("The product of " + str(num1) + " and " + str(num2) + " is " + str(num1 * num2) + ".\n")

# TASK 3

print ("Task 3:")
print("Hello user! Please enter a number:")
user_input = int(input())

if user_input > 0:
    print("The number is positive. Great!")
elif user_input < 0:
    print("The number is negative. Sorry, try again!")
else:
    print("The number is zero. Perfect balance!")

