#! /usr/bin/env python3
import os
import requests


for files in os.listdir("C:/Users/ASUS/coursera/auto/week4/supplier-data/descriptions"):
    # print(files)
    with open(r'C:/Users/ASUS/coursera/auto/week4/supplier-data/descriptions/'+files, 'r') as file:
        files = files.strip(".txt")+".jpeg"
        lines = [line.rstrip('\n') for line in file]
        lines[1] = int(lines[1].strip(' lbs'))
        fruit = { "name": lines[0], "weight": lines[1], "description": lines[2], "image_name": files }
        print(fruit)
        res = requests.post("http://[linux-instance-external-IP]/fruits/", data=fruit)
        