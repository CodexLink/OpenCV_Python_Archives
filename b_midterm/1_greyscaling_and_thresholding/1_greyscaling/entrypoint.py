from os.path import isfile
from subprocess import Popen
from time import sleep
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# # From the OpenCV Library, import only the following.
from cv2 import (
    COLOR_BGR2GRAY,
    WINDOW_NORMAL,
    cvtColor,
    destroyAllWindows,
    imread,
    imshow,
    imwrite,
    namedWindow,
    waitKey,
)

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

# Evaluate by Determining the Length instead of truthy condition.
if not isfile(IMAGE_PATH):
    raise SystemExit("No image file was provided by the user. Please try again.")

# Load Approach Selection Section
# * The user will have two choices...
# * (1) Load with imread() with color channel 0 being only loaded.
# * (2) Load with cvtColor() with COLOR_BGR2GRAY parameter.

# Constants for the Menu.
GREY_COLOR_CHANNEL = 0
LOOP_MENU_ENDLESSLY = 1
LOAD_IMAGE_WITH_IMREAD = 1
LOAD_IMAGE_WITH_CVTCOLOR = 2
ABORT_OPERATION = 3


while LOOP_MENU_ENDLESSLY:
    Popen("CLS", shell=True).communicate()
    print("You can greyscale the image with the following approaches...", end="\n\n")
    print("(1) Load Image with imread() with Color Channel 0.")
    print("(2) Load Image with cvtColor() with COLOR_BGR2GRAY Parameter.")
    print("(3) Abort Operation.", end="\n\n")

    try:
        choice_buffer = int(input("Select an Option |> "))

        if not choice_buffer in range(1, 4):
            print("Your choice is out-of-bounds! Please try again.")
            sleep(1)
            continue

        # Combined for Joint Pathway Function for Saving the Image.
        if choice_buffer in [LOAD_IMAGE_WITH_IMREAD, LOAD_IMAGE_WITH_CVTCOLOR]:

            # Declare image buffer for use of the if and else statement to be referred in the imwrite() function.
            greyscale_image_buffer = None

            if choice_buffer == LOAD_IMAGE_WITH_IMREAD:
                print(
                    "Displaying Image Buffer with Greyscaling (With Color Channel 0)... [Resizable]",
                    end="\n\n",
                )
                greyscale_image_buffer = imread(IMAGE_PATH, GREY_COLOR_CHANNEL)

            # We are sure that the otherwise value of choice_buffer is LOAD_IMAGE_WITH_CVTCOLOR and nothing else.
            else:
                print(
                    "Displaying Image Buffer with Greyscaling (using CvtColor with COLOR_BGR2GRAY). [Resizable]"
                )
                original_image_buffer = imread(IMAGE_PATH)
                greyscale_image_buffer = cvtColor(original_image_buffer, COLOR_BGR2GRAY)

            # ! I don't know why we cannot put namedWindow result to a Variable because this method is too redundant.
            # * But it works either way.
            namedWindow(
                "Image Rendered with "
                + (
                    "imshow() function with Color Channel 0"
                    if choice_buffer == LOAD_IMAGE_WITH_IMREAD
                    else "cvtColor (using COLOR_BGR2GRAY)"
                ),
                WINDOW_NORMAL,
            )
            imshow(
                "Image Rendered with "
                + (
                    "imshow() function with Color Channel 0"
                    if choice_buffer == LOAD_IMAGE_WITH_IMREAD
                    else "cvtColor (using COLOR_BGR2GRAY)"
                ),
                greyscale_image_buffer,
            )

            waitKey(0)  # Wait for any key press while waiting indefinitely.

            destroyAllWindows()  # Once we passed through waitKey() [a blocking function], then de-allocate all window buffers that is displayed with the image.

            # Assume this is the finally version of if and else.
            # Do not ask for save file confirmation but rather save it and notify the user that there is a new file saved under this script.
            imwrite(
                "result_%s.png"
                % ("imread" if choice_buffer == LOAD_IMAGE_WITH_IMREAD else "cvtColor"),
                greyscale_image_buffer,
            )
            print(
                "The greyscale buffer image was automatically saved as 'result_%s.png' for quick inspection of the result and for future case."
                % ("imread" if choice_buffer == LOAD_IMAGE_WITH_IMREAD else "cvtColor")
            )
            sleep(2)

        elif choice_buffer == ABORT_OPERATION:
            raise SystemExit("Script Operation Aborted. Thank you for trying the demo!")

        else:
            print("An unknown condition has occured. Please try again.")
            sleep(1)
            continue

    except ValueError:
        print("Your choice is not an integer! Please try again.")
        sleep(1)
        continue
