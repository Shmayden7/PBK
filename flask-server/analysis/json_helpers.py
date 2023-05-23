#########################
# Imports:
import json
# Constants:
#########################

#########################
# Desc: loads a dictionary from a JSON file
# Params: data: the file name, dir: local dir
# Return: N.A. 
# Dependant on: N.A.
#########################
def loadDictFromJSON(file_name: str, dir='data/json/') -> dict:
    try:
        with open(dir+file_name) as loaded_file:
            return json.load(loaded_file)
    except IOError as e:
        print('Error, could not open {}'.format(file_name))
        print(e)
        exit()

#########################
# Desc: saves a dictionary to a JSON file
# Params: data: the dict, file_name: name of the JSON file, Location: local dir
# Return: dumps a JSOn file in specified directory
# Dependant on: N.A.
#########################
def dumpDictToJSON(data, file_name: str, dump_location='data/json/'):
    try:
        with open((dump_location+file_name), 'w') as a:
            json.dump(data, a, indent=3)
        print('{} dumped to JSON'.format(file_name))
    except IOError as e:
        print('Error, could not open {}'.format(file_name))
        print(e)
        exit()

#########################
# Desc: Removes input words from the text and words field of a JSON Object
# Params: file_name: name of the JSON file, parsed: words we want to remove, Location: local dir
# Return: Overwrites the JSON file in same location
# Dependant on: loadDictFromJSON(), dumpDictToJSON()
#########################
def parseOverwriteJSON(file_name: str, parsed: str, dir='data/json/'):
    dict_pre = loadDictFromJSON(file_name, dir)
    dict_post = {
        "list_number": dict_pre['list_number'],
        "audio_duration": dict_pre['audio_duration'],
        "run_time": dict_pre['run_time'],
    }
    removing_words = parsed.split() 
    returned_words_dict = []
    for word in dict_pre['words']:
        word_string = word['text']
        word_string = word_string.translate(str.maketrans('','', '.?!')) # removes peroids
        word_string = word_string.lower() # converts capitalized to lowercase
        word['text'] = word_string
        if not (word['text'] in removing_words):
            returned_words_dict.append(word)
    dict_post.update({'words': returned_words_dict})

    updated_filename = file_name[:-5] + '_parsed.json'
    dumpDictToJSON(dict_post, updated_filename, dir)

#########################
# Desc: Removes input words from the text and words field of a JSON Object
# Params: file_name: name of the JSON file, parsed: words we want to remove, Location: local dir
# Return: Overwrites the JSON file in same location
# Dependant on: loadDictFromJSON(), dumpDictToJSON()
#########################
