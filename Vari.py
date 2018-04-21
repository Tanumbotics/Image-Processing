import cv2
import numpy as np
img = cv2.imread("test.jpeg")
b,g,r = cv2.split(img)
cv2.imwrite('blue_channel.jpg', b)
cv2.imwrite('green_channel.jpg', g)
cv2.imwrite('red_channel.jpg', r)
# VARI formula is green - red / green + red - blue source:http://www.harrisgeospatial.com/docs/BroadbandGreenness.html
# To Do Merge back
# img = cv2.merge((b,g,r))
VARI = g - r / g + r - b
cv2.imwrite('vari.jpg', VARI)


