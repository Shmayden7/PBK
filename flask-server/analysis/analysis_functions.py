#########################
# Imports:
import os
from data.constants import word_list

from analysis.json_helpers import loadDictFromJSON

# Constants:
#########################

#########################
# Desc: 
# Params: 
# Return: 
# Dependant on: 
#########################
def loadXFromSavedJson(type_out: str, list_number: int, json_path: str) -> dict:
    name = json_path.split('/')[-2]
    folders = []
    data_out = []

    # finding all the folder names in deletion
    for json_path, dirs, filenames in os.walk(json_path):
        folders.extend([{'name': x} for x in dirs])
        break
    folders = sorted(folders, key=lambda x: (x['name'].rsplit('_', 1)[-1] == 'Dfirst', x['name']))

    match type_out:

        case 'accuracy': # out struct contains accuracy values

            for folder in folders:
                path = json_path + folder['name'] +'/'

                data = []
                for index in range(50):

                    if name[3:] == 'normal':
                        file_name = '{}_{}'.format(index,folder['name'] + '.json')
                    elif name[3:] == 'deletion':
                        file_name = '{}_{}'.format(index,folder['name'].rsplit('_', 1)[0] + '.json')

                    loaded_json = loadDictFromJSON(file_name, path)
                    loaded_json = loaded_json['results']

                    if name[3:] == 'normal': # normal case, transcription should match ref word

                        if len(loaded_json) > 0:
                            content = loaded_json[0]['alternatives'][0]['content'].lower()
                            ref_word = word_list[list_number][index]

                            if content == ref_word:
                                data.append(1)
                            else:
                                data.append(0)
                        else:
                            data.append(0)

                    elif name[3:] == 'deletion': # deletion case, transcription should not match ref word

                        if len(loaded_json) > 0:
                            content = loaded_json[0]['alternatives'][0]['content'].lower()
                            ref_word = word_list[list_number][index]

                            if not (content == ref_word):
                                data.append(1)
                            else:
                                data.append(0)
                        else: 
                            data.append(1)

                data_out.extend([{'name': folder['name'], 'data': data}])

        case 'confidence':

            for folder in folders:
                path = json_path + folder['name'] +'/'

                data = []
                for index in range(50):

                    if name[3:] == 'normal':
                        file_name = '{}_{}'.format(index,folder['name'] + '.json')
                    elif name[3:] == 'deletion':
                        file_name = '{}_{}'.format(index,folder['name'].rsplit('_', 1)[0] + '.json')

                    loaded_json = loadDictFromJSON(file_name, path)
                    loaded_json = loaded_json['results']

                    if len(loaded_json) > 0:
                        confidence = loaded_json[0]['alternatives'][0]['confidence']
                        content = loaded_json[0]['alternatives'][0]['content'].lower()
                        ref_word = word_list[list_number][index]
                        
                        data.append(confidence)
                    else:
                        data.append(1)

                data_out.extend([{'name': folder['name'], 'data': data}])
    
    return data_out