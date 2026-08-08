# Python Data Types Details

This file summarizes all the Python data type examples from the project, including the later files added: 5th, 6th, 7th, 8th, and TypeConversion.py.

## 1st File: Numeric Types

The first file introduces numeric data types, including:

- int: whole numbers like 10, 20, -5
- float: decimal numbers like 3.14, 2.5
- complex: numbers with real and imaginary parts like 2 + 3j
- bool: Boolean values True and False

This file shows that Python stores values in different categories and that the type() function can tell us which type a value belongs to.

## 2nd File: String Type

The second file focuses on the string data type.

- Strings are written inside quotes.
- They can contain words, sentences, or characters.
- Characters can be accessed by index.
- Strings can be sliced and repeated.

Example:

```python
name = "Python"
print(name[0])
print(name[1:4])
print(name * 2)
```

Strings are used for text processing, input/output, and user messages.

## 3rd File: Sequence Types

The third file introduces sequence data types such as:

- list: ordered and mutable collection
- tuple: ordered and immutable collection
- range: ordered sequence of numbers

These are useful when we want to store multiple values in one variable and access them by index.

## 4th File: Binary Data Types

The fourth file introduces:

- bytes
- bytearray
- memoryview

These are used when working with binary-style data and memory-level representation. They are especially useful for file, network, and low-level data handling.

## 5th File: Dictionary Data Type

The fifth file teaches the dictionary type, which stores data as key-value pairs.

Example:

```python
dict = {}
dict['one'] = "This is One"
dict[2] = "This is Two"

print(dict['one'])
print(dict[2])
```

A dictionary is useful for mapping related values, such as names to numbers or keys to descriptions.

## 6th File: Set Data Type

The sixth file explains the set type.

- A set is an unordered collection of unique values.
- It cannot contain duplicate items.
- It is useful when we need to store unique values only.

Example:

```python
set1 = {123, 199, 89, 98}
set2 = {'Java', 'Python', 'JavaScript'}
print(set1)
print(set2)
```

Sets are commonly used for membership testing and removing duplicate values.

## 7th File: Boolean and None Types

The seventh file introduces:

- bool: True or False
- None: a special null-like value that means “no value”

Boolean values are often used in conditions and comparisons.

Example:

```python
a = True
b = False
print(type(a))
print(bool(0))
print(bool(None))
```

The file also shows that many values in Python are considered False in boolean contexts, such as 0, empty strings, empty tuples, and None.

## 8th File: type() and Dynamic Typing

The eighth file explains how to check the type of a variable or value using type(). It also shows that Python is dynamically typed, which means a variable can change its type during execution.

Example:

```python
x = 10
x = "Hi Everyone!"
print(type(x))
```

This demonstrates that a variable is not locked to one type in Python.

## TypeConversion.py: Converting Values Between Types

This file shows how to convert data from one type to another using functions like:

- int()
- float()
- str()

Examples:

```python
a = int(2.2)      # 2
b = float(1)      # 1.0
c = str(3.3)      # "3.3"
```

Type conversion is very useful when we want to combine values or prepare them for calculations, display, or storage.

## Overall Summary

The project covers the main built-in Python data types:

- numeric values: int, float, complex, bool
- text values: str
- ordered collections: list, tuple, range
- mapping values: dict
- unique collections: set
- special value: None
- binary values: bytes, bytearray, memoryview

These data types are the foundation of Python programming, and understanding them is essential before learning conditions, loops, functions, and more advanced topics.

## Final Idea

In Python, every value has a type, and knowing that type helps us use the correct operations and avoid errors in our programs.
