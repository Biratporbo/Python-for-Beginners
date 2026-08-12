# Examples of Python Logical Operators
var = 5

print(var > 3 and var < 10)
print(var > 3 or var < 4)
print(not (var > 3 and var < 10))


# Example 1: Logical Operators With Boolean Conditions
x = 10
y = 20
print("x > 0 and x < 10:",x > 0 and x < 10)
print("x > 0 and y > 10:",x > 0 and y > 10)
print("x > 10 or y > 10:",x > 10 or y > 10)
print("x%2 == 0 and y%2 == 0:",x%2 == 0 and y%2 == 0)
print ("not (x+y>15):", not (x+y)>15)


# Example 2: Logical Operators With Non- Boolean Conditions
x = 19
y = 10
z = 0
print("x and y: ", x and y)
print("x or y: ", x or y)
print("z or x: ", z or x)
print("y or z: ", y or z)


# Example 3: Logical Operators With Strings and Tuples
a = "birat"
b = tuple()
print("a and b: ", a and b)
print("b or a: ", b or a)


# Example 4: Logical Operators To Compare Sequences (Lists)
x = [1, 2, 3]
y = [19, 29, 39]
print("x and y:",x and y)
print("x or y:",x or y)
