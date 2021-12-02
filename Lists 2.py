# Lists are containers, which is an object that groups related objects together.
# Indexs are used to acess elements in the container
# Liists i'ths element can be accessed using [i]

# Oldest people program
oldest_people = [122, 119, 117, 117, 116]  # Source: Wikipedia.org

nth_person = int(input('Enter N (1-5): '))

if (nth_person >= 1) and (nth_person <= 5):
    print('The {}th oldest person lived {} years' \
        .format(nth_person, oldest_people[nth_person-1]))
    
# Some common operations on lists
# my_list[start:end]
my_list = [1, 2, 3]
print(my_list[1:3])
# my_list1 + my_list2
my_list = [1, 2] + [3] 
print(my_list)
# my_list[len(my_list):] = [x] appends element to end of list but append is better only used as reference
my_list = [1, 2, 3]
my_list[len(my_list):] = [9]
print(my_list)
# del my_list[i]
my_list = [1, 2, 3]
del my_list[1]
print(my_list)

# List methods
# list.append(x) appends 1 element
my_list = [5, 8]
my_list.append(16)
# list.extend([x]) appends multiple elements
my_list = [5, 8]
my_list.extend([4, 12])
# list.insert(i, x)	insters x before index position i
my_list = [5, 8]
my_list.insert(1, 1.7)
# list.remove(x) removes first element from list with value x
my_list = [5, 8, 14]
my_list.remove(8)
# list.pop() removes and returns last item in list (here val = 14)
my_list = [5, 8, 14]
val = my_list.pop()
# list.pop(i) removes and returns item at position i in the list
my_list = [5, 8, 14]
val = my_list.pop(0)
# list.sort() sort the items of the list in place (here sorts to [5, 8, 14])
my_list = [14, 5, 8]
my_list.sort()
# list.reverse() reverse the elements of list in place (here sorts to [8, 5, 14])
my_list = [14, 5, 8]
my_list.reverse()
# list.index(x) Returns index of first item in list with value x.
my_list = [5, 8, 14]
print(my_list.index(14))
# list.count(x)	Counts the number of times value x is in list.
my_list = [5, 8, 5, 5, 14]
print(my_list.count(5))
      
# Program sorts names in alphabetical order
user_input = input()
short_names = user_input.split()

short_names.sort()
short_names.reverse()

print(short_names)

# program finds the maximum even number
# User inputs string w/ numbers: '203 12 5 800 -10'
user_input = input('Enter numbers:')

tokens = user_input.split()  # Split into separate strings

# Convert strings to integers
nums = []
for token in tokens:
    nums.append(int(token))

# Print each position and number
print()  # Print a single newline
for index in range(len(nums)):
    value = nums[index]
    print('{}: {}'.format(index, value))

# Determine maximum even number
# User inputs string w/ numbers: '203 12 5 800 -10'
user_input = input('Enter numbers:')

tokens = user_input.split()  # Split into separate strings

# Program Converts strings to integers
# User inputs string w/ numbers: '203 12 5 800 -10'
user_input = input('Enter numbers:')

tokens = user_input.split()  # Split into separate string
nums = []
for token in tokens:
    nums.append(int(token))

# Print each position and number
print()  # Print a single newline
for index in range(len(nums)):
    value = nums[index]
    print('{}: {}'.format(index, value))

    
# Program Determines maximum even number
max_num = None
for num in nums:
    if (max_num == None) and (num % 2 == 0):
        # First even number found
        max_num = num
    elif (max_num != None) and (num > max_num ) and (num % 2 == 0):
        # Larger even number found
        max_num = num

print('Max even #:', max_num)


# Program finds the sum of a lists elements
# User inputs string w/ numbers: '203 12 5 800 -10'
user_input = input('Enter numbers: ')

tokens = user_input.split()  # Split into separate strings

# Convert strings to integers
# User inputs string w/ numbers: '203 12 5 800 -10'
user_input = input('Enter numbers: ')

tokens = user_input.split()  # Split into separate strings

# Convert strings to integers
print()
nums = []
for pos, token in enumerate(tokens):
    nums.append(int(token))
    print('{}: {}'.format(pos, token))

sum = 0
for num in nums:
    sum += num

print('Sum:', sum)

# Built-in functions supporting list objects
# all(list) True if every element in the list is True (!=0), or if the list is empty
print(all([1, 2, 3])) # True
print(all([0, 1, 2])) # False
# any(list) True if any element on the list is True
print(any([0, 2])) # True
print(any([0, 0])) # False
# max(list) gets maximum val element on list 
print(max([-3, 5, 25]))	
# min(list) gets minmum val element on list
print(min([-3, 5, 25]))	
# sum(list) gets sum of all elements on list
print(sum([-3, 5, 25]))	


# Program gets user guesses
user_input = input()
test_grades = list(map(int, user_input.split())) # test_grades is an integer list of test scores


sum_extra = 0 # Initialize 0 before your loop

for grade in test_grades:
    if grade >= 100:
        sum_extra += grade - 100

print('Sum extra:', sum_extra)


# Program Prints out an hourly report on temprature
user_input = input()
hourly_temperature = user_input.split()

for element in hourly_temperature:
    print(element, end= '')
    if element != hourly_temperature[len(hourly_temperature)-1]:
        print(' -> ', end='')
    else:
        print(' ')
        
        
# A list can contain another list also known as list nesting
my_list = [[10, 20], [30, 40]]
print('First nested list:', my_list[0])
print('Second nested list:', my_list[1])
print('Element 0 of first nested list:', my_list[0][0]
      

# Program represents a tic-tac-toe board using nested lists aka multi-dimensional data structure
tic_tac_toe = [
    ['X', 'O', 'X'],
    [' ', 'X', ' '],
    ['O', 'O', 'X']
]

print(tic_tac_toe[0][0], tic_tac_toe[0][1], tic_tac_toe[0][2])
print(tic_tac_toe[1][0], tic_tac_toe[1][1], tic_tac_toe[1][2])
print(tic_tac_toe[2][0], tic_tac_toe[2][1], tic_tac_toe[2][2])

# Program uses a two-dimensional list to print the distance between cities 
# direct driving distances between cities, in miles
# 0: Boston    1: Chicago    2: Los Angeles

distances = [
    [
        0,  
        960,  # Boston-Chicago
        2960 # Boston-Los Angeles
    ],
    [
        960,  # Chicago-Boston
        0,
        2011  # Chicago-Los Angeles
    ],
    [
        2960,  # Los Angeles-Boston
        2011,  # Los-Angeles-Chicago
        0
    ]
]

user_input = input('Enter city pair (Ex: 1 2) -- ').strip()
city1, city2 = user_input.split()

print('Distance: {} miles'.format(distances[int(city1)][int(city2)]))

# Example of iterating through list elements
# code will run by removing "Cell" and "ROW-->" only added for clarity
'''      
currency = [
                     CELL
        [1.00, 5.00, 10.0], # US Dollars
        [0.75, 3.77, 7.53], # Euros
 ROW -->[0.65, 3.25, 6.50]  # British pounds
]

for row in currency:
    for cell in row:
        print(cell, end=' ')
    print()
'''
currency = [
   [1, 5, 10 ],  # US Dollars
   [0.75, 3.77, 7.53],  #Euros
   [0.65, 3.25, 6.50]  # British pounds
]
for row_index, row in enumerate(currency):
   for column_index, item in enumerate(row):
       print('currency[{}][{}] is {:.2f}'.format(row_index, column_index, item))

      
# Program prints multiplication table
user_input= input()
lines = user_input.split(',')

# This line uses a construct called a list comprehension,
# to convert the input string into a two-dimensional list.
# Ex: 1 2, 2 4 is converted to [ [1, 2], [2, 4] ]

mult_table = [[int(num) for num in line.split()] for line in lines]

for lst in mult_table:
    for i in range(len(lst)):
        print(lst[i], end='')
        if i != len(lst)-1:
            print(' | ', end='')
    print()
      
      
# List slicing notation
boston_bruins = ['Tyler', 'Zdeno', 'Patrice']
print('Elements 0 and 1:', boston_bruins[0:2])
print('Elements 1 and 2:', boston_bruins[1:3])
# Prints: 
# Elements 0 and 1: ['Tyler', 'Zdeno']
# Elements 1 and 2: ['Zdeno', 'Patrice']
      
# can use negative indices when slicing
election_years = [1992, 1996, 2000, 2004, 2008]
print(election_years[0:-1])  # Every year except the last [1992, 1996, 2000, 2004]
print(election_years[0:-3])  # Every year except the last three [1992, 1996]
print(election_years[-3:-1])  # The third and second to last years [2000, 2004]
      
# List striding
# my_list[start:end:stride] Get a list of every stride element from start to end (minus 1).
my_list = [5, 10, 20, 40, 80]
print(my_list[0:5:3])
# Outputs: [5, 40]
      
      
# Program demonstrates how loops can modify lists
      # Program converts negative values to 0
user_input = input('Enter numbers: ')

tokens = user_input.split()

# Convert strings to integers
nums = []
for token in tokens:
    nums.append(int(token))

# Print each position and number
print()
for pos, val in enumerate(nums):  
    print('{}: {}'.format(pos, val))

# Change negative values to 0
for pos in range(len(nums)):
    if nums[pos] < 0:
        nums[pos] = 0

# Print new numbers
print('New numbers: ')
for num in nums:
    print(num, end=' ')


# List comprehension allows for modification on elemnts with expressions below are the 3 components
# An expression component to evaluate for each element in the iterable object.
# A loop variable component to bind to the current iteration element.
# An iterable object component to iterate over (list, string, tuple, enumerate, etc).
      # new_list = [expression for loop_variable_name in iterable]
my_list = [10, 20, 30]
list_plus_5 = [(i + 5) for i in my_list]

print('New list contains:', list_plus_5)
      
# Program adds 10 to every element
my_list = [5, 20, 50]
for i in range(len(my_list)):
    my_list[ i ] += 10
print(my_list)
      
# Program converts every element to a string
my_list = [5, 20, 50]
for i in range(len(my_list)):
    my_list[ i ] = str(my_list[ i ])
print(my_list)
      
# Program converts input into a list of integers
inp = input('Enter numbers:')
my_list = []
for i in inp.split():
    my_list.append(int(i))
print(my_list)
      
# Program finds the sum of each row in a two-dimensional list
my_list = [[5, 10, 15], [2, 3, 16], [100]]
sum_list = []
for row in my_list:
    sum_list.append(sum(row))
print(sum_list)
      
# Program finds the sum of the row with the smallest sum in a two dimensional table
my_list = [[5, 10, 15], [2, 3, 16], [100]]
sum_list = []
for row in my_list:
    sum_list.append(sum(row))
min_row = min(sum_list)
print(min_row)

# Program returns a list of even numbers
# Get a list of integers from the user
numbers = [int(i) for i in input('Enter numbers:').split()]

# Return a list of only even numbers
even_numbers = [i for i in numbers if (i % 2) == 0]
print('Even numbers only:', even_numbers)
      
      
# Program alphabetically sorts book titles
books = []
prompt = 'Enter new book: '
user_input = input(prompt).strip()

while (user_input.lower() != 'exit'):
    books.append(user_input)
    user_input = input(prompt).strip()

books.sort()

print('\nAlphabetical order:')
for book in books:
    print(book)
      
# Program does a matrix multiplication of 4x2 and 2x3 matrices
m1_rows = 4
m1_cols = 2
m2_rows = m1_cols  # Must have same value
m2_cols = 3

m1 = [
    [3, 4],
    [2, 3],
    [1, 2],
    [0, 2]
]

m2 = [
    [5, 4, 4],
    [0, 2, 3]
]

m3 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# m1 * m2 = m3
for i in range(m1_rows):  # for each row of m1
    for j in range(m2_cols):  # for each column of m2
        # Compute dot product
        dot_product = 0
        for k in range(m2_rows): #  for each row of m2
            dot_product += m1[i][k] * m2[k][j]

        m3[i][j] = dot_product

for i in range(m1_rows):
    for j in range(m2_cols):
        print('{}'.format(m3[i][j]), end=' ')
    print()  # Print single newline

      
# Program reads a list of integers and prints the smallest and largest integers on the list      
# Reading a number
n = int(input())

# Setting min amd max value to n
minVal = n
maxVal = n

# Looping till input is positive
while(n>0):

    # Checking n is smaller than minVal
    if(minVal>n):
        # Updating minVal
        minVal = n

    # Checking n is larger than maxVal
    if(maxVal<n):
        # Updating maxVal
        maxVal = n

    # Reading a number
    n = int(input())

# printing minVal and maxVal
print(minVal,"and",maxVal)

      
# Program prints all integers less than or equal to that last threshold value 
def read_numbers():
    size = int(input())
    nums = []
    for i in range(size):
        nums.append(int(input()))
    thresold = int(input())
    return nums, thresold

def filter_numbers(nums, threshold):
    result = []
    for num in nums:
        if num <= threshold:
            result.append(str(num))
    return ','.join(result)


nums, threshold = read_numbers()
print(filter_numbers(nums, threshold), end=',')
      
# Program adjusts a data set 
# enter number of floating point numbers that will be followed
n = int(input())
# empty list is declared to store the floating point values
val = []
# loop to store n floating point numbers
for i in range(n):
    val.append(float(input()))
# display the normalized floating point values
for i in range(n):
    your_value = val[i]/max(val)
    print('{:.2f}'.format(your_value))
