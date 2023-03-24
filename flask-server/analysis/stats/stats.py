#########################
# Imports:
from analysis.export_helpers import dumpDictToJSON
from analysis.import_helpers import loadDictFromJSON
# Constants:

file_name = 'list_1_assembly_t1.json'
directory = 'data/json/assembly'

#########################


data = loadDictFromJSON(file_name, directory)

