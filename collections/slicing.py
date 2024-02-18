# Use slicing to write Python code to print a 6-character substring of 'Launch School'
# that begins with the first c.

s = 'Launch School'
c_index = s.index('c')
print(s[c_index:c_index + 6])