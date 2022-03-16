#! /usr/bin/env python
import requests
import os

url = "http://localhost/upload/"
for files in os.listdir("C:/Users/ASUS/coursera/auto/week4/supplier-data/images"):
    if files.endswith("jpeg"):
        with open("C:/Users/ASUS/coursera/auto/week4/supplier-data/images/"+files, 'rb') as image:
            # print(image)
            res = requests.post(url, files={'file':image})
            # print(res.status_code)