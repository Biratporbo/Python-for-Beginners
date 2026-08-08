# Dictionary Data Type Show Case --->
# >>> {1:'one', 2:'two', 3:'three'}
# type({1:'one', 2:'two', 3:'three'}) <--- <class 'dict'>

# Example of Dictionary Data Type
dict = {}
dict['one'] = "This is One"
dict[2] = "This is Two" 

tinydict = {'name': 'Birat', 'code':2151, 'dept': 'Development'}

print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values