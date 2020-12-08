# From OpenCV Library, import only bitwise_and, bitwise_or, bitwise_xor, destroyAllWindows, imread, imshow, imwrite and waitKey.
from cv2 import (
    bitwise_and,
    bitwise_not,
    bitwise_or,
    bitwise_xor,
    destroyAllWindows,
    imread,
    imshow,
    imwrite,
    waitKey,
)

# Path to Images were seperated to be referenced on Window Display.
IMAGE_PATH_1 = "../0_assets/img_5.png"
IMAGE_PATH_2 = "../0_assets/img_6.png"

image1 = imread(IMAGE_PATH_1)
image2 = imread(IMAGE_PATH_2)

# Apply bitwise_and or bitwise_or or bitwise_xor from the two image based on pixel of the two image.

"""
    How does it work?
    First, you have to understand how AND OR and XOR operators in Logic.
    Every pixel of the two image were compared at each other with respect to their sizes.

    ! Keep note that the two image should be in the same size or will receive the following error!

    # opencv\modules\core\src\arithm.cpp:669: error: (-209:Sizes of input arguments do not match) The
    # operation is neither 'array op array' (where arrays have the same size and the same number of channels),
    # nor 'array op scalar', nor 'scalar op array' in function 'cv::arithm_op'.

    # # Also keep in mind that, shifting their location parameter may produce different results. (Means of shifting image1 and image2 arguments)
"""

bitwise_and_buffer = bitwise_and(image2, image1, mask=None)  # For Bitwise AND
bitwise_or_buffer = bitwise_or(image2, image1, mask=None)  # For Bitwise OR
bitwise_xor_buffer = bitwise_xor(image2, image1, mask=None)  # For Bitwise XOR
bitwise_not_buffer_1 = bitwise_not(image1, mask=None)  # For Bitwise XOR
bitwise_not_buffer_2 = bitwise_not(image2, mask=None)  # For Bitwise XOR

# Display all bitwise buffers with imshow function.
# ! The following 3 imshow functions spawns 5 windows, atleast.
# ! Pressing any key will close 5 of them (on any spawned focused window).

imshow(
    "Bitwise AND Operators on %s and %s" % (IMAGE_PATH_1, IMAGE_PATH_2),
    bitwise_and_buffer,
)
imshow(
    "Bitwise OR Operators on %s and %s" % (IMAGE_PATH_1, IMAGE_PATH_2),
    bitwise_or_buffer,
)
imshow(
    "Bitwise XOR Operators on %s and %s" % (IMAGE_PATH_1, IMAGE_PATH_2),
    bitwise_xor_buffer,
)
imshow(
    "Bitwise NOT #1 Operators on %s" % IMAGE_PATH_1,
    bitwise_not_buffer_1,
)
imshow(
    "Bitwise NOT #2 Operators on %s" % IMAGE_PATH_2,
    bitwise_not_buffer_2,
)

# Set a Wait Signal for Destroying Windows.
if waitKey(0):
    # Save the results on first-time execution, so that there's no need to excecute the script when looking at the result.
    imwrite("result_and.png", bitwise_and_buffer)
    imwrite("result_or.png", bitwise_or_buffer)
    imwrite("result_xor.png", bitwise_xor_buffer)
    imwrite("result_not_1.png", bitwise_not_buffer_1)
    imwrite("result_not_2.png", bitwise_not_buffer_2)
    destroyAllWindows()
