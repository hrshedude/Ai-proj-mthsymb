import cv2
import numpy as np

def preprocess_image(image_path, resize_dim=(256, 256), low_threshold=100, high_threshold=200, dilate_kernel_size=3, erode_kernel_size=3, erode_iterations=1):
    # Step 1: Read the image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Image not found at the path: {image_path}")
    
    # Step 2: Resize the image
    resized_image = cv2.resize(image, resize_dim)
    
    # Step 3: Convert the image to grayscale
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    
    # Step 4: Apply Gaussian Blur
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    
    # Step 5: Edge detection using Canny
    edges = cv2.Canny(blurred_image, low_threshold, high_threshold)
    
    # Step 6: Dilate the edges
    dilate_kernel = np.ones((dilate_kernel_size, dilate_kernel_size), np.uint8)
    dilated_image = cv2.dilate(edges, dilate_kernel, iterations=1)
    
    # Step 7: Erode the dilated edges
    erode_kernel = np.ones((erode_kernel_size, erode_kernel_size), np.uint8)
    eroded_image = cv2.erode(dilated_image, erode_kernel, iterations=erode_iterations)
    
    # Step 8: Normalize the image
    normalized_image = cv2.normalize(eroded_image, None, 0, 255, cv2.NORM_MINMAX)
    
    return resized_image, gray_image, blurred_image, normalized_image

def on_trackbar(val):
    low_threshold = cv2.getTrackbarPos('Low Threshold', 'Image Processing')
    high_threshold = cv2.getTrackbarPos('High Threshold', 'Image Processing')
    dilate_kernel_size = cv2.getTrackbarPos('Dilate Kernel Size', 'Image Processing')
    erode_kernel_size = cv2.getTrackbarPos('Erode Kernel Size', 'Image Processing')
    erode_iterations = cv2.getTrackbarPos('Erode Iterations', 'Image Processing')
    
    # Ensure kernel sizes are odd and at least 1
    dilate_kernel_size = max(1, dilate_kernel_size)
    if dilate_kernel_size % 2 == 0:
        dilate_kernel_size += 1
    
    erode_kernel_size = max(1, erode_kernel_size)
    if erode_kernel_size % 2 == 0:
        erode_kernel_size += 1
    
    resized_image, gray_image, blurred_image, edges = preprocess_image(image_path, low_threshold=low_threshold, high_threshold=high_threshold, dilate_kernel_size=dilate_kernel_size, erode_kernel_size=erode_kernel_size, erode_iterations=erode_iterations)
    
    # Concatenate images horizontally
    top_row = cv2.hconcat([resized_image, cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)])
    bottom_row = cv2.hconcat([cv2.cvtColor(blurred_image, cv2.COLOR_GRAY2BGR), cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)])
    concatenated_image = cv2.vconcat([top_row, bottom_row])
    
    cv2.imshow('Image Processing', concatenated_image)

# Example usage
image_path = r'C:\Users\alima\OneDrive\Documents\GitHub\Ai-proj-mthsymb\aipart\data\imgtk_sym_synth_raw\img0.jpg'
resized_image, gray_image, blurred_image, edges = preprocess_image(image_path)

# Create a window
cv2.namedWindow('Image Processing')

# Create trackbars for Canny edge thresholds, dilation kernel size, erosion kernel size, and erosion iterations
cv2.createTrackbar('Low Threshold', 'Image Processing', 100, 255, on_trackbar)
cv2.createTrackbar('High Threshold', 'Image Processing', 200, 255, on_trackbar)
cv2.createTrackbar('Dilate Kernel Size', 'Image Processing', 3, 21, on_trackbar)  # Kernel size from 1 to 21
cv2.createTrackbar('Erode Kernel Size', 'Image Processing', 3, 21, on_trackbar)  # Kernel size from 1 to 21
cv2.createTrackbar('Erode Iterations', 'Image Processing', 1, 10, on_trackbar)  # Iterations from 1 to 10

# Initial display
on_trackbar(0)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
