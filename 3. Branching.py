# In a program, a branch is a sequence of statements only executed under a certain condition.
# An if branch is a branch taken only IF an expression is true
# An if-else branch has two branches: 
#     The first branch is executed IF an expression is true,
#       ELSE the other branch is executed.
# == is the equality operator used in funtions to evaluate if branch is equal 
# != is the equality operator used in functions to evaluate if branch is not equal
# Dectecting if two items are equal: Hotel Discount
hotel_rate = 150

num_years = int(input('Enter years married: '))

if num_years == 50:
    print('Congratulations on 50 years of marriage!')
    hotel_rate = hotel_rate / 2

print('Your hotel rate:', hotel_rate)
# elif is used to evaluate multi-branch if-else statments
# Anniversaries example 
num_years = int(input('Enter number years married: '))

if num_years == 1:
    print('Your first year -- great!')
elif num_years == 10:
    print('A whole decade -- impressive.')
elif num_years == 25:
    print('Your silver anniversary -- enjoy.')
elif num_years == 50:
    print('Your golden anniversary -- amazing.')
else:
    print('Nothing special.')
# you can also use if else if statements when trying to evaluate a range 
# this is acccomplished by using relational operators  <, >, <=, >=

# using relational operators to gather an inclusive range
# program will print "in high school" if the value of user_grade is between 9 and 12 inclusive
user_grade = int(input())
if  9 <= user_grade <= 12:
    print('in high school')
else:
    print('not in high school')
    
# logical operators are AND, OR, NOT they evaluate true and false
# Logical operators examples (age > 16) and (age < 25), (age > 16) or (days > 10), not (days > 10)

# Program detects cable tv channels
user_channel = int(input())
   
if (user_channel >= 2) and (user_channel <= 499):
    channel_type = 's'

elif (user_channel >= 1002) and (user_channel <= 1499):
    channel_type = 'h'

else:
    channel_type = 'e'

print('Channel type:', channel_type)

# operands evaluate logically
# Boolean values True, False
# sometimes a programmer has multiple if statments in a sequence which is done because
# Each if statement is independent, and thus more than one branch can execute

# If-else statements can also contain if-else statments inside also known as nested if else statements

# Floating-point types should not be compared using the equality operators
# Strings are compared by converting each character to a number value (ASCII or Unicode), and then comparing each character in order. Most string comparisons use equality operators "==" or "!=", as in today == 'Friday'.
# Lists and tuples are compared via an ordered comparison of every element in the sequence. Every element between the sequences must compare as equal for an equality operator to evaluate to True. Relational operators like < or > can also be used: The result is determined by the first mismatching elements in the sequences. For example, if x = [1, 5, 2] and y = [1, 4, 3], then evaluating x < y first evaluates that 1 and 1 match. The next elements do not match, so 5 < 4 is evaluated, which produces a value of False.
# Dictionaries are compared only with == and !=. To be equal, two dictionaries must have the same set of keys and the same corresponding value for each key.

# important to note that operands have the least precedence not, and, or

# list and dicts multi line constructs
my_list = [
    1, 2, 3,
    4, 5, 6
    ]
my_dict = {
    'entryA': 1,
    'entryB': 2
}
# using the format method allows a programmer to create a string with placeholders that are replaced by values or variable values at execution. 
number = 6
amount = 32
print('{}burritos cost ${}'.format(number, amount))
# can be poitional by indexing placeholders, inferred as above, or named as below
print('The {animal} in the {headwear} is {shape}.'.format(animal='cat', headwear='hat', shape='fat'))


#format specifications
# s || string || '{:s}'.format('Aiden')
# d || decimal || '{:d}'.format(4)
# b || binary || '{:b}'.format(4)
# x,X || Hexadecimal in lowercase (x) and uppercase (X) || '{:x}'.format(15)
# e || exponent || '{:e}'.format(44)
# f || Fixed-point notation (6 places of precision) ||'{:f}'.format(4)
# .[precision]f || Fixed-point notation (programmer-defined precision) || '{:.2f}'.format(4)
# 0[precision]d	|| Leading 0 notation || '{:03d}'.format(4)

# The colon : in the replacement field separates the "what" on the left from the "how" on the right.
#  The left side may be 
# omitted (inferred positional replacement)
'{:s} ${:.2f} tacos is ${:.2f} total'.format('Three', 1.50, 4.50)
# a number (positional replacement)
'{0:s} ${2:.2f} tacos is ${1:.2f} total'.format('Three', 4.50, 1.50)
# a name (named replacement)
'{cnt:s} ${cost:.2f} tacos is ${sum:.2f} total'.format(cnt = 'Three', cost = 1.50, sum = 4.50)
# output : Three $1.50 tacos is $4.50 total

# Automobile service invoice

print("Davy's auto shop services\nOil change -- $35\nTire rotation -- $19\nCar wash -- $7\nCar wax -- $12\n")
# get first and second service from user
first = input("Select first service:\n")
second = input("Select second service:\n")
print("\nDavy's auto shop invoice\n")
# initialise total charge as zero
sum = 0
# compare the first service with menu contents using if else and add corresponding charges to the sum
if first=="Oil change":
    print("Service 1: Oil change, $35")
    sum+= 35
elif first=="Tire rotation":
    print("Service 1: Tire rotation, $19")
    sum+= 19
elif first=="Car wash":
    print("Service 1: Car wash, $7")
    sum+= 7
elif first=="Car wax":
    print("Service 1: Car wax, $12")
    sum+= 12
# if first service is a -, print no service and add no charges
elif first=="-":
    print("Service 1: No service")
# if input matches none of the menu items exactly or the '-', print error message for first service
else:
    print("Service 1: Wrong service entered. Please refer menu")
# compare the second service with menu contents using if else and add corresponding charges to the sum
if second=="Oil change":
    print("Service 2: Oil change, $35")
    sum+= 35
elif second=="Tire rotation":
    print("Service 2: Tire rotation, $19")
    sum+= 19
elif second=="Car wash":
    print("Service 2: Car wash, $7")
    sum+= 7
elif second=="Car wax":
    print("Service 2: Car wax, $12")
    sum+= 12
# if second service is a -, print no service and add no charges
elif second=="-":
    print("Service 2: No service")
# if input matches none of the menu items exactly or the '-', print error message for second service
else:
    print("Service 1: Wrong service entered. Please refer menu")
    
print()
# print total. sep="" is a print() parameter to print no space in between two elements
print("Total: $", sum, sep="")

# leap year checker
is_leap_year = False
   
input_year = int(input())

leap = input_year % 4
 

if input_year == 1900:
    print("{} - not a leap year".format(input_year))
elif leap == 0:
    print("{} - leap year".format(input_year))
else:
    print("{} - not a leap year".format(input_year))
    

