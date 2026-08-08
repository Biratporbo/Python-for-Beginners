# Boolean Data Type Show Case --->
# A Boolean number has only two possible values, as represented by the keywords, 
# True and False. They correspond to integer 1 and 0 respectively.

'''
>>> type (True)
<class 'bool'>
>>> type(False)
<class 'bool'>
'''

#Example 
a = True
print(a)
print(type(a))

# Return false as a is not equal to b
a = 2
b = 4
print(bool(a==b))

# Following also prints the same 
print(a==b)

#Return False as a is None
a = None
print(bool(a))

# Return false as a is an empty sequence
a = ()
print(bool(a))

#Return false as a is 0
a = 0.0
print(bool(a))

# Return false as a is 10
a = 10
print(bool(a))