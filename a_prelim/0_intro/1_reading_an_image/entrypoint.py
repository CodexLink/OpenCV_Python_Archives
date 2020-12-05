# From the OpenCV library import imread function only.
from cv2 import imread

# Reading the image using imread() function
image = imread("../0_assets/road.jpg")

# Extracting the height and width of an image using shape function property.

# According to the documentation.
# It returns tuple of 3 which returns Columns, Row and Channel (If image has a color channel.)
# More Detail: https://docs.opencv.org/master/d3/df2/tutorial_py_basic_ops.html

# ! At this point, we aim to get the tuple index of 0 and 1 by assigning them to h and w
# which means... [truncated..]

print(image.shape)
h, w = image.shape[:2]

# Displaying the height and width
print("(%i) == (Height, Width)" % w)
