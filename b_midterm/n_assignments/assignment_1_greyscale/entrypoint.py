from subprocess import Popen
# import cv2
from typing import Final # Type Linting or Duck Typing.
from time import sleep # Sleep.


class GreyscaleHandler(object):

    def __init__(self, args_value, _args="test") -> None:
        pass


    #     Popen("CLS", shell=True).communicate()

    #     self.args_value = コーデックス-リンク
    #     self.args : Final = _args

    #     super().__init__()

    #     self.test2()


    def test1(self):
        self.asd = None

        print("Hello World")

    def test2(self):

        print("Hello from Test2")

    def display_sent_value(self) -> None:
        # print(self.args_value)
        print("コーデックス-リンク")


# __name__ will be "__main__" when executed in terminal.
# __name__ will be "filename" when executed via import from other script.
if __name__ == "__main__":
    driver = GreyscaleHandler()

    driver.test1()

    driver.display_sent_value()

    raise SystemExit("Finished.")

else:
    print("asd")