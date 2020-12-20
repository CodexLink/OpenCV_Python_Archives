# ! You need to understand morphological transformations before understanding the code.
# * Please check the video for more information with link below.
# # Link is here: https://pythonprogramming.net/morphological-transformation-python-opencv-tutorial/

# * Check the documentation as well for function argument options.
# # Link is here: https://docs.opencv.org/master/d9/d61/tutorial_py_morphological_ops.html#gsc.tab=0

# * For Clarifications on Kernel and Convolation and the ones() usage on Dilation and Erosion.
# # Check it here: https://towardsdatascience.com/basics-of-kernels-and-convolutions-with-opencv-c15311ab8f55
# # Another one: https://github.com/atduskgreg/opencv-processing-book/blob/master/book/filters/blur.md
# # For Full Guide: https://www.pyimagesearch.com/2016/07/25/convolutions-with-opencv-and-python/

# # Visualization #1: https://compvisionlab.wordpress.com/2013/04/07/convolution-opencv/
# # Visualization #2 with OP Question: https://datascience.stackexchange.com/questions/23183/why-convolutions-always-use-odd-numbers-as-filter-size
# ! You need to have a little to more patience when reading these articles especially if you started off,
# ! with little knowledge to college level maths. (For atleast, by understanding them)

# From OpenCV Library, import only IMREAD_COLOR, destroyAllWindows, dilate, erode, imread, imshow, imwrite and waitKey.

from cv2 import (
    IMREAD_COLOR,
    destroyAllWindows,
    dilate,
    erode,
    imread,
    imshow,
    imwrite,
    waitKey,
)
from numpy import ones, uint8

# Constant

WINDOW_TITLES = ["Original", "Eroded", "Dilated"]


# Input your file path here.
IMAGE_PATH = "../0_assets/img_8.png"

# ! Modify your parameters here.
PROCESS_ITERATION = 3  # The no of items for both erode and dilate buffer.

MATRIX_SYMMETRIC_SIZE = 3  # * No of Col and Rows of the Kernel Matrix.

# Read an image with default color RGB metric.
original_image_buffer = imread(IMAGE_PATH, IMREAD_COLOR)


# ! About Kernel
# * You have to imagine that the whole pixel of the original image is a big matrix.
# * And a kernel which is basically a small matrix (preferrable odd),
# * has to traverse from left to right, top to bottom.

# The Covered Parts of the Big Matrix from Kernel * Actual Kernel = Summation of All Elements.
# Will the output / result of the middle pixel after calculation, this is called convulation.

# ! Check the link of Visualization #2 with OP Question on the top for the actual visualization.
# * For erosion, we have to use a (m x n) of matrix with a value of 1.
# * Because we only need to validate a certain pixel either 1 or 0. For Instance, 0 To Black, 1 To White for img_8.
# # More Information Here: https://stackoverflow.com/questions/62417509/why-do-we-use-an-array-of-ones-for-a-kernel-in-opencv.
kernel = ones(
    (MATRIX_SYMMETRIC_SIZE, MATRIX_SYMMETRIC_SIZE), uint8
)  # We have to ensure that the matrix values are indeed, pure unsigned integer.

# Using erode and dilate methods.
erode_buffer = erode(original_image_buffer, kernel, iterations=PROCESS_ITERATION)
dilate_buffer = dilate(original_image_buffer, kernel, iterations=PROCESS_ITERATION)

# Displaying the image with for loop to have a clean code.

for idx, eachBuffers in enumerate([original_image_buffer, erode_buffer, dilate_buffer]):
    imshow(
        "%s Image of %s | Processed with %s Iteration/s"
        % (WINDOW_TITLES[idx], IMAGE_PATH, PROCESS_ITERATION),
        eachBuffers,
    )
    if idx > 0:
        imwrite("output_%s.png" % WINDOW_TITLES[idx].lower(), eachBuffers)

if waitKey(0):
    destroyAllWindows()
