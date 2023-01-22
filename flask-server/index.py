#########################
# Imports:
import os, sys, time, json, asyncio
from api.assembly_ai.assembly_recorded import getAssemblyAIData
from api.deepgram.deepgram_recorded_old import getDeepgramDataOld
from api.deepgram.deepgram_recorded_new import getDeepgramDataNew


from api.assembly_ai.assembly_helpers import parseRawAssembly
#from .api.deepgram.deepgram_helpers import parseRawDeepgram

# Constants:
audio_path = 'data/audio/'
#########################


#########################
# Running:

testing_file = 'goodnight_moon.wav'
full_path = audio_path + testing_file

#assembly_ai_raw = getAssemblyAIData(full_path)
#deepgram_raw = getDeepgramData(full_path)
asyncio.run(getDeepgramDataOld(full_path))

#important_assembly_data = parseRawAssembly(assembly_ai_raw,)

# important_assembly_data = {
#     'duration': assembly_ai_raw['audio_duration'],
#     'utterances': assembly_ai_raw['utterances'],
#     'text': assembly_ai_raw['text'],
#     'words': assembly_ai_raw['words'],
# }
# print(important_assembly_data)
                             
# json.dumps(important_assembly_data)

#print(deepgram_raw)

# important_deepgram_data = {
#     'duration': deepgram_raw['audio_duration'],
#     'utterances': deepgram_raw['utterances'],
#     'text': deepgram_raw['text'],
#     'words': deepgram_raw['words'],
# }

#########################