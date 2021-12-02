# NOTE the = sign is not an equals but instead an assignment
#Write a statement that assigns total_coins with the sum of nickel_count and dime_count. 
total_coins = 0

nickel_count = int(input())
dime_count = int(input())

total_coins = nickel_count + dime_count

print(total_coins)
# Write a statement that assigns cell_count with cell_count multiplied by 10. * performs multiplication.
cell_count = int(input())

cell_count= cell_count * 10

print(cell_count)

# Identifiers must start with a letter or underscore
# Each Python object has three defining properties: value, type, and identity.
#Value: A value such as "20", "abcdef", or 55.
#Type: The type of the object, such as integer or string.
#Identity: A unique identifier that describes the object.
x = 2 + 2    # Create a new object with a value of 4, referenced by 'x'.
print(x)     # Print the value of the object.

x = 2 + 2           # Create a new object with a value of 4, referenced by 'x'.
print(type(x))      # Print the type of the object.
# SAMPLE OUTPUT "<class 'int'>"

print(type('ABC'))  # Create and print the type of a string object.
# SAMPLE OUTPUT "<class 'str'>"

x = 2 + 2           # Create a new object with a value of 4, referenced by 'x'
print(id(x))        # Print the identity (memory address) of the x object
# SAMPLE OUTPUT 1752608
print(id('ABC'))    # Create and print the identity of a string ('ABC') object
# SAMPLE OUTPUT 2330312
# Run The following code and observe the results of str(), type(), and id().
birthday_year = 1986
birthday_month = 'April'
birthday_day = 22

print('birthday_year -->')
print(' value:', birthday_year)
print(' type:', type(birthday_year))
print(' id:', id(birthday_year))

print('\nbirthday_month -->')
print(' value:', birthday_month)
print(' type:', type(birthday_month))
print(' id:', id(birthday_month))

print('\nbirthday_day -->')
print(' value:', birthday_day)
print(' type:', type(birthday_day))
print(' id:', id(birthday_day))

# Floating-point values
# A floating-point number is a real number, like 98.6
# The below program reads in a floating-point value from a user and 
# calculates the time to drive and fly the distance.
miles = float(input('Enter a distance in miles: '))
hours_to_fly = miles / 500.0
hours_to_drive = miles / 60.0

print(miles, 'miles would take:')
print(hours_to_fly, 'hours to fly')
print(hours_to_drive, 'hours to drive')
# NOTE
# floating-point literal using scientific notation is written using an e preceding the power-of-10 exponent
# so 1x10^-3 can be written as 1.0e-3 

# The following program reads in a mass in kilograms 
# prints the amount of energy stored in the mass and 
# the equivalent numbers of AA batteries and tons of TNT.
c_meters_per_sec = 299792458  # Speed of light (m/s)
joules_per_AA_battery = 4320.5  # Nickel-Cadmium AA batteries
joules_per_TNT_ton = 4.184e9

#Read in a floating-point number from the user
mass_kg = float(input())

#Compute E = mc^2.
energy_joules = mass_kg * (c_meters_per_sec**2)  # E = mc^2
print('Total energy released:', energy_joules, 'Joules')

#Calculate equivalent number of AA and tons of TNT.
num_AA_batteries = energy_joules / joules_per_AA_battery
num_TNT_tons = energy_joules / joules_per_TNT_ton

print('Which is as much energy as:')
print('  ', num_AA_batteries, 'AA batteries')
print('  ', num_TNT_tons, 'tons of TNT')
# NOTE overflowerror occurs when a vlaue is larger than  1.8e308 or smaller than 2.3e-308

# Syntax for Manipulating floating-point output
# import math required for the use of "math.pi"
import math 
print('Default output of Pi:',  math.pi)
print('Pi reduced to 4 digits after the decimal:', end=' ')
print('{:.4f}'.format(math.pi))

# program computes how many gallons of paint are needed to cover the given square feet of walls. 
# Assuming 1 gallon can cover 350.0 square feet.

wall_area = float(input())

gallons_paint = 350

gallons_paint = wall_area / gallons_paint

print(gallons_paint)
# output is 0.714285714286

# expressions + - * / **
# precedence (), **, unary(negative so 2*-x, -x first), * , / , % , + , - , then left-to-right

# sample utilizes precendence to calculate Calorie expenditure
calories_man = ( (age_years * 0.2017) + (weight_pounds * 0.09036) + (heart_bpm * 0.6309) - 55.0969 ) * time_minutes / 4.184

calories_woman = ( (age_years * 0.074) - (weight_pounds * 0.05741) + (heart_bpm * 0.4472) - 20.4022 ) * time_minutes/ 4.184


""" Computes the total cost of leasing a car given the down payment,
    monthly rate, and number of months """

down_payment = int(input('Enter down payment: '))
payment_per_month = int(input('Enter monthly payment: '))
num_months = int(input('Enter number of months: '))

total_cost = down_payment + (payment_per_month * num_months)

print ('Total cost:', total_cost)

# compound operators  
# Addition age += 1	
# Subtraction	age -= 1	
# Multiplication age *= 1	
# Division age /= 1	
# Modulo	age %= 1	

# escape sequences 
# EscapeSequence ||	Explanation || Example code || Output
# \\ ||	Backslash (\) || print('\\home\\users\\')|| \home\users\
# \' ||	Single quote (') ||	print('Name: John O\'Donald') || Name: John O'Donald
# \" ||	Double quote (") ||	print("He said, \"Hello friend!\".") || He said, "Hello friend!".
# \n ||	Newline || print('My name...\nIs John...') || My name... Is John...
# \t ||	Tab (indent) || print('1. Bake cookies\n\t1.1. Preheat oven') || 1. Bake cookies 1.1. Preheat oven

# raw strings ignore escape sequences ^
# my_raw_string = r'This is a \n \'raw\' string'

# program takes string inputs and tells a story
#A 'Mad Libs' style game where user enters nouns,
#verbs, etc., and then a story using those words is ouput.

#Get user's words
relative = input('Enter a type of relative: ')
print()
food = input('Enter a type of food: ')
print()
adjective = input('Enter an adjective: ')
print()
period = input('Enter a time period: ')
print()
# Tell the story
print('My', relative, 'says eating', food)
print('will make me more', adjective)
print('so now I eat them every', period)

# len() is used to find lenght of a string
# printing string_name[index number in brackets (so like 0)] 
# prints the string character in that index position

# strings are immutable you must assign a new string to change the output

# string concatenation is done as string_1 + string_2
# then printing as 
string_1 = 'abc'
string_2 = '123'
concatenated_string = string_1 + string_2
print('Easy as ' + concatenated_string)

# type converstions (float int etc)
# 1 + 2 returns an integer type.
# 1 + 2.0 returns a float type.
# 1.0 + 2.0 returns a float type.

# progam below shows input conversion from string to int
total_owls = 0

num_owls_A = input()
num_owls_B = input()

total_owls = int(num_owls_A) + int(num_owls_B)

print('Number of owls:', total_owls)

# program takes 2 ints and divides them into x three times
user_num = int(input())
x = int(input())


print(user_num // x, end=' ') 
print(user_num // x ** 2, end=' ')
print(user_num // x ** 3)

