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
        b_0, g_0, r_0 = [0, 50, 30]

        r = r + 10
        g = g + 10
        b = b + 10

        vvi = ((1 - ((r - r_0) / (r + r_0))) * (1 - ((g - g_0) / (g + g_0))) * (1 - ((b - b_0) / (b + b_0)))) ** (1 / 1)
        # red_channel = (r / (r + g + b))
        # green_chanel = (g / (r + g + b))
        # blue_channel = (b / (r + g + b))

        iso_green = ((2 * g) + b - (2 * r))

        # Specify filename for each channel e.g. blue: b_00001.jpg
        g_file = 'g_000%02d.jpg' % i
        v_file = 'v_000%02d.jpg' % i

        # Specify which directory to save processed channel
        g_export_dir = 'exports/green'
        v_export_dir = 'exports/vvi'

        print('Preparing to process:\t' + g_file)
        cv2.imwrite(os.path.join(g_export_dir, g_file), iso_green)
        print('Preparing to process:\t' + v_file)
        cv2.imwrite(os.path.join(v_export_dir, v_file), vvi)
        print('Done processing:\t' + v_file)
    print('Done procesing image in\t' + FOLDER_DIR)

if __name__ == "__main__":
    main()
