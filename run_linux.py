#! /usr/bin/env python3
import os
import requests


for files in os.listdir("supplier-data/descriptions"):
    # print(files)
    with open(r'supplier-data/descriptions/'+files, 'r') as file:
        files = files.strip(".txt")+".jpeg"
        lines = [line.rstrip('\n') for line in file]
        lines[1] = int(lines[1].strip(' lbs'))
        fruit = { "name": lines[0], "weight": lines[1], "description": lines[2], "image_name": files }
        print(fruit)
        res = requests.post("http://34.136.1.25/fruits/", data=fruit)
        