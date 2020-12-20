from cv2 import destroyAllWindows, imread, imshow, imwrite, split, waitKey

# Choose one for these image path.
# IMAGE_PATH = "../0_assets/cmyk_paint.png"
IMAGE_PATH = "../0_assets/RGB_paint.png"

DISPLAY_WINDOW_COLOR_STRING = [
    "Blue",
    "Green",
    "Red",
]

image = imread(IMAGE_PATH)

# Get Color Buffer to Store in BGR Style Format.
B, G, R = split(image)

# Show the original before showing each in color channel.
imshow("Original Image of %s" % IMAGE_PATH, image)

# Iterate for each Color Channel. Do not invoke wait signal for each window to see the comparison.
for idx, eachColors in enumerate([B, G, R]):
    imshow(
        "%s Color Representation | %s" % (DISPLAY_WINDOW_COLOR_STRING[idx], IMAGE_PATH),
        eachColors,
    )
    imwrite(
        "rgb_%s_color.png" % DISPLAY_WINDOW_COLOR_STRING[idx].lower(),
        eachColors,
    )

# # Note that, each Color Channel shows lighter color.
# ! The lighter it is, the more it actually represents the color.

# We wait for the user input via wait signal to terminate.
if waitKey(0):
    destroyAllWindows()
