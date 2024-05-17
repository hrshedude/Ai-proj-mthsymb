import cv2
import PIL
from PIL import Image
import os
import matplotlib.pyplot
import numpy as np

def crop_bottom(image, crop_fraction=0.2):
    """Crop the bottom part of the image by the specified fraction."""
    height = image.shape[0]
    crop_height = int(height * crop_fraction)
    return image[:-crop_height, :]


img = cv2.imread(r'C:\Users\alima\OneDrive\Documents\GitHub\Ai-proj-mthsymb\aipart\data\imgtk_eq_synth_raw\img0.jpg')

img = crop_bottom(img, 0.4)

cv2.imshow("hi", img)



kernel = np.ones((3,3),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgCanny = cv2.Canny(img,150,200)
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
# imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("Gray Image",imgGray)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialation Image",imgDialation)
# cv2.imshow("Eroded Image",imgEroded)

contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

# Step 6: Display the image
cv2.imshow('Contours', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()