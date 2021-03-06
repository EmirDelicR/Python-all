# Python-all

## content

- [Intro](#intro) <br/>
- [Basic Concepts](#basic) <br/>
- [Control Structures](#control) <br/>
- [Types in Python](#types) <br/>
- [OOP/Classes](#oop) <br/>
- [Modules in Python](#modules)<br/>
- [Exception Handling](#exception) <br/>
- [Regular Expressions](#regex)<br/>
- [JSON in Python](#json)<br/>
- [URLLIB module](#url)<br/>
- [Dates/Time in Python](#date)<br/>
- [Working with files](#files)<br/>
- [Trace and improve functions](#trace)
- [Desktop app with Tkinter](#desktop)<br/>
- [Django with REST](#django)
  - [URLs](#urls)
  - [Create view](#view)
  - [View documentation](#view-docs)
  - [Run migrations](#migrations)
  - [Create superuser](#superuser)
  - [Store and install requirements](#requirements)
  - [Add dependency](#dependency)
  - [Run server](#server)
  - [Add models](#models)
  - [Set up PostGres DB](#db)
  - [Create new migrations](#migrate)
  - [Terminal](#terminal)
  - [Serializers](#serializer)
  - [Api endpoint](#endpoint)
  - [Testing app](#testing)
  - [Create decorators](#decorators)
  - [Create custom tasks](#tasks)
  - [Update app settings](#settings)
  - [Sentry](#sentry)
  - [Custom settings](#setting)
  - [Swagger](#swagger)
  - [Some useful functions](#functions)
- [Client setup](#client)
- [Links](#links)
- [Tips](#tips)

## intro

[Awesome-Python-Git](https://github.com/vinta/awesome-python)

[Awesome-Django-Git](https://github.com/shahraizali/awesome-django)

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

Install PIP and Selenium

```console
$ sudo apt-get install python3-pip
# Use:
$ pip3 -V

$ pip3 install selenium
```

Open python documentation from terminal

```console
$ python -m pydoc <name of module (math)>
$ python -m pydoc <name of type (tuple)>
$ python -m pydoc <name of function (pow)>

# search module or keyword
$ python -m pydoc -k <pattern (ftp)>

# Open pydoc on server
$ sudo python -m pydoc -p <Port number>
$ sudo python -m pydoc -g
```

Install PyCharm

```console
sudo snap install pycharm-community --classic
```

Virtual ENV

[VE](https://docs.python.org/3/tutorial/venv.html)

```console
$ sudo apt-get install python3-venv
$ python3 -m venv <name>

# activate virtual env
$ source <name>/bin/activate

# Install django
$ cd <name>
$ pip install django

# deactivate virtual env
$ deactivate

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

/* Formating string */
>> some_date = [2, 12, 2018]
>> print("Date: {0}/{1}/{2}".format(some_date[0], some_date[1], some_date[2]))
>> Output: Date: 2/12/2018

>> print("{x}/{y}".format(x=100, y=10))
>> Output: 100/10

/* Check if sting start with some word */
>> text = "Start the ..."
>> print(text.startswith("Start"))
>> Output: True
>> print(text.endswith("..."))
>> Output: True
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

#### Lambdas

A lambda function is a small anonymous function.

**lambda arguments : expression**

```python
x = lambda a : a + 10
print(x(5))
# 15

x = lambda a, b : a * b
print(x(5, 6))
# 30

print((lambda x: x**2)(3))
# 9

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
# OR
print(some_list[::-1])

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

# Remove duplicates from list
some_list = ["test", "test1", "test2", "test"]

no_duplicates = list(set(some_list))
print(no_duplicates)

# List slicing
some_list = [1, 2, 3, 4, 5, 6, 7]
print(some_list[2:6])
# [3, 4, 5, 6]

print(some_list[:3])
# [1, 2, 3]

print(some_list[3:])
# [4, 5, 6, 7]

print(some_list[1:6:2])
# [2, 4, 6]

# List comprehensions
some_list = [x**2 for x in range(5)]
print(some_list)
# [0, 1, 4, 9, 16]

some_list = [x**2 for x in range(5) if x**2 % 2 == 0]
print(some_list)
# [0, 4, 16]

# Join is string function to use with list (Must only have strings)
some_date = ["A", "B", "C"]
print("/".join(some_date))
# A/B/C

# Map:
new_list = [1, 2, 3, 4, 5]
double_list = list(map(lambda x: x*2, new_list))
print(double_list)
# [2, 4, 6, 8, 10]

# Filters
new_list = [1, 2, 3, 4, 5]
double_list = list(filter(lambda x: x % 2 == 0, new_list))
print(double_list)
# [2, 4]

# Generators
# Generate list of random words
import random
import string


def random_word(word_length, element_length):
    letters = string.ascii_lowercase
    for i in range(element_length):
        yield ''.join(random.choice(letters) for i in range(word_length))


print(list(random_word(4, 5)))
# ['dtki', 'lazt', 'ioxf', 'ysfa', 'ztpq']

```

#### Tuples

Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

[Tuples methods](https://www.w3schools.com/python/python_ref_tuple.asp)

```pyhton
some_tuple = ("apple", "banana", "cherry")
print(some_tuple)

print(some_tuple[1])
```

#### Sets

Set is a collection which is unordered and unindexed. No duplicate members.

[Sets methods](https://www.w3schools.com/python/python_ref_set.asp)

```pyhton
some_set = {"apple", "banana", "cherry"}
print(some_set)
# {'cherry', 'apple', 'banana'}

some_set.add("orange")
print(some_set)
# {'cherry', 'apple', 'orange', 'banana'}

some_set.update(["orange", "mango", "grapes"])
print(some_set)
# {'apple', 'mango', 'grapes', 'cherry', 'banana', 'orange'}
```

#### Dictionaries

Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

[Dictionaries methods](https://www.w3schools.com/python/python_ref_dictionary.asp)

```pyhton
some_dictionary =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(some_dictionary)
print(some_dictionary["model"])


for x in some_dictionary.values():
    print(x)
# Ford Mustang 1964


for x, y in some_dictionary.items():
    print(x, y)

# brand Ford model Mustang year 1964

# Check if key exist
if "model" in thisdict:

```

[TOP](#content)

## oop

[Classes-documentation](https://docs.python.org/3/tutorial/classes.html)

#### Class

```python
class Person:

    # Initial object
    def __init__(self, name, text):
        self.name = name
        self.text = text

    def __getitem__(self, name):
        return getattr(self, name)

    def __setitem__(self, name, value):
        return setattr(self, name, value)

    def __delitem__(self, name):
        return delattr(self, name)

    def __contains__(self, name):
        return hasattr(self, name)

    def __add__(self, num):
        return "Sum of {0} and {1} is {2}".format(num[0], num[1], num[0] + num[1])

    def print_data(self):
        print("My name is {0} and text is {1}".format(self.name, self.text))


person = Person('Emir', 'This is text')

print("Name: " + person["name"])
# Name: Emir

print("Text: " + person["text"])
# Text: This is text

person['name'] = 'Emir Delic';
print("Item name: " + person["name"])
# Item name: Emir Delic

person.print_data()
# My name is Emir Delic and text is This is text

print("Contains key text: {0}".format('text' in person))
# Contains key text: True
del(person["text"])
print("Contains key text: {0}".format('text' in person))
# Contains key text: False

# Operator overloading (__add__ and all different function)
# is to change the behavior of operator

print(person + [2, 3])

```

#### Inheritance

```python
class Student(Person):

    def __init__(self, obj):
        self.grades = obj
        # call constructor of super class
        super().__init__()


grades = {'Math': '5', 'Bio': '4'}
student = Student(grades)
print(student['grades'])
# {'Math': '5', 'Bio': '4'}
```

#### Private in class

```python
class SomeClass:
    ## Just append __ before variable
    __hidden_variable = 0

```

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

[Errors and Exceptions](https://docs.python.org/3.7/tutorial/errors.html)

```pyhton
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

# Output:
# "Something went wrong"
# "The 'try except' is finished"

try:
  print(10/0)
except ZeroDivisionError as err:
    print("Zero error: {0}".format(err))
finally:
  print("The 'try except' is finished")

# Zero error: division by zero
# The 'try except' is finished

# Look file-reader for example

# manually rise exception
raise Exception('This is the error message.')
```

[TOP](#content)

## regex

[Regex-documentation](https://docs.python.org/3.7/library/re.html)

```pyhton
import re

pattern = r"eggs"

# Must start with pattern
if re.match(pattern, "eggs eggs test"):
    print('Match found')
else:
    print('Match Not found')

# can be anywhere in string
if re.search(pattern, "eggs eggs test"):
    print('Match found')
else:
    print('Match Not found')

print(re.findall(pattern, "eggs eggs test"))
# ['eggs', 'eggs']

text = "My name is Emir, Hi Emir"
# . can replac any string exc(\n)
print(re.findall(r"E..r", text))
# ['Emir', 'Emir']

# ^ - means start of string and $ - is end of string
```

[TOP](#content)

## json

[JSON Documentation](https://docs.python.org/3.7/library/json.html)

```python
import json

# some string:
text = '{ "name":"John", "age":30, "city":"New York"}'
print("Type of variable text is: {0}".format(type(text)))
# parse text to JSON:
json_data = json.loads(text)
print(json_data)
print("Type of variable json_data is: {0}".format(type(json_data)))

# Convert back to string
json_dumps = json.dumps(json_data)
print(json_dumps)
print("Type of variable json_data is: {0}".format(type(json_dumps)))

# Print in nice way
print("Formatted json: ")
print(json.dumps(json_data, sort_keys=True, indent=4))


with open('test.json') as data_file:
    print("Type of variable data_file is: {0}".format(type(data_file)))
    data = json.load(data_file)

print("Type of variable data is: {0}".format(type(data)))
print(data)

```

test.json

```json
{
  "maps": [
    {
      "id": "blabla",
      "iscategorical": "0"
    },
    {
      "id": "blabla",
      "iscategorical": "0"
    }
  ],
  "masks": {
    "id": "valore"
  },
  "om_points": "value",
  "parameters": {
    "id": "valore"
  }
}
```

[TOP](#content)

## url

```python
# https://www.youtube.com/watch?v=LosIGgon_KM&index=2&list=LLXTQOhCUnflnafxq6fz73iQ

# Protocol: https, http, ftp ...

# Host: www.youtube.com

# Path: /watch

# Querystring: v=LosIGgon_KM&index=2&list=LLXTQOhCUnflnafxq6fz73iQ

# Fragment: comes after # - to navigate through single page

# python -m pydoc urllib

# contains

# request: open URLs
# response: (used internally)
# error: request exceptions
# parse: useful URL functions

# in console run python3
# import urllib
# dir(urllib)

```

[TOP](#content)

## date

[DateTime Documentation](https://docs.python.org/3.7/library/datetime.html)

[DateTime w3School](https://www.w3schools.com/python/python_datetime.asp)

```python
import datetime

x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))
```

#### Scheduling Tasks

```python
from datetime import datetime, timedelta
from threading import Timer

def calculate_schedule_time(time_to_schedule_in={'days':1, 'hours':0, 'minutes':0, 'seconds':0 }):
  current_date=datetime.now()

  delta = timedelta(
    days=time_to_schedule_in['days'],
    hours=time_to_schedule_in['hours'],
    minutes=time_to_schedule_in['minutes'],
    seconds=time_to_schedule_in['seconds'],
    microseconds=0,
  )

  to_execute_date = current_date + delta
  delta_t=to_execute_date-current_date

  print('Timer set in: ', delta_t)
  total_in_seconds=delta_t.total_seconds()

  return total_in_seconds

def schedule(time_in_secs, calback):
  t = Timer(time_in_secs, calback)
  t.start()

def hello_world():
    print("hello world")
    #...

time_to_schedule={'days':0, 'hours':0, 'minutes':0, 'seconds':30 }
timer = calculate_schedule_time(time_to_schedule)
schedule(timer, hello_world)
```

[TOP](#content)

## files

```python
    create_path = os.path.join('usr', 'bin', 'spam') # usr/bin/spam

    print(os.path.abspath(path))

    print(os.path.basename(path)) # spam
    print(os.path.dirname(path)) # usr/bin
    print(os.path.split(path)) # returns tuple ('usr/bin', 'spam')
    print(path.split(os.path.sep)) # ['usr', 'bin', 'spam'] # os.path.sep = /


    cwd = os.getcwd() # current working directory
    os.chdir('C:/Data/Test')
    cwd = os.getcwd() # C:/Data/Test
    os.makedirs('C:/delicious/walnut/waffles')

    # set permissions on file
    import stat
    os.chmod(
        'waffles',
        stat.S_IRUSR |
        stat.S_IWUSR |
        stat.S_IRGRP |
        stat.S_IWGRP |
        stat.S_IROTH
    )

    os.getsize('C:/delicious/walnut/waffles.txt')
    os.listdir(cwd) # return array of directories

    os.path.exists(path) # return True or False # isdir, isfile

    # Read file
    with open(main, 'a+') as some_file: # r- read, w- write, a- append
        content_of_file = some_file.read()
        some_file.write('Text')
        print(content)

        # ctx = some_file.readlines() # return array of lines with \n
        # print(ctx)
        # for line in some_file: # can use loop also
        #  print(line)


    # r -   Opens a file for reading only. The file pointer is placed at
    #       the beginning of the file. This is the default mode.
    # rb -  Opens a file for reading only in binary format. The file
    #       pointer is placed at the beginning of the file. This is the default mode.
    # r+ -  Opens a file for both reading and writing. The file pointer will be at
    #       the beginning of the file.
    # rb+ - Opens a file for both reading and writing in binary format. The file pointer
    #       will be at the beginning of the file.
    # w -   Opens a file for writing only. Overwrites the file if the file exists. If the
    #       file does not exist, creates a new file for writing.
    # wb -  Opens a file for writing only in binary format. Overwrites the file if the file
    #       exists. If the file does not exist, creates a new file for writing.
    # w+ -  Opens a file for both writing and reading. Overwrites the existing file if the
    #       file exists. If the file does not exist, creates a new file for reading and writing.
    # wb+ - Opens a file for both writing and reading in binary format. Overwrites the existing
    #       file if the file exists. If the file does not exist, creates a new file for reading and writing.
    # a -   Opens a file for appending. The file pointer is at the end of the file if the file exists.
    #       That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
    # ab -  Opens a file for appending in binary format. The file pointer is at the end of the file
    #       if the file exists. That is, the file is in the append mode. If the file does not exist,
    #       it creates a new file for writing.
    # a+ -  Opens a file for both appending and reading. The file pointer is at the end of the file
    #       if the file exists. The file opens in the append mode. If the file does not exist,
    #       it creates a new file for reading and writing.
    # ab+ - Opens a file for both appending and reading in binary format. The file pointer is at the
    #       end of the file if the file exists. The file opens in the append mode. If the file does
    #       not exist, it creates a new file for reading and writing.

    # To store variables into file and not plain text use shelve module

    import shelve
    shelfFile = shelve.open('fileName')
    cats = ['Zophie', 'Pooka', 'Simon']
    shelfFile['cats'] = cats
    shelfFile.close()

    shelfFile = shelve.open('fileName')
    type(shelfFile) # <class 'shelve.DbfilenameShelf'>
    shelfFile['cats'] # ['Zophie', 'Pooka', 'Simon']
    shelfFile.close()

    shelfFile = shelve.open('fileName')
    list(shelfFile.keys()) # ['cats']
    list(shelfFile.values()) # [['Zophie', 'Pooka', 'Simon']]
    shelfFile.close()
```

#### Organizing Files

The **_shutil_** module provides functions for copying files, as well as entire folders.

```python
import shutil, os

# copy single file
shutil.copy('C:/spam.txt', 'C:/delicious') # 'C:/delicious/spam.txt'
shutil.copy('eggs.txt', 'C:/delicious/eggs2.txt') # 'C:/delicious/eggs2.txt'

# copy all in folder
shutil.copytree('C:/bacon', 'C:/bacon_backup') # (from, to)

# move folder/rename
shutil.move('C:/bacon.txt', 'C:/eggs') # 'C:/eggs/bacon.txt'

# delete file
os.unlink(path)  # Calling os.unlink(path) will delete the file at path.

os.rmdir(path) # Calling os.rmdir(path) will delete the folder at path. This folder must be empty of any files or folders.

shutil.rmtree(path) # Calling shutil.rmtree(path) will remove the folder at path, and all files and folders it contains will also be deleted.

for filename in os.listdir():
    if filename.endswith('.txt'):
        #os.unlink(filename)
        print(filename)


# A much better way to delete files and folders is with the third-party send2trash module.
pip install send2trash

# check folder tree
for folderName, subfolders, filenames in os.walk(path):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

    print('')

```

#### ZIP

```python
import zipfile, os

os.chdir('C:/') # move to the folder with example.zip
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.namelist() # .zip file content ['spam.txt', 'cats/', 'cats/catnames.txt', 'cats/zophie.jpg']
spamInfo = exampleZip.getinfo('spam.txt')
spamInfo.file_size # 13908
spamInfo.compress_size # 3828

exampleZip.extractall() # extract all files in current directory, you can pass path

exampleZip.extract('spam.txt') # Extract single file in current directory
exampleZip.extract('spam.txt', 'C:/some/new/folders') # Extract to path
exampleZip.close()

# ZIP more files into already exiting ZIP file
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()

```

#### EXCEL

```python
# TODO https://automatetheboringstuff.com/chapter12/
# https://openpyxl.readthedocs.io/en/stable/
# Add docs and small example
```

#### PDF and WORD

```python
# TODO https://automatetheboringstuff.com/chapter13/
# http://www.blog.pythonlibrary.org/2018/06/07/an-intro-to-pypdf2/
```

#### CSV and JSON

```python
# TODO https://automatetheboringstuff.com/chapter14/
```

[TOP](#content)

## trace

```python

def memoize(f):
  cache = {}
  def helper(x):
      if x not in cache:
          cache[x] = f(x)
      return cache[x]
  return helper

def trace(f):
  f.indent = 0
  def helper(x):
      print('|  ' * f.indent + '|--', f.__name__, x)
      f.indent += 1
      value = f(x)
      print('|  ' * f.indent + '|--', 'return', repr(value))
      f.indent -= 1
      return value
  return helper

# this is same as calling trace(fib)
@memoize  # Order of decorators is important (executed first)
@trace # (excecuted second)
def fib(n):
    if n == 0 or n == 1:
      return 1

    return fib(n-1) + fib(n-2)

print(fib(4))
```

[TOP](#content)

## desktop

[Tkinter documentation](https://docs.python.org/3.7/library/tkinter.html)

[Widget list](https://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html)

[Tutorial](https://www.tutorialspoint.com/python/python_gui_programming.htm)

Install tkinter

```console
$ sudo apt-get install python3-tk
```

** Look file Desktop-app **

[TOP](#content)

## django

[Django docks](https://docs.djangoproject.com/en/2.1/intro/tutorial01/)
[Django CDRF](http://www.cdrf.co)

Navigate to folder like (Desktop)

(See django-project folder)

```console
# Instal VE if you dont have
$ sudo apt-get install python3-venv
# Create VE with name of project
$ python3 -m venv <name>

# activate virtual env
$ source <name>/bin/activate

# Install django
$ cd <name>
$ pip install django

# check version
$ python -m django --version

# install django rest framework
$ pip install djangorestframework

# create django project
$ django-admin startproject <name (mysite)>
$ cd <name>

# create django app
# django-admin startapp - command ; app - name of app
$ django-admin startapp app

# folder structure
- mysite (rename this to server)
--- app
--- mysite
--- env

# copy urls folder from mysite to app

# deactivate virtual env
$ deactivate

```

[TOP](#content)

#### urls

**Set up URL**

in mysite/urls

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("app.urls")),
]
```

in app/urls

```python
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from rest_auth.views import LogoutView, PasswordChangeView
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from . import views

router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    path('', views.home, name='home'),
    path('admin/login/', obtain_auth_token),
    path('logout/', csrf_exempt(LogoutView.as_view())),
    path('password/change/', PasswordChangeView.as_view()),
    # To pass id to route
    # path('route/<str:id>', views.SomeView.as_view()),
]
```

**Note - install missing dependency and add simple view**

```console
pip install django-rest-auth
```

[TOP](#content)

#### view

**Create an view**

in app/views.py

```python
def home(req):
    return HttpResponse("<h>This is home page</h>")
```

#### view-docs

**ApiView**

[APIView](https://www.django-rest-framework.org/api-guide/views/)

NOTE: Use this only if the view have GET function

```python
from rest_framework.views import APIView
# in view.py check
class TestApiView(APIView):
```

**Generic views**

[GenericView](https://www.django-rest-framework.org/api-guide/generic-views/)

```python
from rest_framework import generics
# in view.py check
class ListCreateTodoView(generics.ListAPIView):
class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
```

**View Set**

[ViewSet](https://www.django-rest-framework.org/api-guide/viewsets/#viewset)

```python
from rest_framework import viewsets
# in view.py check
class TestModelViewSet(viewsets.ModelViewSet):

# in urls.py
router.register('test-model-view-set/', views.TestModelViewSet)
urlpatterns = router.urls

# To have access to default methods (list, create ...) add line above
| NAME          | METHOD        | CLIENT CALL                |
| ------------- |:-------------:| --------------------------:|
| list          | GET all       | "test-model-view-set/"     |
| create        | POST          | "test-model-view-set/"     |
| retrieve      | GET by ID     | "test-model-view-set/<id>" |
| update        | PUT           | "test-model-view-set/<id>" |
| partial_update| PATCH         | "test-model-view-set/<id>" |
| destroy       | DELETE        | "test-model-view-set/<id>" |

# To create an custom action
@action(detail=True, methods=['post'])
def set_todo(self, request, pk=None):
    return Response(status=status.HTTP_200_OK)

# form client call this URL
# `${baseUrl}test-model-view-set/${todoItem.id}/set_todo/`,

```

```python
# If you have function
def save(self, *args, **kwargs):
# And you call function as
save(1,2,3,4,a=20,b=30,c=40)
# args = (1,2,3,4) # Tuple
# kwargs = {'a':20,'b':30,'c':40} # Dictionary

# *args - list of unnamed arguments
# **kwargs - dictionary (named arguments)

```

[TOP](#content)

#### migrations

**Applying migrations**

```console
python3 manage.py migrate
```

[TOP](#content)

#### superuser

**Create Superuser**

```console
python3 manage.py createsuperuser --email admin@example.com --username admin
```

[TOP](#content)

#### requirements

**Store and install requirements**

```console
$ pip freeze > requirements.txt
```

```console
pip install -r requirements.txt
```

[TOP](#content)

#### dependency

**Add dependency**

in mysite/settings.py

```python
# Application definition

INSTALLED_APPS = [
    'app.apps.AppConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Add this
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'app.apps.AppConfig', # Form step django-admin startapp app
]
```

[TOP](#content)

#### server

**Run server**

```console
# navigate to startproject <name> (mysite)
$ .../mysite$ python3 manage.py runserver
```

go to : http://127.0.0.1:8000/api/

or go to : http://127.0.0.1:8000/admin/

[TOP](#content)

#### models

**Creating models**

[Django-models](https://docs.djangoproject.com/en/2.2/topics/db/models/)

in app/models.py

**_Create an base model look in todo-app/server/api/models_**

```python
class Photo(models.Model):
    name = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
```

**Register model to admin interface**

[Django-admin-site](https://docs.djangoproject.com/en/2.2/ref/contrib/admin/)

in app/admin.py

```python
# Register your models here.
from .models import Photo

# Use decorator to register
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'creator')
    search_fields = ('name')

# Other way to register
# admin.site.register(Photo)
```

```python
# Every model can have function that returns string representation of any object
def __str__(self):
    # f"" is short way to format string
    return f"{self.city}"
```

**Relations in models**

```python
address = models.OneToOneField(
    Address, verbose_name="user address" on_delete=models.SET_NULL, null=True, blank=True, related_name='user'
)
# verbose_name="user address" --> name in Django Admin
# on_delete=models.CASCADE || SET_NULL
# related_name='user' --> How to access from other model address.user

# ForeignKey (ManyToOne) goes on child like `One User Have Multi Todo`
# So put this on Todo model class
user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todo')

# ManyToMany
from django.db import models

class Topping(models.Model):
    # ...
    pass

class Pizza(models.Model):
    # ...
    toppings = models.ManyToManyField(Topping)

# In the above example, toppings is in Pizza (rather than Topping having a pizzas ManyToManyField )
# because it’s more natural to think about a pizza having toppings than a topping being on multiple pizzas.
# The way it’s set up above, the Pizza form would let users select the toppings.
```

**Creating Abstract user**

```python
# in mytodoapp/settings.py
AUTH_USER_MODEL = 'api.User'

# in api/models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    def __str__(self):
        return f"{self.username}"
```

[TOP](#content)

#### db

**_Set up postgres DB_**

pgadmin III

```console
vim /etc/postgresql/10/main/pg_hba.conf


# Database administrative login by Unix domain socket
# TODO: set to trust
local   all             postgres                                trust

# TYPE  DATABASE        USER            ADDRESS                 METHOD
# "local" is for Unix domain socket connections only
local   all             all                                     peer
# IPv4 local connections:
# TODO: set to trust
host    all             all             127.0.0.1/32            trust
# IPv6 local connections:
host    all             all             ::1/128                 md5

service postgresql restart
```



login to

```console
sudo -u postgres psql
```

Create DB

```console
postgres=# CREATE DATABASE dbtest;
```

List all DB

```console
postgres=# \l
```

Create user

```console
postgres=# CREATE USER user WITH PASSWORD 'password';
```

Alter user role

```console
postgers=# ALTER ROLE user SET client_encoding TO 'utf8';
postgers=# ALTER ROLE user SET default_transaction_isolation TO 'read committed';
postgers=# ALTER ROLE user SET timezone TO 'UTC';
postgres=# ALTER USER user CREATEDB;

postgres=# GRANT ALL PRIVILEGES ON DATABASE dbtest TO user;
```

Connect to DB

```console
postgres=# \c testdb
```

List DB content

```console
postgres=# \d
```

List data from table

```console
postgres=# select * from <table-name>;
```

Exit from psql

```console
postgres=# \q;
```

**_Make settings in settings.py file_**

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': OPTIONS['DATABASE_NAME'],
        'USER': '', # User created in upper step
        'PASSWORD': '', # User created in upper step
        'HOST': '',
        'PORT': '',
        'TEST': {
            'NAME': 'test_' + OPTIONS['DATABASE_NAME'],
        },
    }
}
```

Install postgres engine

```console
pip install psycopg2-binary
```

If necessery

```console
pip install psycopg2
```

#### migrate

**Make and run new migration**

Run command in terminal

```console
# mysite$ is an folder
mysite$ python3 MY_ENV="DEVELOP" manage.py makemigrations app
# Output: app/migrations/0001_initial.py

# Run migration
mysite$ MY_ENV="DEVELOP" python3 manage.py migrate
```

[TOP](#content)

#### terminal

**Adding data from terminal**

```console
# mysite$ is an folder
mysite$ python manage.py shell

>>> from app.models import Photo

>>> Photo.objects.all()
>>> photo = Photo()
>>> photo.name = "Test"
>>> ... add rest
>>> photo.save()
>>> photo.name
>>> Output: 'Test'
```

**Calling function from terminal**

```python
# in utils.py create function
def test_command(arg_1, arg_2):
    print("This is {} , and this is {}".format(arg_1, arg_2))
```

```console
# mysite$ is an folder
mysite$ python manage.py shell

>>> from app.utils import test_command
>>> test_command('X', 'Y')
```

[TOP](#content)

#### serializer

**Creating serializer for model**

[Django-serializers](https://docs.djangoproject.com/en/2.2/topics/serialization/)

[Rest-Framework-serializers](https://www.django-rest-framework.org/api-guide/serializers/#serializers)

in app/models.py

**_Create an file app/serializers.py_**

```python
from rest_framework import serializers
from .models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ("name", "creator", "price")
```

Some feature with serilizer

```python
# in view add
class TestSerializerView(viewsets.ModelViewSet):
    # Adding ModelViewSet you get automaticly update, create, partial_update ect.
    # Now you can overwrite this function in serilizer

# Register route in urls.py
router.register('test-serializer', views.TestSerializerView)

# Create serilizer

class AddressSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Address.objects.create(**validated_data)
```

[TOP](#content)

#### endpoint

**Creating view for this endpoint**

[rest-generic-view](https://www.django-rest-framework.org/api-guide/generic-views/)

```python
from rest_framework import generics
from .models import Photo
from .serializers import PhotoSerializer

class ListPhotoView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
```

**Add route to urls.py**

```python
urlpatterns += [
  path('photos/', views.ListTodoView.as_view(), name="photos-all")
]
```

[TOP](#content)

#### testing

**Testing App**

Look server/api/tests.py file

```console
python3 manage.py test
```

[TOP](#content)

#### decorators

**Create decorators**

Create decorators.py file

```python
from rest_framework.response import Response
from rest_framework.views import status

def validate_request_data(fn):
    def decorated(*args, **kwargs):
        name = args[0].request.data.get("name", "")
        creator = args[0].request.data.get("creator", "")
        price = args[0].request.data.get("price", "")
        if not name and not creator and not price:
            return Response(
                data={
                    "message": "All fields for photo are necessary"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return fn(*args, **kwargs)
    return decorated
```

[TOP](#content)

#### tasks

**Create custom tasks**

Create management/commands/test.py file

```python
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print("Execute helper function from commands")
```

To execute (! how you call file you need to call here)

```console
python3 manage.py test
```

[TOP](#content)

#### settings

**Customize settings in main app**

**_Set Environment on app_**

```python
# in mysite/settings.py
MY_ENV = os.environ.get('MY_ENV')

if MY_ENV == 'DEVELOP' or MY_ENV == 'LOCAL':
    OPTIONS = {
        'DEBUG': True,
        'DATABASE_NAME': 'Some Db Name',
        'LOGPATH': '/var/log/log-file-name/',
    }
elif MY_ENV == 'PRODUCTION':
    OPTIONS = {
        'DEBUG': False,
        'DATABASE_NAME': 'rlb_essensmarken_production',
        'LOGPATH': '/var/log/rlb_essensmarken_production/',
    }
else:
    raise ValueError('Environment variable "MY_ENV" must be defined to be either DEVELOP or PRODUCTION. Current value: ' + str(MY_ENV))
```

```console
MY_ENV='DEVELOP' python3 manage.py runserver
```

Can pass multi arguments

```console
DEBUG_MODE=xxx API_SECRET=yyy python manage.py runserver
```

[TOP](#content)

#### sentry

**_Set Sentry on app_**

[Sentry-docks](https://docs.sentry.io/platforms/python/)

[Set-logger-with-sentry](https://lincolnloop.com/blog/django-logging-right-way/)

Sign in to Sentry

```console
pip install --upgrade sentry-sdk
```

```python
import sentry_sdk
from sentry_sdk import configure_scope
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="DNS_KEY",
    integrations=[DjangoIntegration()],
    environment=MY_ENV.lower()
)

with configure_scope() as scope:
    scope.set_tag("API_VERSION", "SOME_API_VERSION")
```

[TOP](#content)

#### setting

**_Set rest of the settings_**

```python
DEBUG = OPTIONS['DEBUG']
ALLOWED_HOSTS = ['*']
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Create other paths
MEDIA_ROOT = os.path.join('/data/media', 'file_name')
MEDIA_URL = '/media/'

MEDIA_PUBLIC_ROOT = os.path.join(MEDIA_ROOT, 'public')
```

**_Set rest_framework in the settings_**

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
    	# 'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
    	'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```

[TOP](#content)

#### swagger

**_Set Swagger REST API documentation_**

[Swagger-docs](https://github.com/axnsan12/drf-yasg#installation)

```console
pip install -U drf-yasg
```

```python
# in settings.py
INSTALLED_APPS = [
   ...
   'drf_yasg',
   ...
]

# in urls.py
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="",
      contact=openapi.Contact(email=""),
      license=openapi.License(name=""),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

# Swagger documentation
path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
```

[TOP](#content)

#### functions

**_Some useful functions_**

```python
from django.db import connection

def print_sql_queries():
	indentation = 2
	print("%s\033[33mThe number of SQL Queries is: %s \n" % (" " * indentation, len(connection.queries)))

	if len(connection.queries) > 0:
		width = 240
		total_time = 0.0
		for query in connection.queries:
			nice_sql = query['sql'].replace('"', '').replace(',', ', ')
			sql = "\033[33mTime: \033[31m [%s]\n \033[33m Query: \033[34m%s" % (query['time'], nice_sql)
			total_time = total_time + float(query['time'])
			while len(sql) > width - indentation:
				print("%s%s" % (" " * indentation, sql[:width - indentation]))
				sql = sql[width - indentation:]
			print("%s%s\n" % (" " * indentation, sql))
		replace_tuple = (" " * indentation, str(total_time))
		print("%s\033[1;32m[TOTAL TIME: %s seconds]\033[0m" % replace_tuple)

# To use:
from app.utils import print_sql_queries
print_sql_queries()
```

[TOP](#content)

## client

Create an client side app

```console
# mysite$ is an folder
mysite$ vue create client

mysite$ cd client

mysite$/client/ npm run serve
```

Set cors on server

```console
pip install django-cors-headers
```

```python
# in settings.py

from corsheaders.defaults import default_headers

INSTALLED_APPS = [
    ...
    'corsheaders'
]

# NOTE - Must be before 'django.middleware.common.CommonMiddleware',
MIDDLEWARE = [
    ...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
]

CORS_ORIGIN_ALLOW_ALL = OPTIONS['CORS_ALLOWED'] # True or False

# If Up is True this will be ignored

CORS_ORIGIN_WHITELIST = [
    'http://localhost:8080',
]

# Need for Chrome

CORS_ALLOW_HEADERS = list(default_headers) + [
    'access-control-allow-origin',
]
```

## links

[extend-tutorial](https://sunscrapers.com/blog/ultimate-tutorial-django-rest-framework-part-1/)

[tutorial](https://medium.com/backticks-tildes/lets-build-an-api-with-django-rest-framework-32fcf40231e5)

[best-practice](https://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api)

[heroku-publish](https://rapidapi.com/blog/python-django-rest-api-tutorial/)

[sql-queries-django](https://docs.djangoproject.com/en/2.2/topics/db/queries/)

[TOP](#content)

## tips

Multi assignment

```python
>>> x = y = z = 2
>>> x, y, z
(2, 2, 2)
```

```python
>>> x, y, z = 2, 4, 8
>>> x
2
>>> y
4
>>> z
8
```

```python
>>> x, *y, z = 2, 4, 8, 16
>>> x
2
>>> y
[4, 8]
>>> z
16
```

Merge Dictionaries

```python
>>> x = {'u': 1}
>>> y = {'v': 2}
>>> z = {**x, **y, 'w': 4}
>>> z
{'u': 1, 'v': 2, 'w': 4}

```

Iterations

```python
>>> for i, item in enumerate(['u', 'v', 'w']):
... print('index:', i, 'element:', item)
...
index: 0 element: u
index: 1 element: v
index: 2 element: w

```

Reversed Iteration

```python
>>> for item in reversed(['u', 'v', 'w']):
... print(item)
...
w
v
u

```

Aggregate Elements

```python
>>> x = [1, 2, 4]
>>> y = ('u', 'v', 'w')
>>> z = zip(x, y)
>>> z

>>> list(z)
[(1, 'u'), (2, 'v'), (4, 'w')]

```

Transpose Matrices

```python
>>> x = [(1, 2, 4), ('u', 'v', 'w')]
>>> y = zip(*x)
>>> z = list(y)
>>> z
[(1, 'u'), (2, 'v'), (4, 'w')]

```

Unique Values

```python
>>> x = [1, 2, 1, 4, 8]
>>> y = set(x)
>>> y
{8, 1, 2, 4}
>>> z = list(y)
>>> z
[8, 1, 2, 4]

```

Sort Sequences

```python
>>> x = (1, 'v')
>>> y = (4, 'u')
>>> z = (2, 'w')
>>> sorted([x, y, z])
[(1, 'v'), (2, 'w'), (4, 'u')]

# OR SORT ON SECOND ELEMENT
>>> sorted([x, y, z], key=lambda item: item[1])
[(4, 'u'), (1, 'v'), (2, 'w')]

# REVERSED
>>> sorted([x, y, z], key=lambda item: item[1], reverse=True)
[(2, 'w'), (1, 'v'), (4, 'u')]

# SORT DICTIONARIES (KEYS)
>>> x = {'u': 4, 'w': 2, 'v': 1}
>>> sorted(x.items())
[('u', 4), ('v', 1), ('w', 2)]

# SORT DICTIONARIES (VALUES)
>>> sorted(x.items(), key=lambda item: item[1])
[('v', 1), ('w', 2), ('u', 4)]
>>> sorted(x.items(), key=lambda item: item[1], reverse=True)
[('u', 4), ('w', 2), ('v', 1)]
```

Anagrams

```python
from collections import Counter

def anagram(first, second):
    return Counter(first) == Counter(second)


anagram("abcd3", "3acdb") # True
```

Memory

```python
import sys

variable = 30
print(sys.getsizeof(variable)) # 24
```

Byte Size

```python
def byte_size(string):
    return(len(string.encode('utf-8')))

byte_size('😀') # 4
byte_size('Hello World')
```

Capitalize first letters

```python
s = "programming is awesome"

print(s.title())
```

Chunk

This method chunks a list into smaller lists of a specified size.

```python
def chunk(list, size):
    return [list[i:i+size] for i in range(0,len(list), size)]
```

Compact

This method removes falsy values (False, None, 0 and “”) from a list by using filter().

```python
def compact(lst):
    return list(filter(None, lst))

compact([0, 1, False, 2, '', 3, 'a', 's', 34]) # [ 1, 2, 3, 'a', 's', 34 ]
```

Get vowels

```python
def get_vowels(string):
    return [each for each in string if each in 'aeiou']

get_vowels('foobar') # ['o', 'o', 'a']
get_vowels('gym') # []
```

Decapitalize

```python
def decapitalize(str):
    return str[:1].lower() + str[1:]

decapitalize('FooBar') # 'fooBar'
decapitalize('FooBar') # 'fooBar'
```

Flatten

The following methods flatten a potentially deep list using recursion.

```python
def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret

def deep_flatten(xs):
    flat_list = []
    [flat_list.extend(deep_flatten(x)) for x in xs] if isinstance(xs, list) else flat_list.append(xs)
    return flat_list

deep_flatten([1, [2], [[3], 4], 5]) # [1,2,3,4,5]
```

Difference

This method finds the difference between two iterables by keeping only the values that are in the first one.

```python
def difference(a, b):
    set_a = set(a)
    set_b = set(b)
    comparison = set_a.difference(set_b)
    return list(comparison)


difference([1,2,3], [1,2,4]) # [3]
```

Difference by

The following method returns the difference between two lists after applying a given function to each element of both lists.

```python
def difference_by(a, b, fn):
    b = set(map(fn, b))
    return [item for item in a if fn(item) not in b]


from math import floor
difference_by([2.1, 1.2], [2.3, 3.4], floor) # [1.2]
difference_by([{ 'x': 2 }, { 'x': 1 }], [{ 'x': 1 }], lambda v : v['x']) # [ { x: 2 } ]
```

Calculator without if-else

```python
import operator
action = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul,
    "**": pow
}
print(action['-'](50, 25)) # 25
```

[TOP](#content)

