#########################
# Imports:
import json
from data.constants import word_list
from analysis.json_helpers import loadDictFromJSON
from classes.DoubleyLinkedList import Node, DoubleyLinkedList
# Constants:
#########################

#########################
# Desc: loads a dictionary from a JSON file
# Params: data: the file name, dir: local dir
# Return: N.A. 
# Dependant on: N.A.
#########################
def segmentResponces(eval_file: str, confadince: int, audio_path='data/audio/', json_path='data/json/', segment_dump_location='data/audio/segment/'):
    import_json = loadDictFromJSON(eval_file, json_path)
    import_json_words = import_json['words']
    ideal_word_list = word_list[import_json['list_number']]
    
    # Initiating the Doubly Linked List
    robot_prompts = DoubleyLinkedList()
    child_responces = DoubleyLinkedList()

    # Populating the Lists
    for word in import_json_words:
        if word['speaker'] == 'A':
            robot_prompts.push_tail(word)
        elif word['speaker'] == 'B':
            child_responces.push_tail(word)

    # # Filling in Gaps made by the AI
    # current_word = robot_prompts.head
    # for index in range(robot_prompts.get_size()):
    #     if current_word['text'] == ideal_word_list[index]:
    #         current_word = current_word.next
    #     else: # if the words dont match the word list 
    #         temp_data = {
    #             'text': ideal_word_list[index],
    #             'start': 
    #             'end':
    #             'confidince':
    #             'speaker':
    #         }


    robot_prompts.print('text')

    # print('Length of robot pormots: {}'.format(robot_prompts.get_size()))
    # print('Length of child responces: {}'.format(child_responces.get_size()))

    # index_in_pbk = 0
    # #for word_index in range(len(import_json['text'])): 
    # for word_index in range(3):
    #     current_word = import_json_words[word_index]['text']
    #     next_word = import_json_words[[word_index+1]'text']
    #     segment_start = 0
    #     segment_end = 0

    #     # Case 1, kid gets word right and above confadince
    #     if (
    #         current_word['speaker'] == 'A' # robot is the first speaker
    #         and next_word['speaker'] == 'B' # child is the second speaker
    #         and current_word['text'] == ideal_word_list[index_in_pbk] # the robot text matches that of the pbk list
    #         and next_word['text'] == ideal_word_list[index_in_pbk] # the childs response matches that of the pbk list
    #         and next_word['confidence'] >= confadince # the response is above confadince bound (dont include word in dump)
    #     ):
    #         print('Word {}: Condition 1'.format(ideal_word_list[index_in_pbk]))

    #     # Case 2, kid gets word right and below confadince
    #     if (
    #         current_word['speaker'] == 'A' # robot is the first speaker
    #         and next_word['speaker'] == 'B' # child is the second speaker
    #         and current_word['text'] == ideal_word_list[index_in_pbk] # the robot text matches that of the pbk list
    #         and next_word['text'] == ideal_word_list[index_in_pbk] # the childs response matches that of the pbk list
    #         and next_word['confidence'] <= confadince # the response is above confadince bound (dont include word in dump)
    #     ):
    #         print('Word {}: Condition 2'.format(ideal_word_list[index_in_pbk]))

    #     # Case 3, Ai guesses the kids responce incorrectly
    #     if (
    #         current_word['speaker'] == 'A' # robot is the first speaker
    #         and next_word['speaker'] == 'B' # child is the second speaker
    #         and current_word['text'] == ideal_word_list[index_in_pbk] # the robot text matches that of the pbk list
    #         and not (next_word['text'] == ideal_word_list[index_in_pbk]) # the childs response matches that of the pbk list
    #     ):
    #         print('Word {}: Condition 3'.format(ideal_word_list[index_in_pbk]))

    #     # Case 4, Ai does not catch the kids word at all
    #     if (
    #         current_word['speaker'] == 'A' # robot is the first speaker
    #         and not (next_word['speaker'] == 'B') # robot is the second responce, missed the childs Transcription
    #         and current_word['text'] == ideal_word_list[index_in_pbk] # the robot text matches that of the pbk list
    #     ):
    #         print('Word {}: Condition 4'.format(ideal_word_list[index_in_pbk]))

    #     # Case 4, Ai screws up transcription of the robot word


