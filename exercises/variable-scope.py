# What's my value? (Part 1)
# What will the following code do and why? Don't run it until you have tried to answer.
# This code will print 20 because the condition is true and my_value is set to 20 globally.
if True:
    my_value = 20

print(my_value)

# What's my value? (Part 2)
# What will the following code do and why? Don't run it until you have tried to answer.
# This code will raise a name error because x is declared as a new local variable in the function and
# it doesn't know what to add to. **correction: UnboundLocalError
x = 10

def my_function():
    x = x + 5
    print(x)

# my_function()

# What's my value? (Part 3)
# What will the following code do and why? Don't run it until you have tried to answer.
# This code will output 1 to the console because the local variable a is declared and it is accessible from
# the if block statement.
def my_function():
    a = 1

    if True:
        print(a)

my_function()

# What's my value? (Part 4)
# What will the following code do and why? Don't run it until you have tried to answer.
# This code will print 1 into the console. a is a global variable and can be accessed inside the function.
a = 1

def my_function():
    print(a)

my_function()

# What will the following code do and why? Don't run it until you have tried to answer.
# This code will print 1 to the console, since it's first declared as a global variable accessible from the 
# body of the function. my_function then reassigns a as a local variable with the value 2, 
# but we do not print this. **WRONG ANSWER**

# **CORRECTION**
# Python detects that a is being assigned within the my_function function and therefore treats it as 
# a local variable. However, since we are trying to print the local a variable's value before 
# it has been assigned a value, we get an error. UnboundLocalError
a = 1

def my_function():
    # print(a)
    a = 2

my_function()

# What's my value? (Part 6)
# What will the following code do and why? Don't run it until you have tried to answer.
# It will print 1 to the console because the global variable a value is 1. The line a = 2 in the body
# of my_function creates new local variable a and assigns 2 to it, but this variable is unused.
a = 1

def my_function():
    a = 2

my_function()
print(a)

# What's my value? (Part 7)
# What will the following code do and why? Don't run it until you have tried to answer.
# It will print 2. In the my_function body, it is stated that a is global variable (with global keyword). We reassigned the value of
# a to 2, after the function is invoked global variable a value is now 2, 
# and it is the value we print to the console
a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)

# What's my value? (Part 8)
# What will the following code do and why? Don't run it until you have tried to answer.
# This will cause a NameError because we attemp to print a variable before defining it.
# print(greeting)

greeting = 'Hello world!'

# What's my value? (Part 9)
# What will the following code do and why? Don't run it until you have tried to answer.
# This will print 7. Here we use two different kinds of a, first as a global variable, second as an argument
# to my_function. When we pass a to my_function, we use the value (7) as argument to the function and
# work through the expression in the function body, b += 10 ------ b = 7 + 10 = 17
# but the value of a as global variable remain unchanged
a = 7

def my_function(b):
    b += 10

my_function(a)
print(a)

# What's my value? (Part 10)
# What will the following code do and why? Don't run it until you have tried to answer.
# This will cause an error because my_function is trying to reassign value to the first index of
# local variable b before defining it. **WRONG**

# **CORRECTION**
# This example shows how lists, being mutable objects, can be modified within a function, 
# affecting the original list in the global scope.
# The list b is initialized on line 1 outside the function my_function. Inside the function, on line 4,
# the first element of b is changed to 10. Since b is not a local variable within my_function() 
# but we are directly referencing b from the global scope, the change b[0] = 10 impacts the global variable b.
# Consequently, after the execution of my_function(), the global list b reflects this modification, 
# and printing b will display [10, 2, 3].

b = [1, 2, 3]

def my_function():
    b[0] = 10

my_function()
print(b)