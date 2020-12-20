# From the OpenCV library import imread, imwrite and resize function only.
from cv2 import imread, imwrite, resize

# Reading the image using imread() function
image = imread("../0_assets/road.jpg")

old_dim = image.shape[:2]  # old_dim will get a value of class'tuple in (h, w).

# ! Calculate the ratio with one coordinates revealed to expected resize size.

# In this case, we expect that the result has a width of (int) 800.
# So we need to do the following:
# 1. Calculate the ratio with default width and the declared expected width. -> Returns a Ratio.
# 2. Calculate the height by multiplying default height with ratio for adjustments.

# ! Note that, old_dim() contains h and w, as a tuple.

decl_width = 800
ratio = decl_width / old_dim[1]  # (1)

# Creating a tuple containing width and height after calculation.
new_dim = (decl_width, int(old_dim[0] * ratio))  # (2)

# First Parameter is the one who loads the image with imread.
# Second Parameter is a tuple containing new width and height.
resize_mod = resize(image, new_dim)

# Save the resized image buffer.
imwrite("result.jpg", resize_mod)
