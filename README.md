# Intro-Requests-Django
Introductory to the basics of the requests module, JSON formatting, pull, push requests and Django as a framework.

Problem explained:
I need ot get all of the files from a folder called /data/feedback. From here I need to go through the text files
inside of this folder and save the Title, Name, Date, and feedback, which will all be in order. Next I need to post
this back to the website, and check if an error message was recieved, or if it posted properly.

Pythonized explanation:
Necessary modules: os, requests, json
Use listdir() to retrieve the contents of /data/feedback, iterate through files using
with open('textfile.txt') as file:
  for line in file:
    line  = line.split('\n')
    title = line[0]
    name = line[1]
    date = line[2]
    feedback = line[3]
#not sure if i need to use this or just send the push request yet
Instantiate a list 'p' that will hold these dictionaries, use the json.load() and use requests.post('Website.name', params=p)
on the list to upload it to the website. Then use 
