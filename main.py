#String "I love Python programming!"
#Integer 42
#Float 3.14
#Boolean True or False

name = "Mercer"
age = 22
score = 97.5
engineer = True
print("My name is " + name + ", I am " + str(age) + " years old, my score is " + str(score) + ", and it is " + str(engineer) + " that I am an engineer.")
#-----------------------------------------------------------------------------------------------------------------------------------------#
#Arithmetic operators
#parentheses (()) means "do this first"
#exponents (**) means "to the power of"
#multiplication (*)
#division (/)
# addition (+)
#subtraction (-)

#floor division (//) means "delete the after the decimal point"

print(5 * (2 + 4) / 2 - 3)

num1 = 10
num2 = 5
sum = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
print(sum)
print(subtraction)
print(multiplication)
print(division)
#-----------------------------------------------------------------------------------------------------------------------------------------#
#Escape Characters
print("Mohamed Said: \"I Like Football\"") # \' Single Quote
print("ali\n love me") #\n	New Line
print("Hello \t world") #\t	Tab
print("Hello \b world") #\b	Backspace
print("Hello \f world") #\f	Form Feed
#-----------------------------------------------------------------------------------------------------------------------------------------#
#Multi Line String
print("""I want to be a AI engineer
but I should to learn first a python Language 
after i shold learn machine learning""")


#-----------------------------------------------------------------------------------------------------------------------------------------#
#Variables and User Input
first_name = (input("Enter your First Name: "))
last_name = (input("Enter your Last Name: "))
print("Hello " + first_name + " " + last_name + "! Welcome to Python programming.")
