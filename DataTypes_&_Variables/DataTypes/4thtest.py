# Binary Show Case --->

# i. Byte Data Type -->
# We can create bytes in Python using the built-in bytes() function or by prefixing a sequence of numbers with b.

# Example using the built-in bytes() function to explicitly specify a sequence of numbers representing ASCII values −
# Using bytes() function to create bytes
b1 = bytes([65, 66, 67, 68, 69])
print(b1)

# Using prefix 'b' to create bytes
b2 = b'Hello'
print(b2)


# ii. Bytearray Data Type
# by converting an existing bytes or bytearray object. For this, we use bytearray() function.
# Example creating a bytearray by passing an iterable of integers representing byte values −
# Creating a bytearray from an iterable of integers
value = bytearray([98, 105, 114, 97, 116])
print(value)

# Output show like --> bytearray(b'birat')


# iii. Memory View Data Type
'''
These methods include using the memoryview() constructor, slicing bytes or bytearray objects, 
extracting from array objects, or using built-in functions like open() when reading from files.
'''
# Example 
'''
In the given example, we are creating a memoryview object directly by passing a supported object to the 
memoryview() constructor. The supported objects generally include byte arrays (bytearray), bytes (bytes), 
and other objects that support the buffer protocol −
'''
import array
arr = array.array('i', [1, 2, 3, 4, 5])
view = memoryview(arr)
print(view)

