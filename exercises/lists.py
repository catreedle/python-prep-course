# First Element
# Write a function that returns the first element of a list provided as an argument. For example:
def first(l):
    if l:
        return l[0]
    else:
        return None
print(first(['Earth', 'Moon', 'Mars']))  # Earth
print(first([]))

# Last Element
# Write a function that returns the last element of a list provided as an argument. For example:
def last(lst):
    return lst[len(lst) - 1] if lst else None
print(last(['Earth', 'Moon', 'Mars']))  # Mars
# Be sure to handle the case where the input list is empty.

# Add + Delete
# We are given the following list of energy sources.
energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']
# Write some code to remove 'fossil' from the list, then add 'geothermal' to the end of the list.
def replace_element(lst, el1, el2):
    lst.remove(el1)
    lst.append(el2)
    return lst

print(replace_element(energy, 'fossil', 'geothermal'))

# Alphabet
# Split the string alphabet into a list of characters.
alphabet = 'abcdefghijklmnopqrstuvwxyz'
list_of_chars = list(alphabet)
print(list_of_chars)

# Filter
# Count the number of elements in scores that are 100 or above.
scores = [96, 47, 113, 89, 100, 102]
counter = 0
for score in scores:
    if score >= 100:
        counter += 1
print(counter)

count = [score for score in scores if score >= 100]
print(len(count))

# Vocabulary
# You've been given a list of vocabulary words grouped into sub-lists, by meaning. 
# This is a two-dimensional list or a nested list. Write some code that iterates through and 
# prints all the words, one per line.
vocabulary = [
    ['happy', 'cheerful', 'merry', 'glad'],
    ['tired', 'sleepy', 'fatigued', 'drained'],
    ['excited', 'eager', 'enthused', 'animated'],
]
for lst in vocabulary:
    for word in lst:
        print(word)

# Equality
# Predict the output of the code shown below. When you run the code, do you see what you expected? 
# Why or why not?
# I expected it to print True. Because the object referenced by list1 has the same value as the 
# object referenced by list2


list1 = [2, 6, 4]
list2 = [2, 6, 4]

# print(list1 == list2)

# Type
# How can you check if a variable holds a value that is a list? Given two variables,
# verify whether the values they hold are lists.
some_value1 = [0, 1, 0, 0, 1]
some_value2 = 'I leave you my Kingdom, take good care of it.'
print(type(some_value1).__name__ == 'list')
print(type(some_value2).__name__ == 'list')
# print(isinstance(some_value1, list))  # True
# print(isinstance(some_value2, list))  # False

# Travel
# The destinations list contains a list of travel destinations.
destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']
# Write a function that, without using the built-in in operator, checks whether a specific destination 
# is included within destinations. For example: When checking whether 'Barcelona' is contained in destinations, the expected output is True, whereas the expected output for 'Nashville' is False.
def contains(city, destinations):
    for destination in destinations:
        if city == destination:
            return True
    return False
print(contains('Barcelona', destinations))  # True
print(contains('Nashville', destinations))  # False

# Passcode
# We generated parts of a passcode and now want to combine them into a string.
# Write some code that returns a string, with each portion of the passcode separated by a hyphen (-).
passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']
print('-'.join(passcode))
# Write some code here.
# Expected return value: '11-jZ5-hQ3f*-8!7g3-p3Fs'

# Checking items off the grocery list
# We have a grocery list. As we check off items on that list, we want to remove them from the list.

# Write code that removes the items from grocery_list, one by one, until it is empty. 
# If you print the elements you remove, the expected behavior would look as follows.

grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

# Your code.
grocery_list = list(reversed(grocery_list))
while len(grocery_list) > 0:
    print(grocery_list.pop())

# while grocery_list:
#     checked_item = grocery_list.pop(0)
#     print(checked_item)

print(grocery_list)
    
    
    

