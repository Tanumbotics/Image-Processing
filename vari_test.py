from process_image import *
import cv2
import numpy as np
import os
# import matplotlib.pyplot as plt

FOLDER_DIR = 'plants'


def main():
    plant_img = read_image_files(FOLDER_DIR)

    for i in range(count_images_in_dir(FOLDER_DIR)):
        img_rgb = plant_img[i]
        b, g, r = cv2.split(img_rgb)

        r_0, g_0, b_0 = [1000, 100, 1000]

        vvi_0 = 1 - (np.absolute(np.divide(np.subtract(r, r_0), np.add(r, r_0))))
        vv1_1 = 1 - (np.absolute(np.divide(np.subtract(g, g_0), np.add(g, g_0))))
        vv1_2 = 1 - (np.absolute(np.divide(np.subtract(b, b_0), np.add(b, b_0))))
        vvi = np.multiply(vvi_0, vv1_1, vv1_2)

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
