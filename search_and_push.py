"""This file is going to be left blank for quick checks on code to make sure they are working in a Vacuum."""

import requests, os

folder = (r'Absolute path goes here')
os.chdir(folder)

# Instantiating the necessarry lists and dictionaries.
list_of_dicts_to_push = []
title = {}
name = {}
date = {}
feedback = {}

# Iterates through the specified directory and appends the lines to the list_of_dicts_to_push variable 
# **Maybe should put this into a function?
for file in os.listdir(folder):
    # Important to not forget this dictoinary inside the loop or it will give the incorrect information.
    information = []
    with open(file, 'r') as text:
        for line in text:
            line = line.strip('\n')
            information.append(line)
    # Holder Dictionary for each loop.
    format_dict = {}            
    title['Title'] = information[0]
    name['Name'] = information[1]
    date['Date'] = information[2]
    feedback['Feedback'] = information[3]
    format_dict.update(title)
    format_dict.update(name)
    format_dict.update(date)
    format_dict.update(feedback)
    list_of_dicts_to_push.append(format_dict)

for dictionary in list_of_dicts_to_push:
    # Replace 'www.somewebsite.com' with the website you are trying to push to.
    requests.post("www.somewebsite.com", param=dict)
    
