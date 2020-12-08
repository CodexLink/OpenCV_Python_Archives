# Merging Two Images with Arithmetic Addition in OpenCV.
# Editted. Credit Source will be published later on.

# Import Certain Used Functions to Reduce Load even on Slightest Bit.
# From the OpenCV library import only imread, addWeighted, imshow, waitKey and destroyAllWindows.
from cv2 import addWeighted, destroyAllWindows, imread, imshow, imwrite, waitKey

# Load Two Images to Script Buffer for Merging Use Later.
image1 = imread("../0_assets/img_1.jpg")
image2 = imread("../0_assets/img_2.jpg")

# addWeighted is a function that merges the two images along with
# weight value for each images (alpha as 2nd arg and beta as 4th arg)
# and adjust the brightness with gamma as 5th arg.

# ! Note: More info on Gamma Here | https://www.pyimagesearch.com/2015/10/05/opencv-gamma-correction/

# What's the metric for Alpha and Beta and Gamma?
# So far, 1 is the highest and 0 is lowers, with adjustment from 0 <= x <= 1, float accepted.

# ! But you can go further than value of 1. Maximum value is not known at this point. (in my experience.)
# * Also gamma is affected by more than 1.
# * The constraint given is just an indicator of what I felt is max weight for each of them.

FIRST_IMAGE_WEIGHT = 0.6
SECOND_IMAGE_WEIGHT = 0.4
OVERALL_BRIGHT_ADJUSTMENT = 0.5

# * For wanting to see a much of a more impact to the result, make either of the alpha or beta has a significant difference of value.

weightedSum = addWeighted(
    image1, FIRST_IMAGE_WEIGHT, image2, SECOND_IMAGE_WEIGHT, OVERALL_BRIGHT_ADJUSTMENT
)

# Show the result buffer as weightedSum to imshow.
imshow(
    "Weighted Result | (Alpha: %0.2f, Beta: %0.2f, Gamma: %0.2f)"
    % (FIRST_IMAGE_WEIGHT, SECOND_IMAGE_WEIGHT, OVERALL_BRIGHT_ADJUSTMENT),
    weightedSum,
)

# Set a Wait Signal for Destroying Windows.
if waitKey(0):
    # Save the result on first-time execution, so that there's no need to excecute the script when looking at the result.
    imwrite("result.jpg", weightedSum)
    destroyAllWindows()
