# Subtracting Two Images with Arithmetic Subtraction in OpenCV.
# Editted. Credit Source will be published later on.

# From OpenCV Library, import only imread, subtract, imshow, waitKey and destroyAllWindows.
from cv2 import destroyAllWindows, imread, imshow, imwrite, subtract, waitKey

# Image paths were seperated to be referenced on the Window Title.
IMAGE_PATH_1 = "../0_assets/img_3.jpg"
IMAGE_PATH_2 = "../0_assets/img_4.jpg"

image1 = imread(IMAGE_PATH_1)
image2 = imread(IMAGE_PATH_2)

# Apply Subtraction from two images via subtract function, with buffer to be saved in variable called `sub`.
"""
    ! Keep note that the two image should be in the same size or will receive the following error!

    # opencv\modules\core\src\arithm.cpp:669: error: (-209:Sizes of input arguments do not match) The
    # operation is neither 'array op array' (where arrays have the same size and the same number of channels),
    # nor 'array op scalar', nor 'scalar op array' in function 'cv::arithm_op'.
"""
sub = subtract(image1, image2)

# Show the result buffer from sub with Window Titles referencing to IMAGE_PATH_1 and IMAGE_PATH_2.
imshow("Image Subtraction from %s, based to %s" % (IMAGE_PATH_1, IMAGE_PATH_2), sub)

# Set a Wait Signal for Destroying Windows.
if waitKey(0):
    # Save the result on first-time execution, so that there's no need to excecute the script when looking at the result.
    imwrite("result.jpg", sub)
    destroyAllWindows()
