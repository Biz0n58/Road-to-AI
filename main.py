# #String "I love Python programming!"
# #Integer 42
# #Float 3.14
# #Boolean True or False

# name = "Mercer"
# age = 22
# score = 97.5
# engineer = True
# print("My name is " + name + ", I am " + str(age) + " years old, my score is " + str(score) + ", and it is " + str(engineer) + " that I am an engineer.")
# #-----------------------------------------------------------------------------------------------------------------------------------------#
# #Arithmetic operators
# #parentheses (()) means "do this first"
# #exponents (**) means "to the power of"
# #multiplication (*)
# #division (/)
# # addition (+)
# #subtraction (-)

# #floor division (//) means "delete the after the decimal point"

# print(5 * (2 + 4) / 2 - 3)

# num1 = 10
# num2 = 5
# sums = num1 + num2
# subtraction = num1 - num2
# multiplication = num1 * num2
# division = num1 / num2
# print(sums)
# print(subtraction)
# print(multiplication)
# print(division)
# #-----------------------------------------------------------------------------------------------------------------------------------------#
# #Escape Characters
# print("Mohamed Said: \"I Like Football\"") # \' Single Quote
# print("ali\n love me") #\n	New Line
# print("Hello \t world") #\t	Tab
# print("Hello \b world") #\b	Backspace
# print("Hello \f world") #\f	Form Feed
# #-----------------------------------------------------------------------------------------------------------------------------------------#
# #Multi Line String
# print("""I want to be a AI engineer
# but I should to learn first a python Language 
# after i should learn machine learning""")
# #-----------------------------------------------------------------------------------------------------------------------------------------#
# #Built-in Functions

# print("Length for Hello World is: " + str(len("Hello World"))) # Returns the length of a string
# print("Data type for 3.14 is: " + str(type(3.14))) # Returns the data type of a value
# print("Data type for Hello is: " + str(type("Hello"))) # Returns the data type of a value
# print("Data type for True is: " +str(type(True))) # Returns the data type of a value

# #-----------------------------------------------------------------------------------------------------------------------------------------#
# #string methods 
# print("Mohamed".upper()) # Converts a string to uppercase
# print("Mohamed".lower()) # Converts a string to lowercase
# print("Mohamed".capitalize()) # Capitalizes the first letter of a string
# print("Mohamed".replace("o", "a")) # Replaces a specified value with another value in a string
# print("Mohamed".find("a")) # Searches for a specified value and returns the position of where it was found in a string
# #-----------------------------------------------------------------------------------------------------------------------------------------#
# #Indexing and Slicing
# name = "Eli Mercer" 
# first_name = name[0:3]
# last_name = name[4:]
# print(first_name) # Slices the string from index 0 to index 3 (not including index 3)
# print(last_name) # Slices the string from index 4 to the end
#-----------------------------------------------------------------------------------------------------------------------------------------#
#built-in functions (numbers)
number = -58
number2 = 86.14
number3 = 65
print((abs(number))) # Returns the absolute value of a number
print((round(number2))) # Rounds a number to the nearest integer
print(sum([number, number2, number3])) # Returns the sum of three numbers
print(max(number, number2, number3)) # Returns the largest of three numbers
print(min(number, number2, number3)) # Returns the smallest of three numbers
#-----------------------------------------------------------------------------------------------------------------------------------------#
#Incrimination
numbers = 2
print(numbers) # Output: 2
numbers += 3 # numbers = numbers + 3
print(numbers) # Output: 5


#-----------------------------------------------------------------------------------------------------------------------------------------#
# For Loop

name = "Eli Mercer"
for letter in name: 
    print(letter) # Output: M, e, r, c, e, r



fruits = ["apple", "banana", "cherry" , "watermelon"]
a = 0 
for fruit in fruits:
    a += 1
    print(fruit + " " + str(a)) # Output: apple, banana, cherry, watermelon   

    
for x in range(5):
    print("Hello:" + str(x)) # Output: 0, 1, 2, 3, 4

for y in range(6,11,2): # Output: 6, 8, 10
    print("World:" + str(y))    

    
u = 0 
for letter in input("Enter your name: "):
    u += 1
    print(letter + " " + str(u)) # Takes user input and prints each letter on a new line


#-----------------------------------------------------------------------------------------------------------------------------------------#


#-----------------------------------------------------------------------------------------------------------------------------------------#
#Variables and User Input
# first_name = (input("Enter your First Name: "))
# last_name = (input("Enter your Last Name: "))
# print("Hello " + first_name + " " + last_name + "! Welcome to Python programming.")
