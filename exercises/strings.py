# Length
# Determine the length of the string "These aren't the droids you're looking for.".
print(len("These aren't the droids you're looking for."))

# ALL CAPS
# Convert the string 'confetti floating everywhere' to all upper case.
s = 'confetti floating everywhere'
upper_s = s.upper()
print(upper_s)

# Ignoring Case
# Using the following code, compare the value of name with the string 'RoGeR' while ignoring the case of 
# both strings. Print true if the values are the same; print false if they aren't. Next, 
# perform a case-insensitive comparison between the value of name and the string 'DAVE'.
name = 'Roger'
name_lower = name.lower()
print(name_lower == 'RoGeR'.lower())
print(name_lower == 'DAVE'.lower())
# The str.casefold method offers a more comprehensive approach to normalizing case than str.lower.
# It's primarily designed to facilitate case-insensitive string comparisons, especially in languages 
# where conventional methods of converting to lowercase may fall short.
print(name.casefold() == 'RoGeR'.casefold())
print(name.casefold() == 'DAVID'.casefold())

# Multiline String
# How can you assign the following rhyme to a single variable while preserving the line break?
# A pirate I was meant to be!
# Trim the sails and roam the sea!
multiline = 'A pirate I was meant to be!\nTrim the sails and roam the sea!'
# multiline = '''A pirate I was meant to be!
# Trim the sails and roam the sea!'''
print(multiline)

# Contains Character
# Write code that checks whether the string char_sequence contains the character x.
char_sequence = 'TXkgaG92ZXJjcmFmdCBpcyBmdWxsIG9mIGVlbHMu'
print('x' in char_sequence)

# Is Empty?
# Write a function that checks whether a string is empty or not. For example:
def is_empty(s):
    # return not len(s) > 0
    return not s
print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True

# Is Empty or Blank?
# Write an is_empty_or_blank function to determine whether a string is either empty or consists
# entirely of spaces. For example:
def is_empty_or_blank(s):
    s = s.strip()
    return not s
print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True

# Capitalize Words
# Write code that capitalizes the words in the string 'launch school tech & talk', so that you get 
# the string 'Launch School Tech & Talk'.
def capitalize_words(s):
    words = s.split()
    for i in range(len(words)):
        words[i] = words[i].capitalize()
    return ' '.join(words)

# def capitalize_words(string):
#     return string.title()

print(capitalize_words('launch school tech & talk'))

# Check Prefix
# Write a function that checks whether a string starts with a specific prefix.
def starts_with(s, prefix):
    len_prefix = len(prefix)
    return s[0:len_prefix] == prefix
# def starts_with(string, prefix):
#     return string.startswith(prefix)
print(starts_with("launch", "launch"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True

# Count Substrings
# Write a function that counts the number of occurrences of a substring in a string.
def count_substrings(s, substring):
    return s.count(substring)
print(count_substrings("lemon lemon lemon", "lemon")) # 3
print(count_substrings("laLAlaLA", "la")) # 2
print(count_substrings("launch", "uno")) # 0

