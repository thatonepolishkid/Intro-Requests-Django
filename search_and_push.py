# Importing necessary modules.
import requests, os

folder = (r'C:\Users\Marcin Malek\Desktop\testing\tests')
os.chdir(folder)

#Url needs to be replaced with the external IP address from the lab.
url = 'http://35.185.118.147/feedback/'

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
    title['title'] = information[0]
    name['name'] = information[1]
    date['date'] = information[2]
    feedback['feedback'] = information[3]
    format_dict.update(title)
    format_dict.update(name)
    format_dict.update(date)
    format_dict.update(feedback)
    list_of_dicts_to_push.append(format_dict)


print(list_of_dicts_to_push)


for dictionary in list_of_dicts_to_push:
    # Replace 'http://<corpweb-external-IP>/feedback' with the website you are trying to push to.
    response = requests.post(url, params=dictionary)
    if response.ok:
        print("Response has been received")
    if not response.ok:
        raise Exception("Get failed with status code {}".format(response.status_code))
