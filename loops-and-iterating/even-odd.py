# In this problem, you should write code that creates a new list with one element for each number in my_list.
# If the original number is an even, then the corresponding element in the new list
# should contain the string 'even'; otherwise, the element should contain 'odd'.

my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

new_list = []
for num in my_list:
    if num % 2:
        new_list.append('odd')
    else:
        new_list.append('even')

print(new_list)

# alternative
# 1
# result = ['even' if num % 2 == 0 else 'odd' for num in my_list]

# 2
# def odd_or_even(num):
#     return 'odd' if num % 2 else 'even'

# result = [odd_or_even(num) for num in my_list]
# print(result)

