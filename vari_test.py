from process_image import *
import cv2
import numpy as np
import os
# import matplotlib.pyplot as plt

FOLDER_DIR = 'plants'


def main():
    plant_img = read_image_files(FOLDER_DIR)

    for i in range(count_images_in_dir(FOLDER_DIR)):
        img = imcrop_tosquare(plant_img[i])
        b, g, r = cv2.split(img)

        # Specify filename for each channel e.g. blue: b_00001.jpg
        b_file = 'b_000%02d.jpg' % i
        g_file = 'g_000%02d.jpg' % i
        r_file = 'r_000%02d.jpg' % i
        v_file = 'v_000%02d.jpg' % i

        # Specify which directory to save processed channel
        b_export_dir = 'exports/blue'
        g_export_dir = 'exports/green'
        r_export_dir = 'exports/red'
        v_export_dir = 'exports/vari'

        # Write processed images
        print('Preparing to process:\t' + b_file)
        cv2.imwrite(os.path.join(b_export_dir, b_file), b)
        print('Done processing:\t' + b_file)
        print('Preparing to process:\t' + g_file)
        cv2.imwrite(os.path.join(g_export_dir, g_file), g)
        print('Done processing:\t' + g_file)
        print('Preparing to process:\t' + r_file)
        cv2.imwrite(os.path.join(r_export_dir, r_file), r)
        print('Done processing:\t' + r_file)

        '''VARI formula is green - red	 / green + red - blue
		Source:http://www.harrisgeospatial.com/docs/BroadbandGreenness.html
		To do Merge back: img = cv2.merge((b,g,r))
		'''
        print('Preparing to process:\t' +v_file)
        VARI = g - r / g + r - b
        cv2.imwrite(os.path.join(v_export_dir, v_file), VARI)
        print('Done processing:\t' + r_file)
    print('Done procesing image in\t' + FOLDER_DIR)


if __name__ == "__main__":
    main()
