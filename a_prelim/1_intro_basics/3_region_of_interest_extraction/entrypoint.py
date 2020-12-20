# From the OpenCV library import imread and imwrite function only.
from cv2 import imread, imwrite

# Reading the image using imread() function
image = imread("../0_assets/road.jpg")

# We will calculate the region of interest
# by slicing the pixels of the image.

# ! The slice image are actually range of pixels to region of interest.
# This means that, x start point is 100 up to 500, and y start point is 200 up to 700.
roi = image[100:500, 200:700]


# Save the sliced result to the BASE_FOLDER.
imwrite("slice_result.jpg", roi)
