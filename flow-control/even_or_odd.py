def even_or_odd(num):
    modulus = num % 2
    match modulus:
        case 0:
            return 'even'
        case _:
            return 'odd'
        
# def even_or_odd(num):
#     if num % 2 == 0:
#         return 'even'
#     else:
#         return 'odd'

print(even_or_odd(6))