#!/bin/env python3

#importing libraries
import requests
import sockets
import threading ##threading to speed up the process



target = str(input("Enter the target name or ip or domain name or url: "))
port = int(input("Enter the target port number: "))
trd = int(input("Enter the number of threads: "))

##attacking mechanism will as follows




##sending request to the server

data = {'key1': 'value1', 'key2': 'value2'}

##sending a post to the server
response = requests.post(target, data=data)

##printing the status code
print(response.status_code)



