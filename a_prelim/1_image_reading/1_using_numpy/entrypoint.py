# Python code to reading an image using OpenCV
import numpy as np
from cv2 import imread, imshow, waitKey, destroyAllWindows, imwrite, destroyAllWindows
# You can give path to the
# image as first argument

img = imread('../0_assets/messi.png', 0)

# will show the image in a window
imshow('image', img)

k = waitKey(0) & 0xFF

# wait for ESC key to exit
if k == 27:
    destroyAllWindows()

# wait for 's' key to save and exit
elif k == ord('s'):
    try:
        imwrite('messigray.png',img)
        destroyAllWindows()
    except BaseException as Error:
        print(Error)