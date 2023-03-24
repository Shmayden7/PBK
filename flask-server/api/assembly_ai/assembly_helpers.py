#########################
# Parsing Raw Assembly AI Data
# Desc: Removes un-necessary information from the returned api dict
# Params: raw data dict, single string of attributes, space separated
# Return: dict, Assembly AI data that we care about
# Dependant on: N.A.
#########################
def parseRawAssembly(data: dict, attributes: str):

    # splits up the single string by spaces into array of attributes
    attribute_array = attributes.split()

    important_data = {} # the attributes we acc want

    for i in range(len(attribute_array)):
        print(attribute_array[i])
        string_1 = attribute_array[i]
        string_2 = data[attribute_array[i]]
        new_field = {string_1: string_2}
        print(new_field)
        important_data.update(new_field)

    return important_data


#########################
# Save to .Txt, NEED TO MOVE THIS
# Desc: saves the response as a text file
# Params: data fetched from the API
# Return: N.A., saves a txt file to same directory
# Dependant on: N.A.
#########################
def saveTranscriptToTxt(data, file_name='Assembly_AI_Transcription'):
    if data:
        text_file_name =  file_name + '.txt'
        with open(text_file_name, 'w') as f:
            f.write(data['text'])
        print('Transcription complete!!!')

