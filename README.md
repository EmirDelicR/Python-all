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
- [Dates in Python](#date)<br/>
- [Desktop app with Tkinter](#desktop)<br/>
- [Django](#django)
  - [URL](#url)
  - [Create view](#view)
  - [Run migrations](#migrations)
  - [Create superuser](#superuser)
  - [Store and install requirements](#requirements)
  - [Add dependency](#dependency)
  - [Run server](#server)
  - [Add models](#models)
  - [Create new migrations](#migrate)
  - [Terminal](#terminal)
  - [Serializer](#serializer)
  - [Api endpoint](#endpoint)
  - [Testing app](#testing)
  - [Create decorators](#decorators)
  - [Create custom tasks](#tasks)
  - [Update app settings](#settings)
  - [Sentry](#sentry)
  - [Custom settings](#setting)
  - [Swagger](#swagger)
  - [](#)
- [Links](#links)

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

#### url

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

[TOP](#content)

#### migrate

**Make and run new migration**

Run command in terminal

```console
# mysite$ is an folder
mysite$ python3 manage.py makemigrations app
# Output: app/migrations/0001_initial.py

# This will create an table in sql
mysite$ python3 manage.py sqlmigrate app 0001

# Run migration
mysite$ python3 manage.py migrate
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

## links

[extend-tutorial](https://sunscrapers.com/blog/ultimate-tutorial-django-rest-framework-part-1/)

[tutorial](https://medium.com/backticks-tildes/lets-build-an-api-with-django-rest-framework-32fcf40231e5)

[best-practice](https://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api)

[heroku-publish](https://rapidapi.com/blog/python-django-rest-api-tutorial/)
