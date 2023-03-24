#########################
# Imports:
import json
# Constants:
#########################

#########################
# Saving dict to JSON
# Desc: saves a dictionary to a JSON file
# Params: data: the dict, file_name: name of the JSON file, Location: local dir
# Return: N.A. 
# Dependant on: N.A.
#########################
def dumpDictToJSON(data, file_name: str, dump_location='data/json/'):
    with open((dump_location+file_name), 'w') as a:
        json.dump(data, a, indent=3)
    print('{} dumped to JSON!'.format(file_name))

