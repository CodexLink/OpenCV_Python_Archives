# From OpenCV Library, import only IMREAD_COLOR, GaussianBlur, bilateralFilter, destroyAllWindows, imread, imshow, imwrite, medianBlur, and waitKey.

# # Resource for function information: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_filtering/py_filtering.html

from cv2 import (
    IMREAD_COLOR,
    GaussianBlur,
    bilateralFilter,
    destroyAllWindows,
    imread,
    imshow,
    imwrite,
    medianBlur,
    waitKey,
)

# Input your file image path here.

IMAGE_FILE_PATH = "../0_assets/img_1.jpg"

WINDOW_TITLES = ["Original", "Guassian", "Median", "Bilateral"]

original_image_buffer = imread(IMAGE_FILE_PATH, IMREAD_COLOR)

# ! (1) In GaussianBlur, instead of a box filter consisting of equal filter coefficients, a Gaussian kernel is used.
# ... The second argument is an odd m x n matrix known as kernel.
# It basically requires standard deviation, from the sigmaX and sigmaY, but i don't know what's that for.
# maybe for blurredness effectiveness or reliability.

# * Keep in note that, to make things better, set the 3rd arguments as 0 for calculation of standard deviation.

gaussian_image_buffer = GaussianBlur(original_image_buffer, (7, 7), 0)

# ! (2) In Median Blur, it computes the median of all the pixels under the kernel window and the central pixel is replaced with this median value.
# * Mostly used in images with white noise on it. Please read the source for more information.

# The 2nd argument passed is basically the m x n of the kernel. The m x n has to be consistent.
median_image_buffer = medianBlur(original_image_buffer, 5)

# ! (3) In Bilateral, it is a complex filtering and is highly effective at noise removal while preserving edges.
# * Because of the complexity, it is slower but better.

# # The bilateralFilter does not use kernel here but uses diameter in pixel (which is in 2nd argument).
# * sigmaColor (3rd argument) is an argument in int, basically the larger the value, the more color will be mixed together on result and,
# * sigmaSpace (4th argument) is an argument in int, basically the larger the value, the large will be the coverage of pixel of influence.

# ! So basically, sigmaSpace and sigmaColor are correlated with one another.
bilateral_image_buffer = bilateralFilter(original_image_buffer, 9, 75, 75)

for idx, eachImageBlurBuffers in enumerate(
    [
        original_image_buffer,
        gaussian_image_buffer,
        median_image_buffer,
        bilateral_image_buffer,
    ]
):
    imshow(
        "%s Blurring Filter | %s" % (WINDOW_TITLES[idx].title(), IMAGE_FILE_PATH),
        eachImageBlurBuffers,
    )

    if idx > 0:
        imwrite("output_%s_blur.png" % WINDOW_TITLES[idx].lower(), eachImageBlurBuffers)


if waitKey(0):
    destroyAllWindows()

# Interpretation Results are basically the following (to img_1.jpg):
# !     Guassian — Blurred asf.
# !     Median —  Quite blurred with low-quality pixels.
# !     Bilateral — Semi-Blurred with but noticeable as Effect.
