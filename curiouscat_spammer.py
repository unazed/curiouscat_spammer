import random
import string
import requests
import os
import urllib
import time

url='https://curiouscat.me/api/v2/post/create'
personid=input("Curiouscat address (number): ")
sleeptime=int(input("Sleep time (Milliseconds): "))
message=input("Enter message you want to spam with: ")

while True:
    char_set = string.ascii_uppercase + string.digits
    text=message +"".join(random.sample(char_set*6, 6))
    requests.post("https://curiouscat.me/api/v2/post/create", allow_redirects=False, data={
        "addressees": personid,
        "anon": "true",
        "question": text
    })
    print("Sending text "+text)
    print("Sleeping for "+str(sleeptime)+" milliseconds.")
    time.sleep(sleeptime / 1000.0)
