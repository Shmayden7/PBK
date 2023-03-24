#########################
# Imports:
import asyncio, json, time

from analysis.export_helpers import dumpDictToJSON

from api.assembly_ai.assembly_recorded import getAssemblyAIData
from api.deepgram.deepgram_recorded_old import getDeepgramDataOld
from api.deepgram.deepgram_recorded_new import getDeepgramDataNew
from api.deepgram.deepgram_live import runDeepgramLiveTranscript

from api.assembly_ai.assembly_helpers import parseRawAssembly
from api.deepgram.deepgram_helpers import parseRawDeepgram

# Constants:

# The default path set is the audio directory
audio_path = 'data/audio/pbk/'

trial = 5
file = 1

eval_file = 'pbk_list_{}.wav'.format(file)
#########################


#########################
# Running:

#########################
### Assembly AI
# assembly_start = time.time()
# assembly_ai_data = getAssemblyAIData(eval_file, audio_path)
# run_time = float("%.2f" % (time.time() - assembly_start))
# assembly_ai_data.update({'run-time': run_time})
           
# print(json.dumps(assembly_ai_data, indent=3))
# print('Assembly classification took {}s!'.format(run_time))

# dumpDictToJSON(assembly_ai_data, 'list_{a}_assembly_t{b}.json'.format(a=file, b=trial))
#########################

#########################
## Deepgram AI
deepgram_start = time.time()
#asyncio.run(getDeepgramDataOld(eval_file, audio_path))
deepgram_data = asyncio.run(getDeepgramDataNew(eval_file, audio_path))
run_time = float("%.2f" % (time.time() - deepgram_start))
deepgram_data.update({'run-time': run_time})

print(json.dumps(deepgram_data, indent=3))
print('Deepgram classification took {}s!'.format(run_time))

dumpDictToJSON(deepgram_data, 'list_{a}_deepgram_t{b}.json'.format(a=file, b=trial), dump_location='data/json/deepgram/')

# asyncio.run(runDeepgramLiveTranscript())
#########################

# important_assembly_data = parseRawAssembly(assembly_ai_raw,)

# important_deepgram_data = {
#     'audio_duration': deepgram_raw['audio_duration'],
#     'utterances': deepgram_raw['utterances'],
#     'text': deepgram_raw['text'],
#     'words': deepgram_raw['words'],
# }

#########################