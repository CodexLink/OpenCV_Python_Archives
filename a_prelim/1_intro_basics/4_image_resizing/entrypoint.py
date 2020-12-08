# From the OpenCV library import imread, imwrite and resize function only.
from cv2 import imread, imwrite, resize

# Reading the image using imread() function
image = imread("../0_assets/road.jpg")

# Adjust the parameter's value to your liking.
# ! Keep in mind that this will be the resulting (w, h) to image.
w, h = (800, 700)

# First Parameter is the one who loads the image with imread.
# Second Parameter is tuple containing width and height.
resize_mod = resize(image, (w, h))

# Save the resized image buffer.
imwrite("result.jpg", resize_mod)
