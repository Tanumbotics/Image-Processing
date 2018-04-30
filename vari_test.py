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
        
        # Formula based on http://phl.upr.edu/projects/visible-vegetation-index-vvi
        r_0, g_0, b_0 = [30, 50, 0]

        vvi_0 = np.subtract(1, (np.absolute(np.divide(np.subtract(r, r_0), np.add(r, r_0)))))
        vv1_1 = np.subtract(1, (np.absolute(np.divide(np.subtract(g, g_0), np.add(g, g_0)))))
        vv1_2 = np.subtract(1, (np.absolute(np.divide(np.subtract(b, b_0), np.add(b, b_0)))))
        vvi = np.multiply(vvi_0, vv1_1, vv1_2)

        '''Formula based on https://www.researchgate.net/post/Extract_Greenness2
        B = b / (b + g + r)
        G = g / (b + g + r)
        R = r / (b + g + r)
        '''
        B = np.divide(b, (np.add(b, g, r)))
        G = np.divide(g, (np.add(b, g, r)))
        R = np.divide(r, (np.add(b, g, r)))

        # iso_green = ((2 * G) + B - (2 * R))
        iso_green = np.subtract(np.add(np.multiply(2, G), B), np.multiply(2, R))

        # Specify filename for each channel e.g. blue: b_00001.jpg
        b_file = 'b_000%02d.jpg' % i
        g_file = 'g_000%02d.jpg' % i
        r_file = 'r_000%02d.jpg' % i
        va_file = 'va_000%02d.jpg' % i
        vv_file = 'vv_000%02d.jpg' % i
        ig_file = 'ig_000%02d.jpg' % i

        # Specify which directory to save processed channel
        b_export_dir = 'exports/blue'
        g_export_dir = 'exports/green'
        r_export_dir = 'exports/red'
        va_export_dir = 'exports/vari'
        vv_export_dir = 'exports/vvi'
        ig_export_dir = 'exports/ig'

        # Write processed images
        cv2.imwrite(os.path.join(b_export_dir, b_file), b)
        cv2.imwrite(os.path.join(g_export_dir, g_file), g)
        cv2.imwrite(os.path.join(r_export_dir, r_file), r)

        """ vari formula is green - red / green + red - blue
		    Source: http://www.harrisgeospatial.com/docs/BroadbandGreenness.html
            vari = g - r / g + r - b
        """
        vari = np.divide(np.subtract(g, r), np.subtract(np.add(g, r), b))
        cv2.imwrite(os.path.join(va_export_dir, va_file), vari)
        cv2.imwrite(os.path.join(vv_export_dir, vv_file), vvi)
        cv2.imwrite(os.path.join(ig_export_dir, ig_file), iso_green)

        
if __name__ == "__main__":
    main()
