#!python

## Blood Detection Made by Group 5 Machine Perception (CPE102)

"""
* Leader:       Janrey T. Licas (Creator, github.com/CodexLink)
* Members:      Diaz, Adrian Gabriel
* 	            Imperial, Justine O.
* 	            Jantoc, Janos Angelo G.
* 	            Langaoan, Ronald
"""
from os.path import isfile
from subprocess import Popen
from time import sleep
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from typing import Final, NewType, Text, Tuple

from cv2 import (
    COLOR_BGR2GRAY,
    HOUGH_GRADIENT,
    GaussianBlur,
    HoughCircles,
    circle,
    createCLAHE,
    cvtColor,
    destroyAllWindows,
    equalizeHist,
    imread,
    imshow,
    imwrite,
    medianBlur,
    rectangle,
    waitKey,
    namedWindow,
    WINDOW_NORMAL
)
from numpy import ndarray, round

# Constant Variables
FILE_TYPES: Final = [("Image Files (.jpeg .jpg .png)", ".jpeg .jpg .png")]
DEFAULT_EXT: Final = ".jpg"
FILE_DIALOG_TITLE: Final = "Load an Image File To Process..."
SCRIPT_ON_EXECUTION_STATE: Final = True

# Static Typing Variables
ImageBuffer: Final = NewType("ImageBuffer", ndarray)


class DetectionAssignment(object):
    def __init__(self, **kwargs: dict) -> None:
        window = Tk()
        window.attributes("-topmost", True)
        window.withdraw()

    def entrypoint(self: object) -> None:
        while SCRIPT_ON_EXECUTION_STATE:
            Popen("CLS", shell=True).communicate()
            print(
                "Blood Sample Count based from Image\nCreated by Group 5 of Machine Perception.",
                end="\n\n",
            )
            print(
                "Wait for the File Manager / File Explorer To Open. And select an image file...",
            )
            image_path = askopenfilename(
                title=FILE_DIALOG_TITLE,
                defaultextension=DEFAULT_EXT,
                filetypes=FILE_TYPES,
            )

            if not isfile(image_path) or not len(image_path):
                return 0

            print("File is Valid. Processing the Image...", end="\n\n")

            enhancement_buffer = self.image_enhancement(image_path)
            result_buffer = self.image_process(enhancement_buffer)

            if not self.post_process_prompt(result_buffer):
                break

            continue

    # * Step 1
    # No parameters can be given from this function! Please modify the definition accordingly.
    def image_enhancement(self, img_path: Text) -> ImageBuffer:
        print("Enhancement | Step 0 | Original Image Reading to Numpy Array.")
        img_buffer = imread(img_path)

        # Create a copy, to be passed on the other function.
        original_buffer = imread(img_path)

        print("Enhancement | Step 1 | Grayscale")
        img_buffer = cvtColor(img_buffer, COLOR_BGR2GRAY)

        print("Enhancement | Step 2 | Blurring with Median and Gausian")
        img_buffer = medianBlur(img_buffer, 3)
        img_buffer = GaussianBlur(img_buffer, (7, 7), 0)

        print("Enhancement | Step 3 | Histogram Equalization")
        img_buffer = equalizeHist(img_buffer)

        print("Enhancement | Step 4 | CLAHE Implementation")
        clahe_buffer = createCLAHE(clipLimit=1.5, tileGridSize=(8, 8))
        clahe_apply_buffer = clahe_buffer.apply(img_buffer)

        print("\nEnhancement | Finished...", end="\n\n")

        return original_buffer, clahe_apply_buffer

    # * Step 2
    def image_process(
        self: object, image_buffers: Tuple[ImageBuffer, ImageBuffer]
    ) -> ImageBuffer:
        # Block-Level State Variable
        rbc_count: int = 0

        # @info - The Circle Algo Buffer (HoughCircles) requires to be dynamic in order to
        # ! detect circle at particular size. The image will also be the dependent of the output here.

        # * Samples Parameter Configuration.
        # ! The following algorithm must have a set of values for each sample.
        # * This means that we have to do this dynamically by training a model to determine a particular parameters.

        # @info - Keep in mind that the configurations per samples are not entirely accurate but acceptable.
        # * The following wont start unless any configuration have been uncommented.

        # ! The Configuration Change starts after HOUGH_GRADIENT Parameter.
        circle_algo_buffer = HoughCircles(
            image_buffers[1],  # 1st Index is Enhanced Image Buffer
            HOUGH_GRADIENT,
            # # * For Sample_1
            # 1.3510, # dp as ratioReso
            # 15, # mindist as minDistance
            # param1=45, # param1 as cannyMax
            # param2=22, # param2 as cannyMin
            # minRadius=5,
            # maxRadius=12,
            # * For Sample_2
            # 1.3510, # dp as ratioReso
            # 15, # mindist as minDistance
            # param1=45, # param1 as cannyMax
            # param2=20, # param2 as cannyMin
            # minRadius=5,
            # maxRadius=12,
            # * For Sample_3
            1, # dp as ratioReso
            20, # mindist as minDistance
            param1=75, # param1 as cannyMax
            param2=25, # param2 as cannyMin
            minRadius=15,
            maxRadius=35,

        )

        print("Processing | Step 0 | Detection...")

        if circle_algo_buffer is None:
            raise SystemError(
                "The function `image_process()` expects the buffer to be a type ImageBuffer with context! Please debug this before trying again."
            )

        detected_rbc_context = round(circle_algo_buffer[0, :]).astype("int")

        for (x, y, r) in detected_rbc_context:
            circle(image_buffers[0], (x, y), r, (255, 255, 0), 2)
            rectangle(
                image_buffers[0],  # 0th Index is Original Image Buffer
                (x - 2, y - 2),
                (x + 2, y + 2),
                (255, 128, 255),
                -1,
            )
            rbc_count += 1

        print(
            "Image Processing Finished. Please close the window to remove blocking from the script.", end="\n\n"
        )
        namedWindow(f"Blood Sample Output | Red Blood Cell Count is {rbc_count} | Unstable", WINDOW_NORMAL)
        imshow(
            f"Blood Sample Output | Red Blood Cell Count is {rbc_count} | Unstable",
            image_buffers[0],
        )
        waitKey(0)
        destroyAllWindows()

        return image_buffers[
            1
        ]  # Returns Enhanced Final Image (With Circle Annotation from HoughCircles)

    # * Post-Step
    def post_process_prompt(self, result_image_buffer: ImageBuffer) -> bool:

        try:
            prompt_1 = str(
                input("Do you want to save the modification result? (Y/[N]) > ")
            )

            if prompt_1 in ("Y", "y"):
                print("Result | Saved as final_result.png from ", end="\n\n")
                imwrite("final_result.png", result_image_buffer)

        except ValueError:
            print("Value given is not one of the choices. Default to N Choice.")

        try:
            prompt_2 = str(input("Do you want to re-run this script again? (Y/[N]) > "))

            return True if prompt_2 in ("Y", "y") else False

        except ValueError:
            print("Value given is not one of the choices. Default to N Choice.")
            return False


if __name__ == "__main__":
    inst = DetectionAssignment().entrypoint()

    # ! Once done, raise SystemExit no matter what it takes.
    print(f"Operation Finished. Thank you!"), sleep(2)
    raise SystemExit(0)

raise ImportError("You cannot import this file to other examples!")
