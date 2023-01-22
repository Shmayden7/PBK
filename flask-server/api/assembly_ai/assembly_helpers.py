def parseRawAssembly(data, ):

    parsed_data = {}

    

#########################
# Save to .Txt, NEED TO MOVE THIS
# Desc: saves the response as a text file
# Params: data fetched from the API
# Return: N.A., saves a txt file to same directory
# Dependant on: N.A.
#########################
def saveTranscriptToTxt(data, fileName='Assembly_AI_Transcription'):
    if data:
        text_filename =  fileName + '.txt'
        with open(text_filename, 'w') as f:
            f.write(data['text'])
        print('Transcription complete!!!')

