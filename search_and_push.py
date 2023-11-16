# Importing necessary modules.
import requests, os

folder = (r'Absolute path goes here')
os.chdir(folder)

#Url needs to be replaced with the external IP address from the lab.
url = 'http://<corpweb-external-IP>/feedback'

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



response = requests.get(url)

if response.ok:
    for dictionary in list_of_dicts_to_push:
        # Replace 'http://<corpweb-external-IP>/feedback' with the website you are trying to push to.
        requests.post("http://<corpweb-external-IP>/feedback", param=dictionary)
        if not response.ok:
            raise Exception("Get failed with status code {}".format(response.status_code))
