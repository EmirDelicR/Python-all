import json
import os
from filereader.index import File

file = File()

PATH = os.path.dirname(__file__) + '/'

# type is string
json_data_string = file.read_file(PATH, 'test.json')

# Load JSON data from file
# json.load(file)
# Extend FILE class to support load of JSON file

# Load JSON data from a string
# json.loads(string)
json_data = json.loads(json_data_string)
print(type(json_data))
print(json_data)

print(json_data['maps'][0]['id'])


# Write json data to a file
# json.dump(json_data, file)

# Output JSON as string
# json.dumps(json_data)
json_data_sting = json.dumps(json_data)
print(type(json_data_string))
print(json_data_string)


