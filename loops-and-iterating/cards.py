# nested loop
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = [
    '2', '3', '4', '5', '6', '7', '8', '9', '10',
    'Jack', 'Queen', 'King', 'Ace',
]

deck = []
for suit in suits:
    for rank in ranks:
        card = f'{rank} of {suit}'
        deck.append(card)

print(deck)

nums = [1, 2, 3]
my_list = []
for num in nums:
    sublist = [num]
    new_nums = nums.copy()
    new_nums.remove(num)
    for item in new_nums:
        sublist.append(item)
    
    my_list.append(sublist)


print(my_list)
    