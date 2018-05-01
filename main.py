import cv2
import numpy as np
import os
import sys
import channelsplit as cs
import vari

filepath = os.path.join(os.path.dirname(__file__), 'plants')

def list_files():
    listoffile = []
    for file in os.listdir(filepath):
        listoffile.append(file)
    return listoffile

def main():
    filecount = 1
    filelist = list_files()
    for file in filelist:
        cs.splitchannel(os.path.join(filepath, file), filecount)
        vari.makevari(os.path.join(filepath, file), filecount)
        filecount = filecount + 1

if __name__ == "__main__":
    main()

