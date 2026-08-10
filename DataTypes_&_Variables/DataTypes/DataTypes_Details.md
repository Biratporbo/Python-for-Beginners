# Python Data Types Details

This document explains the built-in Python data types covered in this project and connects each file with the concept it demonstrates.

---

## 1st File: Numeric Types

File: `1sttest.py`

This file introduces the main numeric data types:

- `int`: whole numbers such as `10`, `-5`, and `200`
- `float`: decimal values such as `10.83` and `19.45`
- `complex`: values with real and imaginary parts such as `10+3j`
- `bool`: boolean values `True` and `False`

Example:

```python
var1 = 1
var2 = True
var3 = 10.83
var4 = 10 + 3j

print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))
```

This file shows that Python stores values by type and that `type()` can tell us which category a value belongs to.

---

## 2nd File: String Type

File: `2ndtest.py`

Strings are text values enclosed in quotes. They are one of the most commonly used data types in Python.

Key points:
- strings can be single or double quoted
- individual characters are accessed by index
- string slicing works with `[start:end]`
- strings can be concatenated and repeated

Example:

```python
str = 'Birat Dey'
print(str)
print(str[0])
print(str[2:5])
print(str * 2)
print(str + " TEST")
```

This file demonstrates that strings are useful for names, messages, and text-based input/output.

---

## 3rd File: Sequence Types

File: `3rdtest.py`

This file covers the main sequence types:

- `list`: ordered and mutable
- `tuple`: ordered and immutable
- `range`: sequence of numbers generated in order

Examples:

```python
list1 = ['Rohit', 2100, 7.45, 'Arijit', 8.67]
tuple1 = ('Birat', 786, 2.23, 'Rahul', 70.2)

print(list1[1:3])
print(tuple1[2:])

for i in range(5):
    print(i)
```

Lists and tuples are used to store multiple values in a single variable, while `range()` is commonly used in loops.

---

## 4th File: Binary Data Types

File: `4thtest.py`

This file introduces binary-related data types:

- `bytes`: immutable sequence of bytes
- `bytearray`: mutable sequence of bytes
- `memoryview`: view of memory data in a structured way

Examples:

```python
b1 = bytes([65, 66, 67, 68, 69])
b2 = b'Hello'

value = bytearray([98, 105, 114, 97, 116])
print(b1)
print(b2)
print(value)
```

These types are useful when working with binary data, file content, and lower-level memory operations.

---

## 5th File: Dictionary Data Type

File: `5thtest.py`

A dictionary stores data as key-value pairs. It is one of the most useful built-in Python data structures.

Example:

```python
dict = {}
dict['one'] = "This is One"
dict[2] = "This is Two"

tinydict = {'name': 'Birat', 'code': 2151, 'dept': 'Development'}

print(dict['one'])
print(dict[2])
print(tinydict.keys())
print(tinydict.values())
```

Dictionaries are often used to represent records, settings, JSON-like data, and mappings.

---

## 6th File: Set Data Type

File: `6thtest.py`

A set is an unordered collection of unique values. It does not keep duplicate items.

Key points:
- sets are unordered
- duplicate values are removed automatically
- sets are useful for membership checks and unique storage

Example:

```python
set1 = {123, 199, 89, 98}
set2 = {'Java', 'Python', 'JavaScript'}

print(set1)
print(set2)
```

Sets are great when you want to store only unique values.

---

## 7th File: Boolean and None Types

File: `7thtest.py`

This file explains:

- `bool`: `True` or `False`
- `None`: a special value indicating no value or null-like state

Example:

```python
a = True
b = False
print(type(a))
print(bool(0))
print(bool(None))
```

Python treats many values as false in boolean contexts, including `0`, empty strings, empty tuples, and `None`.

---

## 8th File: Type Checking and Dynamic Typing

File: `8thtest.py`

This file focuses on `type()` and dynamic typing in Python.

Important ideas:
- `type(value)` returns the type of a value
- variables can be reassigned to a different type later
- Python is dynamically typed

Example:

```python
x = 10
x = "Hi Everyone!"
print(type(x))
```

This shows that a variable is not permanently locked to one data type.

---

## TypeConversion.py: Converting Between Data Types

File: `TypeConversion.py`

This file explains how to convert values using built-in functions such as:

- `int()`
- `float()`
- `str()`

Example:

```python
a = int(2.2)    # 2
b = float(1)    # 1.0
c = str(3.3)    # "3.3"
```

Type conversion is useful when combining values, formatting output, or preparing data for calculations and storage.

---

## Variables Example File

File: `Variables/Examples.py`

This file demonstrates the basic concept of variables in Python, including:

- variable creation
- deleting variables
- checking variable type
- type casting
- case sensitivity
- multiple assignment
- local and global scope examples

This file gives a practical view of how variables work in real Python scripts.

---

## Overall Summary

The project covers the most important built-in Python data types:

- numeric: `int`, `float`, `complex`, `bool`
- text: `str`
- ordered collections: `list`, `tuple`, `range`
- mapping: `dict`
- unique collection: `set`
- special values: `None`
- binary data: `bytes`, `bytearray`, `memoryview`

These types form the foundation of Python programming and are essential before learning conditions, loops, functions, and more advanced topics.

---

## Final Idea

In Python, every value has a type, and understanding that type helps us choose the right operations, avoid errors, and write cleaner code.
