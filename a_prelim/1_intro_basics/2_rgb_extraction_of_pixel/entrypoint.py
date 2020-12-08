# From the OpenCV library import imread function only.
from cv2 import imread

# Reading the image using imread() function
image = imread("../0_assets/road.jpg")

# Extracting RGB values.
# Here we have randomly choose a pixel.
# The [100, 100] represents pixel position in X and Y.

# Keep note that you have to be in bounds with respect to image size.

(B, G, R) = image[100, 100]

# Display the pixel values
print("R = {}, G = {}, B = {}".format(R, G, B))

# We can also specify color channel to extract on a pixel.
# The color channel parameter is on the 3rd parameter of image.
# ! Which I guess specifies B color of the pixel (???)
B = image[100, 100, 0]

print("B = {}".format(B))
