import os
# import matplotlib.pyplot as plt
import cv2


def __init__(self, folder):
	self.folder = folder

def count_images_in_dir(folder):
    return len([img_i
                for img_i in os.listdir(folder)
                if img_i.endswith('.jpg')])


'''Import images from folder_name that ends with .jpg'''
def import_image_files(folder):
    return [os.path.join(folder, img_i)
            for img_i in os.listdir(folder)
            if img_i.endswith('.jpg')]


'''Reads images for plotting'''
def read_image_files(folder):
    return [cv2.imread(img_i) for img_i in import_image_files(folder)]


def resize_images():
    '''TODO: Make a function to resize all images in a dir into same size
    In image processing ML, you need to make sure all imgs are of the same
    sizes
    '''
