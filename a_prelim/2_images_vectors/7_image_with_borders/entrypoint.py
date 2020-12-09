# From the OpenCV Library, import only, BORDER_CONSTANT, BORDER_REFLECT, copyMakeBorder, destroyAllWindows, imread, imwrite, and waitKey.
from cv2 import (
    BORDER_CONSTANT,
    BORDER_DEFAULT,
    BORDER_REFLECT,
    BORDER_REFLECT_101,
    BORDER_REPLICATE,
    copyMakeBorder,
    destroyAllWindows,
    imread,
    imshow,
    imwrite,
    waitKey,
)

# Please add your file image path.
IMAGE_PATH = "../0_assets/img_1.jpg"

# Constants
WINDOW_TITLES = ["Constant", "Reflect", "Reflect 101", "Default", "Replicate"]

# Read the image without any special processing like changing color channel render.
original_image_buffer = imread(IMAGE_PATH)

"""
    in copyMakeBorder(), you have the following parameters:
    1st -> Buffer,
    2nd -> Top Width in Pixels
    3rd -> Bottom Width in Pixels
    4th -> Left Width in Pixels
    5th -> Right Width in Pixels
    6th -> Border Type

    In border types, there are multiple choices to use.
    # Info were copied from https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_basic_ops/py_basic_ops.html#making-borders-for-images-padding

    (1) BORDER_CONSTANT — Adds a constant colored border.
    (2) BORDER_REFLECT — Border will be mirror reflection of the border elements, like this: fedcba|abcdefgh|hgfedcb
    (3) BORDER_REFLECT_101 — Same as above, but with a slight change, like this: gfedcb|abcdefgh|gfedcba
    (4) BORDER_DEFAULT — Last element is replicated throughout, like this: aaaaaa|abcdefgh|hhhhhhh
    (5) BORDER_REPLICATE — Can’t explain, it will look like this : cdefgh|abcdefgh|abcdefg

    ! The explanation seem to be not enough to show the output. Please run the program instead.

"""

# Please adjust the width of the border with respect to image size, accordingly.

constant_image_buffer = copyMakeBorder(
    original_image_buffer, 20, 20, 20, 20, BORDER_CONSTANT
)
reflect_image_buffer = copyMakeBorder(
    original_image_buffer, 20, 20, 20, 20, BORDER_REFLECT
)
reflect_101_image_buffer = copyMakeBorder(
    original_image_buffer, 20, 20, 20, 20, BORDER_REFLECT_101
)
default_image_buffer = copyMakeBorder(
    original_image_buffer, 20, 20, 20, 20, BORDER_DEFAULT
)
replicate_image_buffer = copyMakeBorder(
    original_image_buffer, 20, 20, 20, 20, BORDER_REPLICATE
)

# Displaying the image in recursion while saving the image as well.

for idx, eachImageBuffers in enumerate(
    [
        constant_image_buffer,
        reflect_image_buffer,
        reflect_101_image_buffer,
        default_image_buffer,
        replicate_image_buffer,
    ]
):
    imshow("%s Border Demo of %s" % (WINDOW_TITLES[idx], IMAGE_PATH), eachImageBuffers)
    imwrite(
        "output_%s_border.png" % WINDOW_TITLES[idx].replace(" ", "_").lower(),
        eachImageBuffers,
    )

if waitKey(0):
    destroyAllWindows()
