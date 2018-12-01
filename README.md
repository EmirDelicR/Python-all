# Python-all

## content

[Intro](#intro) <br/>
[Basic Concepts](#basic) <br/>
[Control Structures](#control) <br/>
[Types in Python](#types) <br/>
[Modules in Pyhton](#modules)<br/>
[Exception Handling](#exception) <br/>
[File handling](#file) <br/>

## intro

[Official page](https://www.python.org/)

[PyCharm](https://www.jetbrains.com/pycharm/)

Check python version on linux

```console
$ /usr/bin/python --version
Python 2.7.15rc1
$ /usr/bin/python3 --version
Python 3.6.7
```

Open python console

```console
$ python3
>> print('Hello')
/* Exit the console */
>> exit()
/* To clear console  press CTRL+l */
```

Install PyCharm

```console
sudo snap install pycharm-community --classic
```

[TOP](#content)

## basic

Print:

```console
>> print('Hello')
```

#### Division:

```console
>> 100/25
>> Output: 4.0
>> 100//25
>> Output: 4
```

#### Math operation:

```console
>> 100+25
>> Output: 125

>> 100*25
>> Output: 2500

>> 10**2
>> Output: 100

/* Root */
>> 4**(1/2)
>> Output: 2.0

>> int(4**(1/2))
>> Output: 2

/* Module */
>> 7%3
>> Output: 1
```

#### Strings:

[String Methods](https://www.w3schools.com/python/python_ref_string.asp)

```console
>> 'He\'s'
>> Output: "He's"
>> "He's"
>> Output: "He's"

>> a = "testing"
>> print(b[2:len(b)])
>> Output: sting

>> a = "   Hello   "
>> print(a.strip())
>> Output: "Hello"

>> a = "Hello"
>> print(len(a))
>> 5

>> print(a.lower())
>> Output: "hello"

>> print(a.upper())
>> Output: "HELLO"

>> print(a.replace("H", "J"))
>> Output: "Jello"

>> print(a.split("e"))
>> Output: ['h', 'llo']

/* Reverse string */
>> txt = "Hello World"[::-1]
>> print(txt)

```

#### Bitwise operators:

```console
The Operators:

x << y
Returns x with the bits shifted to the left by y places
(and new bits on the right-hand-side are zeros).
This is the same as multiplying x by 2**y.

x >> y
Returns x with the bits shifted to the right by y places.
This is the same as //'ing x by 2**y.

x & y
Does a "bitwise and". Each bit of the output is 1 if the
corresponding bit of x AND of y is 1, otherwise it's 0.

x | y
Does a "bitwise or". Each bit of the output is 0 if the
corresponding bit of x AND of y is 0, otherwise it's 1.

~ x
Returns the complement of x - the number you get by
switching each 1 for a 0 and each 0 for a 1.
This is the same as -x - 1.

x ^ y
Does a "bitwise exclusive or". Each bit of the output
is the same as the corresponding bit in x if that
bit in y is 0, and it's the complement of the bit
in x if that bit in y is 1.

Just remember about that infinite series of 1 bits in a negative number, and these should all make sense.
```

#### Logical operators:

- **and**

- **or**

- **not**

Identity and membership operator

- **is** - Returns true if both variables are the same object

- **in** - Returns True if a sequence with the specified value is present in the object

#### Accepting input:

```console
>> input('Enter value: ')
>> Enter value:
>> print('He\n s')
>> He
>>  s

>> value = input('Enter value: ')
>> print('This is your value: ', value)
>> del value
>> print(value) // error
```

#### In place operators:

```console
>> a=10
>> a+=1
>> a
>> Output: 11
/* Apply this to all operators (*, -, //, / ...) */
```

[TOP](#content)

## control

#### If statement:

```python
a = 18
if a > 18:
    print("Greater then 18")
elif a == 18: # != not equal
    print("Equal to 18")
else:
    print("Smaller then 18")
```

#### Range:

```python
numbers = list(range(10))
print(numbers)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers = list(range(3, 10))
print(numbers)
# [3, 4, 5, 6, 7, 8, 9]

numbers = list(range(3, 10, 3))
print(numbers)
# [3, 6, 9]

```

#### Functions:

[Build-in Functions](https://www.w3schools.com/python/python_ref_functions.asp)

```python
def print_name(value = "John Doo"):
    print(value)


def get_name():
    return "Some name"


print_name()
# John Doo

print_name(get_name())
# Some name

```

#### For loop:

```python
total = 0
for num in range(1, 10):
    total += num

print(total)


for num in range(6):
    if num == 3:
        # this will skip this iteration
        continue

    print(num)


for num in range(6):
    if num == 3:
        # this will break loop
        break

```

#### While loop:

```python
i = 1
while i < 6:
  print(i)
  i += 1

# Can use break and continue here also
```

[TOP](#content)

## types

#### Lists:

List is a collection which is ordered and changeable. Allows duplicate members.

[List methods](https://www.w3schools.com/python/python_ref_list.asp)

```python
some_list = ["test", "test1", "test2"]
print("test" in some_list) # Prints true

# Add element to end
some_list.append("test3")

# Length
print(len(some_list))

# Add element to specific position
some_list.insert(2, "Test#")

# Remove element
some_list.remove("Test#")

# Remove last element (can pass index)
some_list.pop()

# Empty list
some_list.clear()

# Copy list
ne_list = some_list.copy()

# Reverse list
some_list.reverse()

# Sort list
some_list.sort()

# Count element in list
fruits = ['apple', 'banana', 'cherry', 'cherry']
x = fruits.count("cherry") # x is 2

# Extend list with some new list
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
# ['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo']

# Index of element
print(some_list.index("Test#"))
```

#### Tuples

Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

[Tuples methods](https://www.w3schools.com/python/python_ref_tuple.asp)

#### Sets

Set is a collection which is unordered and unindexed. No duplicate members.

[Sets methods](https://www.w3schools.com/python/python_ref_set.asp)

#### Dictionaries

Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

[Dictionaries methods](https://www.w3schools.com/python/python_ref_dictionary.asp)

[TOP](#content)

## modules

[List of build-in modules](https://docs.python.org/3/py-modindex.html)

```python
# my_module.py
def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

# some_file.py
import my_module
my_module.greeting("Jonathan")
my_module.person1["age"]

# OR
import my_module as mx
mx.person1["age"]

# OR
from my_module import person1
person1["age"]


# List all modules (need to import)
help('modules')

# Print all existing build in modules
print(dir(__builtins__))

```

[TOP](#content)

## exception

[TOP](#content)

## file

[TOP](#content)
