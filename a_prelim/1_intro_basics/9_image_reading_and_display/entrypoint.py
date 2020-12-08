# From the OpenCV library import imread imshow, waitKey, destroyAllWindows, imwrite and destroyAllWindows.
from cv2 import imread, imshow, waitKey, destroyAllWindows, imwrite, destroyAllWindows

# Open the Image with Greyscale Color Channel.
IMAGE_PATH = "messi.png"
img = imread(IMAGE_PATH, 0)

# Show the image with filename of it.
imshow('Preview of %s in Greyscale' % IMAGE_PATH, img)

# This function waits for any key indefinitely but because of bitwise AND operator,
# we wait for a particular key. But it doesn't work in this case.
k = waitKey(0) & 0xFF

# wait for ESC key or any key except S key to exit.
if k == 27:
    destroyAllWindows()

# wait for 's' key to save and exit.
elif k == ord('s'):
    imwrite('messigray.png',img)
    destroyAllWindows()
