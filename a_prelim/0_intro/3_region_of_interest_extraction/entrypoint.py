# From the OpenCV library import imread and imwrite function only.
from cv2 import imread, imwrite

# Reading the image using imread() function
image = imread("../0_assets/road.jpg")

# We will calculate the region of interest
# by slicing the pixels of the image
roi = image[100 : 500, 200 : 700]


# Save the sliced result to the BASE_FOLDER.
imwrite("slice_result.jpg", roi)
