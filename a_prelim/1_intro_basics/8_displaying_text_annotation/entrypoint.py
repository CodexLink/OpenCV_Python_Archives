# From the OpenCV library import imread, imwrite, putText and FONT_HERSHEY_SIMPLEX function only.
from cv2 import imread, imwrite, putText, FONT_HERSHEY_SIMPLEX

# Reading the image using imread() function
image = imread("../0_assets/road.jpg")

# // We are copying the original image,
# // as it is an in-place operation.
# output = image.copy()
# ! As of opencv-python==4.4.0.46 (not sure for onwards).
# ! It is now possible to use the variable who holds imread function return buffer.

# Adding the text using putText() function from an image canvas.
"""
    To be understand rectangle function. You have to know that parameters are the following:
    1. Image Buffer
    2. Text To Paste on Image Buffer
    3. Coordinates in Pixel from where to put Text at. (Beginning)
    4. Font Scale (Similar on how Image Scaling Works (?))
    5. BGR Color of the Font.
    5. Font Thiccness. (Here in this case, 8 px wide)
"""

text = putText(
    image, "OpenCV Demo", (500, 550), FONT_HERSHEY_SIMPLEX, 4, (255, 0, 0), 8
)

# Write the text buffer to a new file called "result.jpg".
imwrite("result.jpg", text)
