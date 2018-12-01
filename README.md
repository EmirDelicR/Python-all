# Python-all

## content

[Intro](#intro) <br/>
[Basic Concepts](#basic) <br/>
[Control Structures](#control) <br/>

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

## basic

Print:

```console
>> print('Hello')
```

Division:

```console
>> 100/25
>> Output: 4.0
>> 100//25
>> Output: 4
```

Math operation:

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

Strings:

```console
>> 'He\'s'
>> Output: "He's"
>> "He's"
>> Output: "He's"
```

Accepting input:

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

In place operators:

```console
>> a=10
>> a+=1
>> a
>> Output: 11
/* Apply this to all operators (*, -, //, / ...) */
```

[TOP](#content) <br/>

## control