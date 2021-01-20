#
# This script is most likely correlated from a previous module.
# Please check if this one of the scripts that you want to try.

from os.path import isfile
from subprocess import Popen
from time import sleep
from tkinter import Tk
from tkinter.filedialog import askopenfilename

from cv2 import INTER_AREA, INTER_CUBIC, imread, imwrite, resize

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

# # Main Code
try:

    image_parse = imread(IMAGE_PATH)

    # Print the Image's Width and Height and let the user decides whether use default or its user-defined value.
    print(
        "Keep in note that this script does not utilize Maintaining Aspect Ratio!",
        end="\n\n",
    )

    print("The image %s has the following attributes: " % IMAGE_FILENAME)
    print("Width: %i" % image_parse.shape[1])
    print("Height: %i" % image_parse.shape[0], end="\n\n")

    # * Constants on While Loops
    SIZE_IMAGE_INPUT_NOT_ZERO = 1
    DOES_NOT_CONFIRM_CHANGES_PROPERLY = 1

    while SIZE_IMAGE_INPUT_NOT_ZERO:

        try:
            w_mod_buffer = int(
                input("Please input your resulting width image size (0 to Cancel) |> ")
            )

            if not w_mod_buffer:
                break

            h_mod_buffer = int(
                input("Please input your resulting height image size (0 to Cancel) |> ")
            )

            if not h_mod_buffer:
                break

            while DOES_NOT_CONFIRM_CHANGES_PROPERLY:
                Popen("CLS", shell=True).communicate()

                print(
                    "These are the following attributes from default to resulting image output, continue?",
                    end="\n\n",
                )
                print("Width: %i >>> %i" % (image_parse.shape[1], w_mod_buffer))
                print(
                    "Height: %i >>> %i" % (image_parse.shape[0], h_mod_buffer),
                    end="\n\n",
                )

                try:
                    confirm_buffer = str(input("Confirm | Are you sure? (Y/N) |> "))

                    if confirm_buffer.capitalize() not in ["Y", "N"]:
                        print("User inputted a wrong choice! Please try again!")
                        sleep(1.5)
                        continue

                    if confirm_buffer.capitalize() in ["N"]:
                        break

                    Popen("CLS", shell=True).communicate()

                    # ! Interpolation Decision
                    # If the width and height input of the image is lower than the original then use INTER_AREA.
                    # Or else use INTER_CUBIC.

                    interpolation_choice = (
                        INTER_AREA
                        if image_parse.shape[1] < w_mod_buffer
                        or image_parse.shape[0] < h_mod_buffer
                        else INTER_CUBIC
                    )

                    resize_buffer = resize(
                        image_parse,
                        (w_mod_buffer, h_mod_buffer),
                        interpolation=interpolation_choice,
                    )
                    imwrite("result.png", resize_buffer)
                    print(
                        "The file will be saved as result.png from where the script was stored!", end="\n\n"
                    )
                    exit(0)

                except ValueError:
                    print("User inputted is not a string! Please try again.")
                    sleep(1.5)
                    continue

        except ValueError:
            print("User Inputted is not an Integer! Please try again!")
            sleep(1.5)
            continue

        break


except IOError as TechErr:
    raise SystemError(
        "Error: Cannot detect the file or went missing after selection. Please try again later."
        % TechErr
    )

finally:
    raise SystemExit("Script Terminated Gracefully.")
