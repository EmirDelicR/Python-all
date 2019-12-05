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