"""This file is going to be left blank for quick checks on code to make sure they are working in a Vacuum."""

import requests, os

folder = (r'C:\Users\Marcin Malek\Desktop\testing\tests')
os.chdir(folder)

list_of_dicts_to_push = []
title = {}
name = {}
date = {}
feedback = {}

for file in os.listdir(folder):
    information = []
    with open(file, 'r') as text:
        for line in text:
            line = line.strip('\n')
            information.append(line)
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

print(list_of_dicts_to_push)
for dictionary in list_of_dicts_to_push:
    print(dictionary)
    #requests.post("www.somewebsite.com", param=dict)
    
