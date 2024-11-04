import numpy as np
import cv2

# Create a blank canvas that's 300 px x 300 px
canvas = np.zeros((300, 300, 3), dtype = "uint8")

# Let's paint our entire canvas blue
blue = (255, 0, 0)
cv2.rectangle(canvas, (0,0), (299, 299), blue, -1)
cv2.imshow("Canvas", canvas)


# Get the coordinates of the center of the canvas
(centerX, centerY) = (canvas.shape[1] / 2, canvas.shape[0] / 2)

# Let's paint white circles for ripples
white = (255, 255, 255)

# Let's wait a moment and then drop a stone into our still pond
cv2.waitKey(1000)
cv2.circle(canvas, (centerX, centerY), 5, white, -1)
cv2.imshow("Canvas", canvas)

# Let's paint some diminishing ripples in our pond,
# though it's going to kinda sorta look cheap since
# I'm using a single process and thread to draw this
for i in xrange(0, 25, 5):
    for r in xrange(25, 175, 25 + i):
        cv2.circle(canvas, (centerX, centerY), r, white, 5 - (i / 5))
        cv2.imshow("Canvas", canvas)
        cv2.waitKey(250)
    for r in xrange(25, 175, 25 + i):
        cv2.circle(canvas, (centerX, centerY), r, blue, 5 - (i / 5))
        cv2.imshow("Canvas", canvas)
        cv2.waitKey(150)
