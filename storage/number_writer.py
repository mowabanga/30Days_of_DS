import json

numbers = [1, 2, 3, 5, 6, 8]

file = 'numbers.json'

with open(file, 'w') as file_obj:
    json.dump(numbers, file_obj)
