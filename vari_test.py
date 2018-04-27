from process_image import *
import cv2
import numpy as np
import os
# import matplotlib.pyplot as plt

FOLDER_DIR = 'plants'


def main():
    plant_img = read_image_files(FOLDER_DIR)

    for i in range(count_images_in_dir(FOLDER_DIR)):
        img_rgb = imcrop_tosquare(plant_img[i])
        b, g, r = cv2.split(img_rgb)
        # red_channel = (r / (r + g + b))
        # green_chanel = (g / (r + g + b))
        # blue_channel = (b / (r + g + b))
        iso_green = ((2 * g) + b - (2 * r))

        # Specify filename for each channel e.g. blue: b_00001.jpg
        g_file = 'g_000%02d.jpg' % i

        # Specify which directory to save processed channel
        g_export_dir = 'exports/green'

        print('Preparing to process:\t' + g_file)
        cv2.imwrite(os.path.join(g_export_dir, g_file), iso_green)
        print('Done processing:\t' + g_file)
    print('Done procesing image in\t' + FOLDER_DIR)

'''def split_image(image):
    # Formula based from https://www.researchgate.net/post/Extract_Greenness2
    b, g, r = cv2.split(image)
    red_channel = (r / (r + g + b))
    green_chanel = (g / (r + g + b))
    blue_channel = (b / (r + g + b))
    iso_green = ((2 * g) + b - (2 * r))
    return iso_green
'''

if __name__ == "__main__":
    main()
