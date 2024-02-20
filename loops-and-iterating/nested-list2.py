# Print all of the even numbers in the following list of nested lists. This time, don't use any for loops.

my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

index_a = 0
while index_a < len(my_list):
    current_list = my_list[index_a]
    index_b = 0
    while index_b < len(current_list):
        num = current_list[index_b]
        if num % 2 == 0:
            print(num)
        index_b += 1
    index_a += 1
    
    
    