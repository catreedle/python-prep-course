a = float(input('Enter the first number: '))
b = float(input('Enter the second number: '))

def multiply(num1, num2):
    return num1 * num2

result = multiply(a, b)
print(f'{a} * {b} = {result}')


# def multiply(left, right):
#     return left * right

# def get_number(prompt):
#     entry = input(prompt)
#     return float(entry)

# first_number = get_number('Enter the first number: ')
# second_number = get_number('Enter the second number: ')
# product = multiply(first_number, second_number)
# print(f'{first_number} * {second_number} = {product}')