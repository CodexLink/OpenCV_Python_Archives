# From the OpenCV library import imread function only.
from cv2 import imread

# Reading the image using imread() function
image = imread("../0_assets/road.jpg")

# Extracting RGB values.
# Here we have randomly chosen a pixel
# by passing in 100, 100 for height and width.

(B, G, R) = image[100, 100]

# Displaying the pixel values
print("R = {}, G = {}, B = {}".format(R, G, B))

# We can also pass the channel to extract
# the value for a specific channel which is B, G, R.
# The channel parameter is on the 3rd parameter of image.
B = image[100, 100, 0]

print("B = {}".format(B))
