# https://automatetheboringstuff.com/chapter7/
import pprint
import os

#################################################################################################################################
''' Working with list and nested lists '''
def reverse_matrix(): 
    grid = [['.', '.', '.', '.', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]

    ''' 
        ..OO.OO..
        .OOOOOOO.
        .OOOOOOO.
        ..OOOOO..
        ...OOO...
        ....O.... 
    '''        

    new_grid = [ [] for _ in range(len(grid[0]))]
    for i, item in enumerate(grid):
      # print(item)
      for j, elem in enumerate(item):
        new_grid[j].append(elem)
        
    for i, item in enumerate(new_grid):
      print(item)    

#################################################################################################################################
''' Working with dictionary's keys(), values(), and items() '''
def dict_test():
    spam = {'color': 'red', 'age': 42}
    
    for v in spam.values():
        print(v) # red 42

    for k in spam.keys():
        print(k) # color age

    for i in spam.items():
        print(i) # ('color', 'red') ('age', 42)

    # Insted of checking if key is inside of dict use .get()   
    # get() method that takes two arguments: the key of the value to 
    # retrieve and a fallback value to return if that key does not exist.
    print(spam.get('color', 'blue')) # red
    print(spam.get('colors', 'all is blue')) # all is blue

def count_lethers():
    message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
    count = {}

    for character in message:
        count.setdefault(character, 0)
        count[character] = count[character] + 1

    pprint.pprint(count)


stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory".center(40, '='))
    item_total = 0
    for k, v in inventory.items():
      print(v, k)
      item_total += v
 
    print("Total number of items: " + str(item_total))

displayInventory(stuff)


def addToInventory(inventory, addedItems):
    for item in addedItems:
      inventory.setdefault(item, 0)
      inventory[item] += 1

    return inventory   

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(stuff, dragonLoot)
displayInventory(inv)

#################################################################################################################################        
''' String manipulation '''
def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
        
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 20, 6)

#################################################################################################################################
tableData = [
  ['apples', 'oranges', 'cherries', 'banana'],
  ['Alice', 'Bob', 'Carol', 'David'],
  ['dogs', 'cats', 'moose', 'goose']
]

def printTable(data):
  colWidths = [0] * len(data)

  for i, item in enumerate(data):
    for val in item:
      if len(val) > colWidths[i]:
        colWidths[i] = len(val)

  for i, item in enumerate(data):
    for j, val in enumerate(item):
      item[j] = val.rjust(colWidths[i])
      
  zipped = list(zip(*tableData))
  
  for i, item in enumerate(zipped):
    print(' '.join(item))

printTable(tableData)


#################################################################################################################################
''' read/write files '''

def test_file():
    create_path = os.path.join('usr', 'bin', 'spam') # usr/bin/spam

    print(os.path.abspath(path))

    print(os.path.basename(path)) # spam
    print(os.path.dirname(path)) # usr/bin
    print(os.path.split(path)) # returns tuple ('usr/bin', 'spam')
    print(path.split(os.path.sep)) # ['usr', 'bin', 'spam'] # os.path.sep = /


    cwd = os.getcwd() # current working directory
    # os.chdir('C:/Data/Test')
    # cwd = os.getcwd() # C:/Data/Test
    # os.makedirs('C:/delicious/walnut/waffles')

    # set permissions on file    
    # import stat
    # os.chmod(
    #     'waffles',
    #     stat.S_IRUSR |
    #     stat.S_IWUSR |
    #     stat.S_IRGRP |
    #     stat.S_IWGRP |
    #     stat.S_IROTH
    # )

    # os.getsize('C:/delicious/walnut/waffles.txt') 
    os.listdir(cwd) # return array of directories

    os.path.exists(path) # return True or False # isdir, isfile

    # Read file
    with open(main, 'r') as some_file: # r- read, w- write, a- append
        content_of_file = some_file.read()
        print(content)
        
        # ctx = some_file.readlines() # return array of lines with \n
        # print(ctx)
        # for line in some_file: # can use loop also
        #  print(line)


#################################################################################################################################
# Renaming Files
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.

import shutil, os, re

# Create a regex that matches files with the American date format.
datePattern = re.compile(r"""
    ^(.*?)          # all text before the date
    ((0|1)?\d)-     # one or two digits for the month
    ((0|1|2|3)?\d)- # one or two digits for the day
    ((19|20)\d\d)   # four digits for the year (must start with 19 or 20)
    (.*?)$          # all text after the date
    """, re.VERBOSE)

# Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # Skip files without a date.
    if mo == None:
        continue

    # Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart  = mo.group(2)
    dayPart    = mo.group(4)
    yearPart   = mo.group(6)
    afterPart  = mo.group(8)

    # Form the European-style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Rename the files.
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    #shutil.move(amerFilename, euroFilename) # uncomment after testing


#################################################################################################################################
# Backing Up a Folder into a ZIP File
#! python3
# backupToZip.py
# Copies an entire folder and its contents into
# a zip file whose filename increments.

import zipfile, os

def backupToZip(folder):
    # Backup the entire contents of "folder" into a zip file.

    folder = os.path.abspath(folder) # make sure folder is absolute

    # Figure out the filename this code should used based on 
    # what files already exist.
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # Create the zip file.
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        # Add the current folder to the ZIP file.
        backupZip.write(foldername)

        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            if filename.startswith(os.path.basename(folder) + '_') and filename.endswith('.zip'):
                continue # don't backup the backup ZIP files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')


backupToZip('C:/delicious')

#################################################################################################################################
# https://inventwithpython.com/cracking/
#################################################################################################################################
# Simple encryption function
def caesar_chiper(msg='', mode='dec'):
  print('MESSAGE: ', msg)
  
  SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
  key = 13
  translated = ''
  
  for symbol in msg:
    # Note: Only symbols in the SYMBOLS string can be encrypted/decrypted.
    if symbol in SYMBOLS:
      symbolIndex = SYMBOLS.find(symbol)
      # Perform encryption/decryption:
      translatedIndex = symbolIndex - key
      if mode == 'enc':
        translatedIndex = symbolIndex + key

      # Handle wraparound, if needed:
      if translatedIndex >= len(SYMBOLS):
        translatedIndex = translatedIndex - len(SYMBOLS)
      elif translatedIndex < 0:
        translatedIndex = translatedIndex + len(SYMBOLS)
    
      translated = translated + SYMBOLS[translatedIndex]
    else:
      # Append the symbol without encrypting/decrypting:
      translated = translated + symbol

  return translated

text = caesar_chiper(msg='Testing.', mode='enc')
print(text)

#################################################################################################################################
# Brute force caesar_chiper function
def brute_force_caesar_chiper(msg=""):
  SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
  # Loop through every possible key:
  for key in range(len(SYMBOLS)):
    # It is important to set translated to the blank string so that the
    # previous iteration's value for translated is cleared:
    translated = ''
    # The rest of the program is almost the same as the Caesar program:

    # Loop through each symbol in message:
    for symbol in msg:
      if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)
        translatedIndex = symbolIndex - key

        # Handle the wraparound:
        if translatedIndex < 0:
          translatedIndex = translatedIndex + len(SYMBOLS)
        # Append the decrypted symbol:
        translated = translated + SYMBOLS[translatedIndex]
      else:
        # Append the symbol without encrypting/decrypting:
        translated = translated + symbol
    # Display every possible decryption:
    print('Key #%s: %s' % (key, translated))

brute_force_caesar_chiper(msg = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM')

#################################################################################################################################

def encrypt_message(key, message):
  # Each string in ciphertext represents a column in the grid:
  if key < 2 or key > len(message)/2:
    print(f'key is not valid! Must be betwean 2 and {int(len(message)/2)}')
    return 
  ciphertext = [''] * key # ['', '', '', '', '', '', '', '']
  # Loop through each column in ciphertext:
  for column in range(key):
    currentIndex = column
    # Keep looping until currentIndex goes past the message length:
    while currentIndex < len(message):
      # Place the character at currentIndex in message at the
      # end of the current column in the ciphertext list:
      print(column, ' : ', currentIndex)
      ciphertext[column] += message[currentIndex]
      # Move currentIndex over:
      currentIndex += key

  # Convert the ciphertext list into a single string value and return it:
  print(''.join(ciphertext))


encrypt_message(key=15, message="Common sense is not so common.")

#################################################################################################################################
# Example of interators using yield and next
import copy

def test_iterator():
  vowels = ['a', 'e', 'i', 'o', 'u']
  vowelsIter = iter(vowels) 
  print(next(vowelsIter)) # 'a'
  print(next(vowelsIter)) # 'e'
  print(next(vowelsIter)) # 'i'
  print(next(vowelsIter)) # 'o'
  print(next(vowelsIter)) # 'u'

  def peep(it):
    it_copy = copy.copy(it)
    return [next(it_copy), it]

  it = iter(range(5))
  x, it1 = peep(it)
  print(x, list(it1))
  # 0 [0, 1, 2, 3, 4]


#################################################################################################################################
# Improve execution of function using cache 
def memoize(f):
  cache = {}
  def helper(x):
      if x not in cache:            
          cache[x] = f(x)
      return cache[x]
  return helper

def trace(f):
  f.indent = 0
  def g(x):
      print('|  ' * f.indent + '|--', f.__name__, x)
      f.indent += 1
      value = f(x)
      print('|  ' * f.indent + '|--', 'return', repr(value))
      f.indent -= 1
      return value
  return g

@memoize
@trace
def fib(n):
    if n == 0 or n == 1:
      return 1
    
    return fib(n-1) + fib(n-2)

print(fib(4))