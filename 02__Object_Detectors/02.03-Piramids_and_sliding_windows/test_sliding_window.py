# import the necessary packages
from custom_library.object_detection.helpers import sliding_window, pyramid
import time
import cv2

# load the input image and unpack the command line arguments
image = cv2.imread('/home/damian/Workspace/GitHub_Repos/pyimagegurus_course/02__Object_Detectors/02.03-Piramids_and_sliding_windows/florida_trip.png')

(winW, winH) = (64, 64) #hardcoded standard  width x height

scale_value = 1.5


# loop over the image pyramid
for layer in pyramid(image, scale=scale_value):

    # loop over the sliding window for each layer of the pyramid
    for (x, y, window) in sliding_window(layer, stepSize=32, windowSize=(winW, winH)):
        # if the current window does not meet our desired window size, ignore it
        if window.shape[0] != winH or window.shape[1] != winW:
            continue

        # THIS IS WHERE WE WOULD PROCESS THE WINDOW, EXTRACT HOG FEATURES, AND
        # APPLY A MACHINE LEARNING CLASSIFIER TO PERFORM OBJECT DETECTION
        # since we do not have a classifier yet, let's just draw the window
        clone = layer.copy()
        cv2.rectangle(clone, (x, y), (x + winW, y + winH), (0, 255, 0), 2)
        cv2.imshow("Window", clone)

        # normally we would leave out this line, but let's pause execution
        # of our script so we can visualize the window
        cv2.waitKey(1)
        time.sleep(0.025)