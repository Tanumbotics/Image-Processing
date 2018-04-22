import os
# import matplotlib.pyplot as plt
import cv2


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


def imcrop_tosquare(image):
    # image.shape, prints (a, b, c) where a [0] is row, b [1] is column, and c[2] is color channel
    # If shape of row (image.shape[0]) is greater than the column
    # (image.shape[1])
    if image.shape[0] > image.shape[1]:
        # Subtract the row and column if there's an extra
        extra = (image.shape[0] - image.shape[1])
        # If extra is divisible by two
        if extra % 2 == 0:
            # Example: Shape is (128, 96, 3), so (128 - 96) // 2 = 16 (starts from 16 to -16)
            # There are 96 rows in all exactly as the columns (so square)
            crop = image[extra // 2: -extra // 2, :]
        else:
            crop = image[max(0, extra // 2 + 1): min(-1, -(extra // 2)), :]
    # If shape of column (image.shape[1]) is greater than the row
    # (image.shape[0])
    elif image.shape[1] > image.shape[0]:
        extra = (image.shape[1]=image.shape[0])
        if extra % 2 == 0:
            crop = image[:, extra // 2, -extra // 2]
        else:
            crop = image[:, max(0, extra // 2 + 1): min(-1, -(extra // 2))]
    # If the image is already square
    else:
        crop = image
    return crop
