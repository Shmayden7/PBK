#########################
# Imports:
import json
# Constants:
#########################

#########################
# Load dict from JSON
# Desc: loads a dictionary from a JSON file
# Params: data: the file name, dir: local dir
# Return: N.A. 
# Dependant on: N.A.
#########################
def loadDictFromJSON(file_name: str, dir='data/json/'):
    try:
        with open(dir+file_name) as loaded_file:
            return json.load(loaded_file)
    except IOError as e:
        print('Error, could not open {}'.format(file_name))
        print(e)
        exit()

