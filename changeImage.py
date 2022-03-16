#!/usr/bin/env python3
import os, sys
from PIL import Image

size = (600, 400)
for infile in os.listdir("C:/Users/ASUS/coursera/auto/week4/supplier-data/images"):
    outfile = os.path.splitext(infile)[0]+".jpeg"
    # print(outfile)
    os.chdir("C:/Users/ASUS/coursera/auto/week4/supplier-data/images")
    try: 
        with Image.open(infile).convert('RGB') as im:
                im.thumbnail(size)
                im.save("C:/Users/ASUS/coursera/auto/week4/supplier-data/images/"+outfile, "JPEG")
    except OSError:
                pass