my_list = [6, 3, 0, 11, 20, 4, 17]

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
print()
for num in my_list:
    print(num)
    
# even-odd

print('\neven')
index = 0
while index < len(my_list):
    num = my_list[index]
    if num % 2 == 0:
        print(num)
    index += 1

print('\nodd')
for num in my_list:
    if num % 2:
        print(num)
