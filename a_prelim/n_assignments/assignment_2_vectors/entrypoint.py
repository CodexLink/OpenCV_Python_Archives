from os import getcwd, path  # For File Access
from subprocess import Popen  # os.system("CLS") equivalent.
from time import sleep  # for timeout. Just like delay() in Arduino.
from typing import (
    Final,
)  # Type Hinting, for Strict Return Hinting Process for Standardization.
from shutil import copy as copy_file  # For File Copying from SRC to DEST.
from cv2 import imread, imshow, destroyAllWindows, waitKey
from tkinter import filedialog,

class VectorAssignmentClass(object):
    def __init__(self, filename: str, filename_extension: str) -> None:

        # Pre-Initialization, Clear the terminal first.
        Popen("CLS", shell=True).communicate()

        # ! Constraints
        # The constraints must be passed before initialization all attributes that will be used inside.

        # * Constraint | Check for Parameter 'filename_extension' should be truthy to 'self.acceptable_image_exts'.
        self.acceptable_image_exts: Final = ("jpg", "jpeg", "png")

        if not filename_extension in self.acceptable_image_exts:
            raise SystemExit(
                "Extension supplied is not allowed! Use (%s, %s, %s) files instead."
                % self.acceptable_image_exts
            )

        # * Contraint | Check for `filename` should be truthy to type(str).
        if not isinstance(filename, str):
            raise SystemExit(
                "Filename should be or atleast %s and not made of %s!"
                % (str, type(filename))
            )

        # # Constants

        self.FEATURE_DISPLAY_STRS: Final = {
            "BASE_OPTION_1": {
                "BASE_NAME": "Store a Valid Image File Path to the Script.",
                "DESCRIPTION": "Please provide a file path in absolute form (recommended) or relative form. The script won't make a copy of the image but rather take the reference via file path.",
            },
            "BASE_OPTION_2": "Display Inserted Image or Last Known Operation Result.",
            "BASE_OPTION_3": {
                "BASE_NAME": "Apply Blurring to Image (with Interpolations)",
                "DESCRIPTION": "When it comes blurring an object, there are some multiple approaches",
                "OPTION_1": "Apply Blur with Gaussian Interpolation",
                "OPTION_2": "Apply Blur with Median Interpolation",
                "OPTION_3": "Apply Blur with Bilateral Interpolation",
                "OPTIONALS" : {
                    "RETAIN_ASPECT_RATIO": "Resize with Aspect Ratio",
                    "DO_NOT_RETAIN_ASPECT_RATIO": "Do not resize with Aspect Ratio",
                }
            },
            "BASE_OPTION_4": {
                "BASE_NAME": "Apply Enlargement or Shrinking to Image (with Interpolations)",
                "DESCRIPTION": """
                    When it comes resizing an object, there are some multiple approaches
                """,
                "OPTION_1": "Apply Resize with INTER_LINEAR Interpolation",
                "OPTION_2": "Apply Resize with INTER_AREA Interpolation",
                "OPTION_3": "Apply Resize with INTER_CUBIC Interpolation",
                "OPTION_4": "Apply Resize with INTER_NEAREST Interpolation",
                "OPTION_5": "Apply Resize with INTER_LANCZOS4 Interpolation",
            },
            "BASE_OPTION_5": "Terminate Script",
            "WRITE_IMAGE_OPTIONS": {
                "OVERRIDE_RESULT": "Override the Result",
                "NEW_RESULT": "Create A New Result based from Image Path",
            },
        }

        # !! This is based from self.FEATURE_DISPLAY_STRS. Adjust accordingly with respect to the index position.
        self.STORE_IMAGE_PATH: Final = 1
        self.DISPLAY_RESULT: Final = 2
        self.APPLY_BLUR: Final = 3
        self.APPLY_RESIZE: Final = 4
        self.EXIT_SCRIPT: Final = 5

        self.GAUSSIAN_OPTION : Final = 1
        self.MEDIAN_OPTION : Final = 2
        self.BILATERAL_OPTION : Final = 3

        self.file_image_result_metadata: Final = {
            "FILE_NAME": "result" if not filename else filename,
            "FILE_EXTENSION": "png" if not filename_extension else filename_extension,
        }

        # * self.CURRENT_PATH_IMG_FILE is just a directory form of the target image.
        self.CURRENT_PATH_IMG_FILE = (
            getcwd()
            + "/"
            + self.file_image_result_metadata["FILE_NAME"].lower()
            + "."
            + self.file_image_result_metadata["FILE_EXTENSION"].lower()
        )

        # ! Attributes (Inlined, Less Hassle on Script instead of seperate file)
        # Filename and Extension for Image Target of the Script.

        self.input_buffers = {
            "display_choices": 0,  # Buffer for All Choices in Number.
            "valid_file_image_path": "",  # Buffer Strings for Valid File Path.
        }

        self.result_payload_exists: bool = path.isfile(
            self.CURRENT_PATH_IMG_FILE
        )  # For Stateful File Image Validation Storage.

    # # Functions
    # * Each functions should return bool to better handle exceptions on __name__ driver part of this code.

    def display_options(self: object) -> bool:
        Popen("CLS", shell=True).communicate()

        print(self.result_payload_exists)

        print(  # Output if the Script has valid image file path.
            "Script Has Image Path? : %s"
            % (
                "Yes, File Path Override is Allowed."
                if path.isfile(self.input_buffers["valid_file_image_path"])
                else "No, Please Input an Image Path."
            ),
            end="\n\n",
        )

        # Output Choices.
        for eachIndex in range(0, 5):
            option_name = None
            try:
                option_name = self.FEATURE_DISPLAY_STRS[
                    "BASE_OPTION_%i" % (eachIndex + 1)
                ]["BASE_NAME"]

            except (KeyError, TypeError):
                option_name = self.FEATURE_DISPLAY_STRS[
                    "BASE_OPTION_%i" % (eachIndex + 1)
                ]

            finally:
                print("%i.) %s" % (eachIndex + 1, option_name))

        # Wait for the Choice. Strict Checking After Choice Type.
        try:
            self.input_buffers["display_choices"] = int(
                input("\nChoose your option |> ")
            )

        except ValueError:
            print("\nYour choice is not a number! Please try again.")
            sleep(1)
            return True

        # Run the function according to the choices.
        if self.input_buffers["display_choices"] == self.STORE_IMAGE_PATH:
            self.store_or_override_image_path()
            return True

        elif self.input_buffers["display_choices"] == self.DISPLAY_RESULT:
            self.display_result_output()
            return True

        elif self.input_buffers["display_choices"] == self.APPLY_BLUR:
            self.apply_blur_effect_on_image()
            return True

        elif self.input_buffers["display_choices"] == self.APPLY_RESIZE:
            self.apply_resize_on_image()
            return True

        elif self.input_buffers["display_choices"] == self.EXIT_SCRIPT:
            return False

        else:
            print("\nYour choice is invalid! Please try again.")
            sleep(1)
            return True

    def store_or_override_image_path(self: object) -> bool:
        while 1:
            file_buffer_path = str(
                input(
                    "\n%s\n\nInput the path or type '0' (zero) to cancel |> "
                    % self.FEATURE_DISPLAY_STRS["BASE_OPTION_1"]["DESCRIPTION"]
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
                    self.input_buffers["valid_file_image_path"] = file_buffer_path
                    print(
                        "The file path %s is a valid image file. Success!!!"
                        % file_buffer_path
                    )
                    sleep(1.5)
                    break

                else:
                    # Print Message and iterate here again.
                    print(
                        "The file path you supplied is not a valid image file. Please try again..."
                    )
                    sleep(1.5)

    def display_result_output(self: object) -> None:
        image_buffer = (
            self.CURRENT_PATH_IMG_FILE
            if self.result_payload_exists
            else self.input_buffers["valid_file_image_path"]
        )
        try:

            # Check the image based on given path.
            image_disp_buf = imread(image_buffer)

            imshow("Image Display | %s" % image_buffer, image_disp_buf)
            print("\n\nReading %s file..." % image_buffer)

            # Add Wait Signal (as Blocking to Main Thread) To Terminate Window on Focus.
            waitKey(0)  # 0 as in Indefinite Time before termination.
            # Call destroyAllWindows after detecting any key based on waitKey signal.
            destroyAllWindows()

            print("Image Display Window Closed. Wait for 1s.")
            sleep(1)

        # I don't know what kind of error will it raise but for assurance, use BaseException instead.
        except BaseException:
            print(
                "\nFile %s does not exists! Please produce an output image first!"
                % (image_buffer)
            )
            sleep(1)

    def apply_resize_on_image(self: object) -> None:
        pass

    def apply_blur_effect_on_image(self: object) -> None:
        while 1:
            blur_interp_option = 0
            blur_write_option = 0

            print("\n\n%s\n" % self.FEATURE_DISPLAY_STRS["BASE_OPTION_3"]["DESCRIPTION"])

            for optionIndex in range(0, 3):
                print("%i.) %s" % (optionIndex + 1, self.FEATURE_DISPLAY_STRS["BASE_OPTION_3"]["OPTION_%i" % optionIndex + 1]))

            try:
                self.input_buffers["display_choices"] = int(input("Please choose your option |> "))

                if self.input_buffers["display_choices"] == self.GAUSSIAN_OPTION:
                    pass

                elif self.input_buffers["display_choices"] == self.MEDIAN_OPTION:
                    pass

                elif self.input_buffers["display_choices"] == self.BILATERAL_OPTION:
                    pass

                else:
                    print("You picked a choice that does not exists! Please try again.")
                    sleep(1)
                    continue

                # Make the user decide whether to overwrite or write a new result with appended (n) where is nth of the same file name.


            except ValueError:
                print("Your choice is not an integer! Please try again.")
                sleep(1)

LOOP_ENDLESSLY = 1  # Constant Annotation on While Loop inside Driver.

if __name__ == "__main__":
    handler = VectorAssignmentClass("image", "jpg")
    while LOOP_ENDLESSLY:
        if not handler.display_options():
            break

    raise SystemExit("The script has finished executing.\n")

raise SystemError("Cannot import this module from another script.\n")
