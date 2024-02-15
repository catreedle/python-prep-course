# Use the REPL and the arithmetic operators to extract the individual digits of 4936:

# One place is 6.
# Tens place is 3.
# Hundreds place is 9.
# Thousands place is 4.
# Each digit may require multiple Python statements.

number = 4936
ones = number % 10
tens = (number % 100) // 10
hundreds = (number % 1000) // 100
thousands = number // 1000
print(thousands, hundreds, tens, ones)

# alternative
# ones = number % 10
# number = number // 10
# tens = number % 10
# number = number // 10
# hundreds = number % 10
# thousands = number // 10