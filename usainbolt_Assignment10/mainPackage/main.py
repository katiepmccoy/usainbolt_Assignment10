#Name:Usain Bolt Group
#email: mccoykp@mail.uc.edu, gogginjt@mail.uc.edu, allfreqy@mail.uc.edu
#Assignment Title: Assignment 10
#Course: IS 4010
#Semester/Year: Spring 2023
#Brief Description: This project demonstrates that I can use Eclipse to create a PyDev project that creates an API call with a URL. This also demonstrates that I can build a URL with a 
#data request and submit it to the server. This also shows I can parse the results from the server into a python dictionary and extract data from the dictionary. 
#Citations:
#Anything else that's relevant:
#main.py
import requests
import json
# Make a request to a web server and store the results in response
#response = requests.get('https://api.nasa.gov/neo/rest/v1/neo/3542519?api_key=0EP0AAZk9LAY5GZ5sMSvslhzFfk4T6O37z3YF9c4')
response = requests.get('https://api.nasa.gov/neo/rest/v1/neo/browse?api_key=0EP0AAZk9LAY5GZ5sMSvslhzFfk4T6O37z3YF9c4')
json_string = response.content
#
parsed_json = json.loads(json_string) # This turned the json object into a dictionary
#Invoke my function in the other module, pass it parsed_json
print(parsed_json)
for name in parsed_json['near_earth_objects']: 
    print(name['name_limited'])