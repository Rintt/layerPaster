#!/usr/bin/env python3
import sys
from turtle import back
from PIL import Image
import os, glob

backgrounds_file = './backgrounds'
backgrounds_sans_character_file = './backgrounds_sans_character'
foregrounds_file = './foregrounds'
foregrounds2_file = './foregrounds2'
save_path = './combinations'
save_path2 = './combinations2'
character = './character'

def mixer(background, foreground, combinations):
  print("Combining " + background[2:] + " and " + foreground[2:] + ", then pasting it into " + combinations[2:])
  count = 0
  for back in os.listdir(background):
    for fore in os.listdir(foreground):
      b = Image.open(background + "/" + back)
      f = Image.open(foreground + "/" + fore)
      b.paste(f, (0, 0), f)
      blended = Image.blend(b, f, alpha=0)
      blended.save(combinations + "/" + str(count) + ".png")
      count = count + 1
  print("Done!")

mixer(backgrounds_sans_character_file, character, backgrounds_file)
mixer(backgrounds_file, foregrounds_file, save_path)
mixer(save_path, foregrounds2_file, save_path2)
print("FINISHED!")
  

