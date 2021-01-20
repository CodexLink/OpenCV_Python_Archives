# read enhanced image
import cv2
import numpy as np

img = cv2.imread('assets/da9786183a30bdde3a542ac19603a563.jpg', 0)

print(img)

# Initialize the list
Cell_count, x_count, y_count = [], [], []

# read original image, to display the circle and center detection
display = cv2.imread("assets/da9786183a30bdde3a542ac19603a563.jpg")

# hough transform with modified circular parameters
circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1.2, 20,
                           param1 = 50, param2 = 20, minRadius = 1, maxRadius = 15)

# circle detection and labeling using hough transformation
if circles is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")

        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:

                cv2.circle(display, (x, y), r, (0, 255, 0), 2)
                cv2.rectangle(display, (x - 2, y - 2),
                              (x + 2, y + 2), (0, 128, 255), -1)
                Cell_count.append(r)
                x_count.append(x)
                y_count.append(y)
        # show the output image
        cv2.imshow("gray", display)
        cv2.waitKey(0)