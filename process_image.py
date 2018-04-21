import os
# import matplotlib.pyplot as plt
import cv2

def count_images_in_dir():
	return len([img_i
		        for img_i in os.listdir('plants')
		        if img_i.endswith('.jpg')])

'''Import images from folder_name that ends with .jpg'''
def import_image_files():
    plants_images = [os.path.join('plants', img_i)
                    for img_i in os.listdir('plants')
                    if img_i.endswith('.jpg')]
    return plants_images

'''Reads images for plotting'''
def read_image_files():
    return [cv2.imread(img_i) for img_i in import_image_files()]

def resize_images():
	'''TODO: Make a function to resize all images in a dir into same size
	In image processing ML, you need to make sure all imgs are of the same
	sizes
	'''
