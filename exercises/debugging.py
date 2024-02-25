# Reading Error Messages
# You come across the following code. What errors does it raise for the given examples and 
# what exactly do the error messages mean?
# TypeError: find_first_nonzero_among() takes 1 positional argument but 6 were given
# It means the function invocation gives more arguments (6) than what it requires (1)
# TypeError: 'int' object is not iterable
# It means the function is given the argument type integer when it expects iterables.
def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n

print(find_first_nonzero_among((0, 0, 1, 0, 2, 0)))
print(find_first_nonzero_among({1,}))

# Weather Forecast
# Our predict_weather function should output a message indicating whether a sunny or cloudy day lies ahead.
# However, the output is the same every time the method is invoked. 
# Why? Fix the code so that it behaves as expected.
# We started by printing the value of sunshine. We can see that random.choice is working just fine, sometimes
# giving us 'True' and sometimes 'False'. However sunshine is always truthy because it is not an empty string,
# so it's always the block in if that is executed. To fix this we can change the condition to 
# if sunshine == 'True' or we can use boolean instead of string for the random.choice [True, False].


import random

def predict_weather():
    sunshine = random.choice([True, False])
    if sunshine:
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")

predict_weather()

# Multiply By Five
# When the user inputs 10, we expect the program to print The result is 50!, 
# but that's not the output we see. Why not?
# The built-in function input() gives us string, so n * 5 means make a copy of n five times.
# To have expected result, we must first convert the string to integer. number = int(input())
def multiply_by_five(n):
    return n * 5

# print("Hello! Which number would you like to multiply by 5?")
# number = int(input())

# print(f"The result is {multiply_by_five(number)}!")

# Pets
# Magdalena has just adopted a new pet! She wants to add her new dog, Bowser, to the pets dictionary. 
# After doing so, she realizes that her dogs Sparky and Fido have been mistakenly removed. 
# Help Magdalena fix her code so that all three of her dogs' names will be associated with 
# the key 'dog' in the pets dictionary.

pets = { 'cat': 'pepe', 'dog': ['sparky', 'fido'], 'fish': 'oscar' }

# pets['dog'] = 'bowser'
pets['dog'].append('bowser')

print(pets)  # Output: {'cat': 'pepe', 'dog': 'bowser', 'fish': 'oscar'}

# Confucius Says
# You want to have a small script delivering motivational quotes, but with the following code you run
# into a very common error message: TypeError: can only concatenate str (not "NoneType") to str.
# What is the problem and how can you fix it?
# This function does not return the value, so it defaults to returning None and then cause error when trying
# to concatenate. We should add return to each block inside the if condition.
def get_quote(person):
    if person == 'Yoda':
        return 'Do. Or do not. There is no try.'
    if person == 'Confucius':
        return 'I hear and I forget. I see and I remember. I do and I understand.'
    if person == 'Einstein':
        return 'Do not worry about your difficulties in Mathematics. I can assure you mine are still greater.'

print('Confucius says:')
print('"' + get_quote('Confucius') + '"')

# Populate List
# You want to add the numbers from 1 to 5 to a list, but the code below is not producing the expected result.
# How can you fix it?
# range(5) means i starts at zero and stops at the number before 5. To fix this we should append numbers 
# with i + 1 instead.
numbers = []

for i in range(5):
    numbers.append(i + 1)

print(numbers)

# Dictionary Access
# You are trying to access a value in a dictionary, but the code is giving you an error. 
# Can you change line 3 so that it prints "Unknown" instead of raising an error?
info = {'name': 'Srdjan', 'age': 38}

# print(info['city'])
# print(info.get('city') if info.get('city') else 'Unknown')
print(info.get('city', 'Unknown'))

# Matrix
# We wanted to create a matrix 3x3 so we could use it to build a Tic-Tac-Toe game. 
# However, we encountered an issue, as whenever we change a value in one nested list, 
# all nested lists are affected. Can you fix the code?
# When we append sub_list to matrix using for loop, we're assigning the exact same object
# with the same address for each list in matrix, therefore when we try to update one,
# all the list (that reference to the same object) are updated. We can fix this by
# making a copy of sub_list or appending the value ["-", "-", "-"] directly 
# in the for loop, so that it creates a new object each time.

sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    # matrix.append(sub_list)
    matrix.append(sub_list.copy())

matrix[0][0] = "X"
print(matrix) # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]

# Find Maximum
# Your colleague has implemented a custom function to find the maximum value in a list. 
# However, the function sometimes works correctly, but other times it produces incorrect results.
# Can you help your colleague fix the bug?
def find_maximum(numbers):
    if not numbers:
        return None
    max_number = numbers[0]
    # max_number = float('-inf')
    # second solution: we initialize max_number to negative infinity (float('-inf'))
    
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

print(find_maximum([45, 3, 10, 98, 22]))  # Expected 98
print(find_maximum([-1, 0, 5, 3]))         # Expected 5
print(find_maximum([-10, -3, -20, -2]))   # Expected -2

# Digit Product
# You've been asked to implement a function called digit_product that takes a string of digits as 
# an argument and returns the product of all the digits in the string.
# When testing the function, you find that it returns 0, which is not what you expect. 
# Can you identify the issue and correct the code?
def digit_product(str_num):
    digits = [int(n) for n in str_num]
    product = 1

    for digit in digits:
        product *= digit

    return product

result = digit_product('12345')
print(result)  # expected: 120, actual: 0