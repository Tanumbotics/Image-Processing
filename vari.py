import cv2
#import numpy as np
import os


def makevari(image, count):
    img = cv2.imread(image)
    b, g, r = cv2.split(img)
    # VARI formula is green - red / green + red - blue
    # Source: http://www.harrisgeospatial.com/docs/BroadbandGreenness.html
    vari = g - r / g + r - b

    # Specify filename for each channel e.g. blue: b_00001.jpg
    vari_file = "vari_" + str(count) + ".jpg"

    # Folder Directory
    exportspath = os.path.join(os.path.dirname(__file__), "exports", "vari")

    # Write processed images
    # Todo use os.makedirs(path, exist_ok=true) to premade folder in case there is no folder
    cv2.imwrite(os.path.join(exportspath, vari_file), vari)
