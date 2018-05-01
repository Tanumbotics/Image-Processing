import cv2
#import numpy as np
import os

def splitchannel(image, count):
    img = cv2.imread(image)
    b,g,r = cv2.split(img)

    # Specify filename for each channel e.g. blue: b_00001.jpg
    b_file = "b_" + str (count) + ".jpg"
    g_file = "g_" + str (count) + ".jpg"
    r_file = "r_" + str (count) + ".jpg"

    # Folder Directory 
    exportspath = os.path.join(os.path.dirname(__file__), "exports")
    b_export_dir = os.path.join(exportspath, "blue_channel")
    g_export_dir = os.path.join(exportspath, "green_channel")
    r_export_dir = os.path.join(exportspath, "red_channel")

    # Write processed images
    # Todo use os.makedirs(path, exist_ok=true) to premade folder in case there is no folder
    cv2.imwrite(os.path.join(b_export_dir, b_file), b)
    cv2.imwrite(os.path.join(g_export_dir, g_file), g)
    cv2.imwrite(os.path.join(r_export_dir, r_file), r)