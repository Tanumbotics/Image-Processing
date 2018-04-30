import os
import cv2


def count_images_in_dir(folder):
    return len([img_i
                for img_i in os.listdir(folder)
                if img_i.endswith('.jpg')])

  
# Import images from folder_name that ends with .jpg
def import_image_files(folder):
    return [os.path.join(folder, img_i)
            for img_i in os.listdir(folder)
            if img_i.endswith('.jpg')]


# Reads images for plotting
def read_image_files(folder):
    return [cv2.imread(img_i) for img_i in import_image_files(folder)]


# Crops images to square
def imcrop_tosquare(image):
    if image.shape[0] > image.shape[1]:
        extra = (image.shape[0] - image.shape[1])
        if extra % 2 == 0:
            crop = image[extra // 2: -extra // 2, :]
        else:
            crop = image[max(0, extra // 2 + 1): min(-1, -(extra // 2)), :]
    elif image.shape[1] > image.shape[0]:
        extra = (image.shape[1] - image.shape[0])
        if extra % 2 == 0:
            crop = image[:, extra // 2, -extra // 2]
        else:
            crop = image[:, max(0, extra // 2 + 1): min(-1, -(extra // 2))]
    else:
        crop = image
    return crop