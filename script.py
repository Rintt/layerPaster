#!/usr/bin/env python3
import sys
from PIL import Image
import os, glob

backgrounds = './backgrounds'
foregrounds = './foregrounds'
save_path = './combinations'
count = 0
for background in os.listdir(backgrounds):
  for foreground in os.listdir(foregrounds):
    b = Image.open(backgrounds + "/" + background)
    f = Image.open(foregrounds + "/" + foreground)
    b.paste(f, (0, 0), f)
    blended = Image.blend(b, f, alpha=0)
    blended.save("./combinations/blended" + str(count) + ".png")
    count = count + 1
    print("created " + background + " + " + foreground)
print("FINISHED!")
  

