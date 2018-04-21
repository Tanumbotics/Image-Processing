from process_image import import_image_files
import cv2
import numpy as np
import matplotlib.pyplot as plt

def compute_vari(images):
	plant_img = [cv2.imread(img_i) for img_i in images]

	for i in range(len(plant_img)):
		img = cv2.imread(plant_img[i])
		b,g,r = cv2.split(img)

		b_file = 'b_000%02d.jpg' %i
		g_file = 'g_000%02d.jpg' %i
		r_file = 'g_000%02d.jpg' %i
		v_file = 'v_000%02d.jpg' %i

		cv2.imwrite(b_file, b)
		cv2.imwrite(g_file, g)
		cv2.imwrite(r_file, r)

		"""VARI formula is green - red / green + red - blue
		Source:http://www.harrisgeospatial.com/docs/BroadbandGreenness.html
		To do Merge back: img = cv2.merge((b,g,r))
		"""
		VARI = g - r / g + r - b
		cv2.imwrite('v_file', VARI)

def main():
    compute_vari(import_image_files())

if __name__ == "__main__":
	main()