import cv2
import PIL
from PIL import Image
import os
import matplotlib.pyplot
import numpy as np
import random

def crop_bottom(image, crop_fraction=0.2):
    """Crop the bottom part of the image by the specified fraction."""
    height = image.shape[0]
    crop_height = int(height * crop_fraction)
    return image[:-crop_height, :]

import cv2

def crop_image_percentages(image, percent_left, percent_right):

  (height, width, channels) = image.shape

  # Calculate the number of pixels to crop from each side
  crop_left_pixels = int(width * percent_left)
  crop_right_pixels = int(width * percent_right)

  # Define the new start and end points for cropping
  start_x = crop_left_pixels
  end_x = width - crop_right_pixels

  # Crop the image
  cropped_image = image[:, start_x:end_x, :]

  return cropped_image




img = cv2.imread(rf'C:\Users\senlab4\codesali\schoolstuff\prac\gitstuff\Ai-proj-mthsymb\aipart\data\imgtk_sym_synth_raw\img{random.randint(1,100)}.jpg')

img = crop_bottom(img, 0.4)
crop_image_percentages
img = img.reshape(64,64)


kernel = np.ones((3,3),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgCanny = cv2.Canny(img,150,200)
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("Gray Image",imgGray)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialation Image",imgDialation)
cv2.imshow("Eroded Image",imgEroded)


cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()