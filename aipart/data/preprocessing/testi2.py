import cv2


def crop_bottom(image, crop_fraction=0.2):
    """Crop the bottom part of the image by the specified fraction."""
    height = image.shape[0]
    crop_height = int(height * crop_fraction)
    return image[:-crop_height, :]

image = cv2.imread(r'C:\Users\alima\OneDrive\Documents\GitHub\Ai-proj-mthsymb\aipart\data\imgtk_sym_synth_raw\img0.jpg')

image = crop_bottom(image,0.4)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Apply thresholding
# The first parameter is the source image, the second is the threshold value which is used to classify the pixel values,
# the third parameter is the maximum value which is assigned to pixel values exceeding the threshold.
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)

# Step 4: Find contours
# The second parameter is the contour retrieval mode (cv2.RETR_TREE can be used to retrieve all of the contours and reconstructs a full hierarchy of nested contours).
# The third parameter is the contour approximation method (cv2.CHAIN_APPROX_SIMPLE compresses horizontal, vertical, and diagonal segments and leaves only their end points).
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Step 5: Draw contours
# The second parameter is the contours we want to draw.
# The third parameter is the index of the contour to draw (-1 means all contours).
# The fourth parameter is the color of the contours (in BGR format).
# The fifth parameter is the thickness of the contours (-1 for filled contour).
cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

# Step 6: Display the image
cv2.imshow('Contours', image)

# Wait until a key is pressed
cv2.waitKey(0)

# Destroy all the window opened by OpenCV
cv2.destroyAllWindows()
