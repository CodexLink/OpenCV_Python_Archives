from os.path import isfile
from subprocess import Popen
from time import sleep
from tkinter import Tk
from tkinter.filedialog import askopenfilename

from cv2 import imread, imwrite, warpAffine
from numpy import float32


Popen("CLS", shell=True).communicate()
sleep(0.5)

print("Please insert an image reference through file manager...", end="\n\n")
print(
    "Can't see the file manager? Please ALT+TAB and look out for a spawned window of file manager."
)


# Get File Path with File Manager Section

# ! File Manager Context Constants
FILE_TYPES = [("Image Files (.jpeg .jpg .png)", ".jpeg .jpg .png")]
DEFAULT_EXT = ".jpg"

# Everytime we use the Tk associate classes, a small window will be spawned.
# We have to withdraw it or hide it everytime we use its associate functions.

root = Tk()
root.attributes("-topmost", True)
root.withdraw()

IMAGE_PATH = askopenfilename(
    title="Load an Image...", defaultextension=DEFAULT_EXT, filetypes=FILE_TYPES
)

# * Split the image path with '/' delimeter.
# ! And get the last slice by reverse and add 0th index to get the literal string.
IMAGE_FILENAME = IMAGE_PATH.split("/")[-1:][0]

# Evaluate by Determining the Length instead of truthy condition.
if not isfile(IMAGE_PATH):
    raise SystemExit("No image file was provided by the user. Please try again.")

try:
    # ! Creating a Translation Matrix.
    # # According to https://towardsdatascience.com/transformations-with-opencv-ff9a7bea7f8b.

    # * matrix = | size, rotation, position | (of x axis)
    # *          | rotation, size, position | (of y axis)

    # ! Keep in note that...
    # * You have to have a 2x3 matrix representing the following cols and rows.
    # * Getting further or getting less than 2x3 will result in error, as the matrix given on the above
    # * is what it is and is considered cols and rows as parameter of the image from a function.
    # * The pixel position of x and y must respect the size of the image, or you will get an error.
    # * Size metric is in scale ratio. 1 is normal, 2 is double, 0.5 is half of original size.
    # * Rotation metric is in angle metric. Manipulation of Angles will result of distorted image.

    # The matrix can be encapsulated with any float function associated in numpy. In this script
    # we used float32 for precision when the user gave float values.

    M = float32([[0.5, 0, 100], [0, 0.5, 50]])

    print(M)

    # Read image from disk.
    img = imread(IMAGE_PATH)
    (rows, cols) = img.shape[:2]

    # warpAffine does appropriate shifting given the
    # translation matrix.
    res = warpAffine(img, M, (cols, rows))

    # Write image back to disk.
    imwrite('result.jpg', res)

except IOError as TechErr:
    raise SystemError(
        "Error: Cannot detect the file or went missing after selection. Please try again later."
        % TechErr
    )

finally:
    raise SystemExit("Script Terminated Gracefully.")
