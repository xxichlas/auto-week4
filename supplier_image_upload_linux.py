#! /usr/bin/env python3
import requests
import os

url = "http://localhost/upload/"
for files in os.listdir("supplier-data/images"):
    if files.endswith("jpeg"):
        with open("supplier-data/images/"+files, 'rb') as image:
            # print(image)
            res = requests.post(url, files={'file':image})
            # print(res.status_code)
