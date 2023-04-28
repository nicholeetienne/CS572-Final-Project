#! /usr/bin/env python
from collections import defaultdict

"""
This module will have two inputs <History files path> <Train/eval/Test files path>.
On getting these files, a user specific dictionary is made. 
All feature functions will have to call the functions in this file 

eval and dev are aresed interchangably 
"""

""" This function reads the train file and 
    puts everything into a list. 
    This list is what is going to be referred to by the rest of the 
    training program
"""
#user_objects=defaultdict(list)

def read_file(file_name,search_logs):
    #global search_logs
    with open(file_name) as f:
      for each in f.readlines():
           search_logs.append(each)
    return search_logs


"""create a dictionary per user. The key is User_ID and the value is the list of user sessions - This would be done for obtaining 
user history in an easy format"""
def get_user_objects(search_logs):
#    global search_logs
 #   global user_objects
    user_objects=defaultdict(list)
    temp = []
    for log in search_logs:
        items=log.split()
        if items[1] == 'M':
            if(len(temp)!=0):
                user_objects[user_id].append(temp)
            user_id=items[3]
            temp = []
            continue;
        temp.append(log)
    if(len(temp)!=0):
        user_objects[user_id].append(temp)
    return user_objects




