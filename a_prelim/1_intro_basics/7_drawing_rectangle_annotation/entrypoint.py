# From the OpenCV library import imread, imwrite and rectangle function only.
from cv2 import imread, imwrite, rectangle

# Reading the image using imread() function
image = imread("../0_assets/road.jpg")

# // We are copying the original image,
# // as it is an in-place operation.
# output = image.copy()
# ! As of opencv-python==4.4.0.46 (not sure for onwards).
# ! It is now possible to use the variable who holds imread function return buffer.

# Using the rectangle() function to create a rectangle from an image canvas.
"""
    To be understand rectangle function. You have to know that parameters are the following:
    1. Image Buffer
    2. Point 1 and 2 (contains both pixel)
    3. Point 3 and 4 (contains both pixel)
    4. Color of Rectangle (in BGR Form)
    5. Rectangle Outline Thiccness. (Here in this case, 4 px wide)
"""

rect = rectangle(image, (1500, 900), (600, 400), (255, 64, 128), 4)

# Write the rect buffer to a new file called "result.jpg".
imwrite("result.jpg", rect)
