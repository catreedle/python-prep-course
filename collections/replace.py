# Write Python code to replace all the : characters in the string below with +.

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
info_split = info.split(':')
info_join = ('+').join(info_split)

print(info_join)

# from documentation:
print(info.replace(':', '+'))