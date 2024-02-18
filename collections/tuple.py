# Write Python code to create a new tuple from (1, 2, 3, 4, 5).
# The new tuple should be in reverse order from the original.
# It should also exclude the first and last members of the original.
# The result should be the tuple (4, 3, 2).

tuple1 = (1, 2, 3, 4, 5)
tuple2 = tuple(reversed(tuple1))[1:len(tuple1) - 1]
print(tuple2)

# my_tuple = (1, 2, 3, 4, 5)
# result = my_tuple[3:0:-1]
# print(result)       # (4, 3, 2)