import os
import matplotlib.pyplot as plt
import cv2

'''Import images from folder_name that ends with .jpg'''
def import_image_files():
    plants_images = [os.path.join(folder_name, img_i)
					 for img_i in os.listdir(folder_name)
                     if img_i.endswith('.jpg')]
    return plants_images

'''Reads images for plotting'''
def read_image_files(plant_images):
    return [cv2.imread(img_i) for img_i in plant_images]
