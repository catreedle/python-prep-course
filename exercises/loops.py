# Loop and Print
# Add some code inside the following for loop to print the current value of num on each iteration. 
# Before you execute the code: What sequence of numbers do you expect to be printed?
for num in range(0, 11, 2):
    print(num) # 0 2 4 6 8 10
    
# Countdown
# The following code prints the numbers from 1 to 10. Modify it so that it instead prints the numbers
# from 10 to 1 in descending order, followed by 'Launch!'.
for i in range(10, 0, -1):
    print(i)

print('Launch!')

# Triple Greeting
# Write a loop that prints the value of the greeting variable three times.
greeting = 'Aloha!'
for _ in range(3):
    print(greeting)

# Take Two
# Write a for loop that iterates over the integers from 1 to 100 and prints the result of multiplying
# each integer by 2.
for num in range(1, 101):
    print(num * 2)

# Looping over List Elements
# Using the code below as a starting point, write a while loop that prints the elements of lst 
# at each index and terminates after printing the last element of the list.
lst = [1, 3, 7, 15]
index = 0
while index < len(lst):
    print(lst[index])
    index += 1

# Greet Your Friends
# Your friends just showed up! Given the following list of names, use a for loop 
# to greet each friend individually.
friends = ['Sarah', 'John', 'Hannah', 'Dave']
for friend in friends:
    print(f'Hello, {friend}!')
    
# Write a for loop that iterates over the elements of the list cities and prints the length of each string. 
# If the element is None, use the continue statement to skip forward to the next iteration 
# without printing anything.
cities = ['Istanbul', 'Los Angeles', 'Tokyo', None,
          'Vienna', None, 'London', 'Beijing', None]
for city in cities:
    if city is None:
        continue
    print(len(city))
    
# And on and on and on
# The following code keeps looping forever. (You can hit Ctrl-C to stop it.)
# Why does the loop keep running? Modify it so that it stops after the first iteration.
while True:
    print("and on")
    break

# Finding Nemo
# Loop over the elements of the fish_list list below, logging each one. 
# Terminate the loop immediately after printing the string 'Nemo'.
fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']
for fish in fish_list:
    print(fish)
    if fish == 'Nemo':
        break

index = 0
while index < len(fish_list):
    print(fish_list[index])
    if(fish_list[index] == 'Nemo'):
        break
    index += 1

# Loop on Command
# Modify the following code so the loop continues iterating until the user inputs 'yes'.
while True:
    print('Should I stop looping?')
    answer = input()
    if answer == 'yes':
        break
    print('Enter "yes" if you want me to stop.')