#!/usr/bin/env python3
import os, sys
from PIL import Image

size = (600, 400)
os.chdir('supplier-data/images/')
for infile in os.listdir():
    outfile = os.path.splitext(infile)[0]+".jpeg"
    # print(outfile)
    try: 
        with Image.open(infile).convert('RGB') as im:
                im.thumbnail(size)
                im.save(outfile, "JPEG")
    except OSError:
                pass