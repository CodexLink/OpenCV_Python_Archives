from os import getcwd, path  # For File Access
from subprocess import Popen  # os.system("CLS") equivalent.
from time import sleep  # for timeout. Just like delay() in Arduino.
from typing import (
    Final,
)  # Type Hinting, for Strict Return Hinting Process for Standardization.
from shutil import copy as copy_file  # For File Copying from SRC to DEST.
from cv2 import imread, imshow, destroyAllWindows, waitKey


class AssignmentHandler(object):
    def __init__(self, stored_filename: str, stored_filename_ext: str) -> None:

        # Pre-Initialization, Clear the terminal first.
        Popen("CLS", shell=True).communicate()

        # ! Attributes (Inlined, Less Hassle on Script instead of seperate file)

        # Filename and Extension for Image Target of the Script.
        self.stored_image_name: Final = (
            "test" if not stored_filename else stored_filename
        )
        self.stored_image_ext: Final = (
            "jpg" if not stored_filename_ext else stored_filename_ext
        )

        self.choice_buffer: int = 0  # Buffer for display_options(), Initially 0. Will Wait for Input Before Running Function.
        self.file_path_buffer: str = ""  # Buffer String for InInitially None, Will Wait for Input Before Processing.
        self.function_ret_output: int = (
            0  # Initially None, will change according to function return code.
        )
        self.inserted_file_is_valid: bool = False

        # ! Constraints
        # Checks for Parameter Values first before Initialization of the Class.

        # * Constraint | Check for Parameter 'stored_filename_ext' should be truthy to 'self.acceptable_image_exts'.
        self.acceptable_image_exts: Final = ("jpg", "jpeg", "png")

        if not stored_filename_ext in self.acceptable_image_exts:
            raise SystemExit(
                "Extension supplied is not allowed! Use (%s, %s, %s) files instead."
                % self.acceptable_image_exts
            )

        # * Contraint | Check for `stored_filename` should be truthy to type(str).
        if not isinstance(stored_filename, str):
            raise SystemExit(
                "Filename should be or atleast contain a %s and not purely made of %s!"
                % (str, type(stored_filename))
            )

        # # Constants
        self.DISPLAY_OPTIONS: Final = [
            "Store or Override an Image by Inputting File Path.",  # Option #1
            "Display Stored Image from the Script.",  # Option #2
            "Exit Script",  # Option #3
        ]

        # This is based from self.DISPLAY_OPTIONS. Adjust accordingly with respect to the index position.
        self.STORE_IMAGE: Final = 1
        self.DISPLAY_STORED_IMAGE: Final = 2
        self.EXIT_SCRIPT: Final = 3

        # File Path Handlers
        self.CURRENT_PATH = (
            getcwd()
        )  # Initially None, but will be constant virtually after some parts of runtime.
        # * self.CURRENT_PATH_IMG_FILE is just a directory form of the target image.
        self.CURRENT_PATH_IMG_FILE = (
            self.CURRENT_PATH
            + "/"
            + self.stored_image_name
            + "."
            + self.stored_image_ext
        )

    # # Functions
    # * Each functions should return bool to better handle exceptions on __name__ driver part of this code.

    # ! No need to invoke or put the arguments inside of this function. Refer to the variable instead.
    # * Returns bool, False for doing nothing, True for re-running this function.

    def display_options(self: object) -> bool:
        Popen("CLS", shell=True).communicate()
        self.inserted_file_is_valid = path.isfile(self.CURRENT_PATH_IMG_FILE)

        # Output if the Script contains the image already via lambda function.
        print(
            "Script Has The Image? : %s"
            % (
                "Yes, Can Override the Stored Image."
                if self.inserted_file_is_valid
                else "No, Please Input an Image Path To Store."
            ),
            end="\n\n",
        )

        # Output Choices.
        for idxOption, eachOption in enumerate(self.DISPLAY_OPTIONS):
            print("%i.) %s" % (idxOption + 1, eachOption))

        # Wait for the Choice. Strict Checking After Choice Type.
        try:
            self.choice_buffer = int(input("\nChoose your option |> "))
        except ValueError:
            print("\nYour choice is not a number! Please try again.")
            sleep(1)
            return 1

        # Run the function according to the choices.
        if self.choice_buffer == self.STORE_IMAGE:
            self.input_or_overwrite_image()
            return 1

        elif self.choice_buffer == self.DISPLAY_STORED_IMAGE:
            self.display_image()
            return 1

        elif self.choice_buffer == self.EXIT_SCRIPT:
            return 0

        else:
            print("\nYour choice is invalid! Please try again.")
            sleep(1)
            return 1

    def input_or_overwrite_image(self: object) -> bool:
        while 1:
            file_buffer_path = str(
                input(
                    "\nInput your File Path with Extensions to Store, type 0 to cancel |> "
                )
            )

            if file_buffer_path == "0":
                break

            else:
                is_file = path.isfile(file_buffer_path) and file_buffer_path.endswith(
                    self.acceptable_image_exts
                )
                if is_file:
                    # Copy the Image from src to this script.
                    file_buffer_path = copy_file(
                        file_buffer_path, self.CURRENT_PATH_IMG_FILE
                    )
                    return True

                else:
                    # Print Message and iterate here again.
                    print("The file path you give is not valid. Please try again...")
                    sleep(1)

    def display_image(self: object) -> bool:
        if self.inserted_file_is_valid:
            # Check the image.
            image_disp_buf = imread(self.CURRENT_PATH_IMG_FILE)
            print("Reading %s file..." % self.CURRENT_PATH_IMG_FILE)

            imshow(
                "Image Display for %s"
                % (self.stored_image_name + "." + self.stored_image_ext),
                image_disp_buf,
            )

            # Add Wait Signal (as Blocking to Main Thread) To Terminate Window on Focus.
            waitKey(0)  # 0 as in Indefinite Time before termination.
            # Call destroyAllWindows after detecting any key based on waitKey signal.
            destroyAllWindows()

            print("Image Display Terminated. Wait for 1 Second...")
            sleep(1)
            return True

        else:
            print(
                "\nFile %s does not exists! Please input an image first!"
                % (self.CURRENT_PATH_IMG_FILE)
            )
            sleep(1)
            return True


LOOP_ENDLESSLY = 1  # Constant Annotation on While Loop inside Driver.

if __name__ == "__main__":
    handler = AssignmentHandler("image", "jpg")
    while LOOP_ENDLESSLY:
        if not handler.display_options():
            break

    raise SystemExit("The script has finished executing.\n")

raise SystemError("Cannot import this module from another script.\n")
