# Sequence show case
# i.List Data Type -->
# [2023, "Python", 3.11, 5+6j, 1.23E-4]

# type([2023, "Python", 3.11, 5+6j, 1.23E-4])
list = ['Rohit', 2100, 7.45, 'Arijit', 8.67]
tinylist = [2245, 'Arijit']

print (list)            # Prints complete list
print (list[0])         # Prints first element of the list
print (list[1:3])       # Prints elements starting from 2nd till 3rd 
print (list[2:])        # Prints elements starting from 3rd element
print (tinylist * 2)    # Prints list two times
print (list + tinylist) # Prints concatenated lists


# ii. Tuple Data type -->
# (2023, "Python", 3.11, 5+6j, 1.23E-4)
# type((2023, "Python", 3.11, 5+6j, 1.23E-4)) <--- <class 'tuple'>
tuple = ( 'Birat', 786 , 2.23, 'Rahul', 70.2  )
tinytuple = (123, 'Rahul')

print (tuple)               # Prints the complete tuple
print (tuple[0])            # Prints first element of the tuple
print (tuple[1:3])          # Prints elements of the tuple starting from 2nd till 3rd 
print (tuple[2:])           # Prints elements of the tuple starting from 3rd element
print (tinytuple * 2)       # Prints the contents of the tuple twice
print (tuple + tinytuple)   # Prints concatenated tuples


# iii. Range Data Type -->
# range(start, stop, step)
for i in range(5):
  print(i)
  
for i in range(1, 5, 2):
  print(i)