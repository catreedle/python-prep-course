# Write a find_integers function that returns a list of all the integers from my_tuple:

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)

def find_integers(els):
    result = []
    for el in els:
        if type(el) is int:
            result.append(el)
    
    return result

# comprehension way
# def find_integers(els):
#     return [el for el in els if type(el) is int]
            
integers = find_integers(my_tuple)
print(integers)                    # [1, 3, -4]