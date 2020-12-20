# From OpenCV Library, import only imread, resize, INTER_LINEAR, INTER_AREA and INTER_CUBIC.
from cv2 import INTER_AREA, INTER_CUBIC, INTER_LINEAR, imread, imwrite, resize
from matplotlib.pyplot import (
    imshow as show_image,
    savefig,
    show as show_figure,
    subplot,
    title,
)

# % matplotlib qt # ! They said its a magic line, uncomment if you're having issues. And I have no idea what this was for.

"""
    # In this script, we're not worrying about the aspect ratio when it comes to image resizing.
    * The focus of image resizing here is for the use of interpolation.

    ! So far, in OpenCV we have three best-known available interpolations for image resizing and those are:
    * (1) INTER_LINEAR — Default Option for Image Enlargement. Faster than Cubic, Primarily Used when zooming is required.
    * (2) INTER_AREA — Specifically used for Image Shrinking. Technically an interpolation for using best representative pixel to ensure quality is not worse upon shrink.
    * (3) INTER_CUBIC — A Complex Computated Interpolation for Image Enlargement. Slower than Linear, but the quality is better.

    * Meanwhile, there are other known Interpolators as well. But its not that well known or used as far as I cant tell.
    * (1) INTER_NEAREST — a nearest-neighbor interpolation, might be used for image shrinking because it base on near-pixel of the selected pixel.
    * (2) INTER_LANCZOS4  — a Lanczos interpolation over 8×8 pixel neighborhood. Potentially usable for pixel-candidate for image shrinking and enlargement.

    For now, only INTER_LINEAR, INTER_AREA, and INTER_CUBIC will be introduced for now.
"""

# # If you're still confused, here's a great article to read about image scaling.
# # https://subscription.packtpub.com/book/application_development/9781785283932/1/ch01lvl1sec13/image-scaling


# This is a magic command to display in an external window
# Credits to https://www.gardeningknowhow.com/edible/vegetables/tomato/planting-tomato-plants.htm for the picture.

original_image_buffer = imread("../0_assets/img_7.jpg")
original_image_h, original_image_w = original_image_buffer.shape[:2]
"""
    * By this point, we have to create atleast 3 buffers to modify the original image, and to show the interpolation output as well.
    * The original image properties of ../0_assets/img_7.jpg has the following:
        (1) Type: .jpg
        (2) Size: 224 KB
        (3) Width and Height: (1600 x 1200)

"""

# The use of scaling factors is okay than using the width and height for adjustment.
# Though the effects of scaling and the result is not known, to my case so, it is your preference to do some modification to the parameters.
area_shrink_buffer = resize(
    original_image_buffer, (0, 0), fx=0.1, fy=0.1, interpolation=INTER_AREA
)
cubic_enlarge_buffer = resize(
    original_image_buffer,
    (original_image_w * 2, original_image_h * 2),
    interpolation=INTER_CUBIC,
)
linear_enlarge_buffer = resize(
    original_image_buffer,
    (original_image_w * 2, original_image_h * 2),
    interpolation=INTER_LINEAR,
)

FIGURE_TITLES = ["Original", "Inter. Area", "Inter. Cubic", "Inter. Linear"]
IMAGE_BUFFERS = [
    original_image_buffer,
    area_shrink_buffer,
    cubic_enlarge_buffer,
    linear_enlarge_buffer,
]

# Referencing IMAGE_BUFFER will cause the figure to not show it.
# The for loop seem complex, let's deconstruct it.

"""
    * enumerate(range(0, len(FIGURE_TITLES)))

    First, we figure out the number of elements in the list, which is 4.
    Then we generate a range for the iteration from 0 as starting point and the resulting len(FIGURE_TITLES) which is 4, as the last point.
    Then we enumerate it by having an index generate for us, which is then stored in idx variable of the for loop for element reference in the list.
"""

for idx, buf in enumerate(range(0, len(FIGURE_TITLES))):
    subplot(2, 2, idx + 1)
    title(FIGURE_TITLES[idx])
    show_image(IMAGE_BUFFERS[idx])
    # Ignore the Original Image and Save the Other Modifications while Sterilizing the Image Write File Name.
    if idx > 0:
        imwrite(
            "%s.png" % (FIGURE_TITLES[idx].replace(".", "_").replace(" ", "").lower()),
            IMAGE_BUFFERS[idx],
        )

# ! Note, if you don't have tkinter by default (means of opt-out from the python installation), you might not be able to see the output.
# ! Here's the result if you don't have tkinter, UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.

# # By this point, you have to re-install your python to install the tkinter. Because in the future modules, you really have to display some other elements that is correlated in the figure.

# * Credits to the OP of this issue: https://stackoverflow.com/questions/56656777/userwarning-matplotlib-is-currently-using-agg-which-is-a-non-gui-backend-so
show_figure()  # ! Uncomment this line if you want to display the figure window.

# In my perspective, I don't have tkinter, so I might wanna save it instead to see the result.
# * Solution from the Issue: https://stackoverflow.com/a/58181952/5353223
savefig(
    "result.png"
)  # Uncommment if you wanna see them 4 in 1 picture without executing this.
