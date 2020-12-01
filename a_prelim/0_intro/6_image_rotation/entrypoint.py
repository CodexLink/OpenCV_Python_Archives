# From the OpenCV library import imread, imwrite, getRotationMatrix2D and warpAffineresize function only.
from cv2 import imread, imwrite, getRotationMatrix2D, warpAffine

# Reading the image using imread() function
image = imread("../0_assets/road.jpg")

h, w = image.shape[:2]

# Calculating the center of the image
center = (w // 2, h // 2)

"""
    Create a 2D Matrix based on (1) Canvas Size, (2) Degree, and (3) Image Scale.
    This function also respects image location. (ie. Located from center)

    It returns a 2*3 matrix consisting of values derived from alpha and beta
    alpha = scale * cos(angle)
    beta = scale * sine(angle)

    More Information: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_geometric_transformations/py_geometric_transformations.html
"""

DEGREE_ROTATION = -45
IMAGE_SCALE = 1.0

matrix = getRotationMatrix2D(center, DEGREE_ROTATION, IMAGE_SCALE)

# Performing (affine) transformation to the image with matrix that contains rotation data.
rotated = warpAffine(image, matrix, (w, h))

new_img = imwrite("result.jpg", rotated)
