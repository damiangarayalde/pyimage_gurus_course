# import the necessary packages
import cv2
import numpy as np
import imutils

# load the image and convert it to grayscale
image = cv2.imread("/home/damian/Workspace/GitHub_Repos/pyimagegurus_course/01.11-Contours/basic_shapes.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# show the original image
cv2.imshow('original', image)
cv2.waitKey(0)

# # find all contours in the image and draw ALL contours on the image
# cnts  = cv2.findContours(gray.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# cntss = imutils.grab_contours(cnts) # list of the contours found

# clone = image.copy()

# cnts2draw     = -1 # list index of the contour to draw. Use -1 to draw them all
# cnt_colour    = (0 , 255, 0 ) # green
# cnt_thickness = 2             # pixels

# cv2.drawContours(clone, cntss, cnts2draw, cnt_colour, cnt_thickness)

# print(f'''Found {len(cntss)} contours''')

# # show the output image
# cv2.imshow('output',clone)

