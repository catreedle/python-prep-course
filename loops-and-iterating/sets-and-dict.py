# set
my_set = {1000, 2000, 3000, 4000, 5000}
for member in my_set:
    print(member)
    
my_dict = {'a': 1, 'b': 2, 'c': 3}
for item in my_dict.items():
    print(item)

# tuple unpacking
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.items():
    print(f'{key} = {value}')