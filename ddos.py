#!/bin/env python3
import requests

target = input("Enter the target name or ip or domain name or url: ")


##sending request to the server

data = {'key1': 'value1', 'key2': 'value2'}

##sending a post to the server
response = requests.post(target, data=data)

##printing the status code
print(response.status_code)



