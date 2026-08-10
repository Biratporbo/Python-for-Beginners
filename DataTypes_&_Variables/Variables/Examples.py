# Example to Print Python Variables

counter = 100   # Creates an integer variable
miles = 1200.0  # Creates a floating point variable
name = "Birat"  # Creates a string variable

print(counter)
print(miles)
print(name)

# Deleting Python Variable
# del var_a, var_b

# Example

counter = 120
print(counter)

del counter

# Getting Type of Variable
x = "Birat"
y = 10
z = 10.6

print(type(x))
print(type(y))
print(type(z))

# Casting Python Variable
x = float(9)    # x will be 9.0
y = str(10)     # y will be '10'
z = int(10)     # z will be 10

print("x: ", x)
print("y: ", y)
print("z: ", z)


# Case Sensitive of Python variables
age = 23
Age = 23

print("age: ", age)
print("Age: ", Age)

# Python Multiple Assignment Values Put
a = b = c = 23
print(a)
print(b)
print(c)


# Another Method 
a, b, c = 2151, 23, "Birat"

print(a)
print(b)
print(c)

# Python Local Variables
def sum(x, y):
    sum = x + y
    return sum
print(sum(5, 10))

# Global Variables
x, y = 10, 9
def sum():
    sum = x + y
    return sum
print(sum())