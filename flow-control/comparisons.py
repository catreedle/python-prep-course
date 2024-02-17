# Write a function that takes a single integer argument and prints a message that describes whether:

# the value is between 0 and 50 (inclusive)
# the value is between 51 and 100 (inclusive)
# the value is greater than 100
# the value is less than 0

def comparisons(value):
    if value >=0 and value <= 50:
        print(f'{value} is between 0 and 50')
    elif 51 <= value <= 100:
        print(f'{value} is between 51 and 100')
    elif value > 100:
        print(f'{value} greater than 100')
    else:
        print(f'{value} less than 0')


comparisons(2007)          