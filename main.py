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
# 
# 
# 
# 
# 
# 
# 
# 
#                                                     NEW   #-----------------------------------------------------------------------------------------------------------------------------------------#
# #Indexing and Slicing
# name = "Eli Mercer" 
# first_name = name[0:3]
# last_name = name[4:]
# print(first_name) # Slices the string from index 0 to index 3 (not including index 3)
# print(last_name) # Slices the string from index 4 to the end
#-----------------------------------------------------------------------------------------------------------------------------------------#
#built-in functions (numbers)
# number = -58
# number2 = 86.14
# number3 = 65
# print((abs(number))) # Returns the absolute value of a number
# print((round(number2))) # Rounds a number to the nearest integer
# print(sum([number, number2, number3])) # Returns the sum of three numbers
# print(max(number, number2, number3)) # Returns the largest of three numbers
# print(min(number, number2, number3)) # Returns the smallest of three numbers
#-----------------------------------------------------------------------------------------------------------------------------------------#
#Incrimination
# numbers = 2
# print(numbers) # Output: 2
# numbers += 3 # numbers = numbers + 3
# print(numbers) # Output: 5


#-----------------------------------------------------------------------------------------------------------------------------------------#
# For Loop

# fruits = ["apple", "banana", "cherry" , "watermelon"]
# a = 0 
# for fruit in fruits:
#     a += 1
#     print(fruit + " " + str(a)) # Output: apple, banana, cherry, watermelon   

    


# u = 0 
# for letter in input("Enter your name: "):
#     u += 1
#     print(letter + " " + str(u)) # Takes user input and prints each letter on a new line
#     exit


#-----------------------------------------------------------------------------------------------------------------------------------------#
# Nested Loops
# cars = ["Toyota", "Honda", "Ford"]
# colors = ["Red", "Blue", "Green"]
# for car in cars: 
#     print("Car: " + car) # Output: Toyota, Honda, Ford
#     print("The Available Colors are: ") 
#     for color in colors: 
#         print( color) # Output: Red, Blue, Green

#-----------------------------------------------------------------------------------------------------------------------------------------#
#While Loop
# while 1 < 5: #True
#     print("Hello World") # Output: Hello World (infinite loop)
   
# while 1 > 5: #False
#     print("Hello World") # Output: (nothing)
#-----------------------------------------------------------------------------------------------------------------------------------------#
#Conditional Statements
# age = int(input("Enter your age: "))
# if age >= 21:
#     print("You can buy smoke & alcohol") # Output: You can buy smoke
# elif age >= 18:
#     print("You can buy smoke only") # Output: You can buy smoke only
# else:
#     print("You are not allowed to buy smoke or alcohol") # Output: You are not allowed to buy smoke or alcohol
# #-----------------------------------------------------------------------------------------------------------------------------------------#
# #Comparison Operators
# # == Equal to
# # != Not equal to
# # > Greater than
# # < Less than
# # >= Greater than or equal to
# # <= Less than or equal to
# #-----------------------------------------------------------------------------------------------------------------------------------------#
# #Break and Continue
# nmb = input("Enter a number: ")
# number = int(nmb)
# x = 0
# while x < 10:
#     x += 1
#     if x == number:
#         continue
#     print(x) # Output: 1, 2, 3, 4, 5, 6, 7, 8, 9 (skips the number entered by the user)

# #-----------------------------------------------------------------------------------------------------------------------------------------#
# #not
# #and   
# #or
# score = int(input("Enter your score: "))
# absent = int(input("Are you absent?: "))
# if score >= 90 and absent == 0:
#     print("You are excellent") # Output: You are excellent
# elif score >= 90 or absent == 0:
#     print("You are excellent") # Output: You are excellent
# elif score >= 80 and absent == 5:
#     print("You are good") # Output: You are good
# elif score >= 60 and absent == 10:
#     print("You are average") # Output: You are average
# else:
#     print("You are fail") # Output: You are fail
#-----------------------------------------------------------------------------------------------------------------------------------------#
#nested if statements
number  =  int(input("Enter a number: "))
if number >= 0:
    if number == 0:
        print("zero") # Output: zero
    else:
        print("positive number") # Output: positive number
else:
    print("negative number") # Output: negative number

#-----------------------------------------------------------------------------------------------------------------------------------------#
#Lists
Students = ["Ali", "Sara", "mohamed", "Mercer", "Ali"]
print(Students.index("Mercer") )# Returns the index of the first occurrence of "mohamed" in the list
print(Students.pop(1)) # Removes and returns the element at index 1 (Sara)
print(Students.count("Ali")) # Returns the number of times "mohamed" appears in the list
print(Students.insert(2, "Ahmed")) # Adds "Ahmed" to the end of the list
print(Students.remove("Mercer")) # Removes the first occurrence of "Mercer" from the list
print(Students) # Output: ['Ali', 'Sara', 'mohamed', 'Ahmed']
print(Students[2]) # Output: mohamed

x = 0
for Student in Students: 
    x += 1
    print(str(x) + "-" + Student) # Output: 1 Ali, 2 Sara, 3 mohamed, 4 Mercer
#-----------------------------------------------------------------------------------------------------------------------------------------#
#Nested Lists

#-----------------------------------------------------------------------------------------------------------------------------------------#

#Variables and User Input
# first_name = (input("Enter your First Name: "))
# last_name = (input("Enter your Last Name: "))
# print("Hello " + first_name + " " + last_name + "! Welcome to Python programming.")
