# Yes? No? Part 1
# The code provided below randomly initializes random_number to either 0 or 1 each time it is executed.
# Write an if statement that prints Yes! if random_number is 1, and No. if random_number is 0.
import random
random_number = random.randint(0, 1)
if random_number:
    print('Yes!')
else:
    print('No.')

# Yes? No? Part 2 (conditional expression)
# Rewrite your code from the previous exercise to use a ternary expression.
print('Yes!') if random_number else print('No.')
# print('Yes!' if random_number else 'No.')

# Check the Weather, Part 1
# Initialize a variable weather with a string value being 'sunny', 'rainy', 
# or whatever weather condition you choose. Then, write an if statement that prints:

# It's a beautiful day! if weather's value is 'sunny'
# Grab your umbrella. if weather's value is 'rainy'
# Let's stay inside. if weather's value is anything else
# Test your code with different values for weather.
weather = input('How\'s the weather today?\n')
if weather == 'sunny':
    print('It\'s a beautiful day!')
elif weather == 'rainy':
    print('Grab your umbrella.')
else:
    print("Let's stay inside.")
    
# Check the Weather, Part 2
# Take your code from the previous Check the Weather exercise and rewrite it as a match-case statement.
# Feel free to add more cases besides 'sunny' and 'rainy'.
weather = input('How\'s the weather today?\n')
match weather:
    case 'sunny':
        print('It\'s a beautiful day!')
    case 'rainy':
        print('Grab your umbrella.')
    case 'snowy':
        print('Let\'s build a snowman!')
    case _:
        print("Let's stay inside.")