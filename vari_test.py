from process_image import import_image_files
import cv2
import numpy as np
import os
# import matplotlib.pyplot as plt

def compute_vari(images):
	plant_img = [cv2.imread(img_i) for img_i in images]

	for i in range(2):
		img = plant_img[i]
		b,g,r = cv2.split(img)

		b_file = 'b_000%02d.jpg' %i
		g_file = 'g_000%02d.jpg' %i
		r_file = 'r_000%02d.jpg' %i
		v_file = 'v_000%02d.jpg' %i

		b_export_dir = 'exports/blue'
		g_export_dir = 'exports/green'
		r_export_dir = 'exports/red'
		v_export_dir = 'exports/vari'


		cv2.imwrite(os.path.join(b_export_dir, b_file), b)
		cv2.imwrite(os.path.join(g_export_dir, g_file), g)
		cv2.imwrite(os.path.join(r_export_dir, r_file), r)

		"""VARI formula is green - red	 / green + red - blue
		Source:http://www.harrisgeospatial.com/docs/BroadbandGreenness.html
		To do Merge back: img = cv2.merge((b,g,r))
		"""
		VARI = g - r / g + r - b
		cv2.imwrite(os.path.join(v_export_dir, v_file), VARI)

def main():
    compute_vari(import_image_files())

if __name__ == "__main__":
	main()