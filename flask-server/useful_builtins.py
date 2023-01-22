import os, sys, time, json

os.getcwd() # useful for getting current dir

sys.argv[n] # useful for getting the nth console entry

for file in os.listdir(): # prints all the files in a dir
    print(file)

json.dumps(json_varible, indent=1) # this prints json in a more readable way