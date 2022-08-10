# import the necessary packages
from custom_library.object_detection.helpers import pyramid
import cv2

# load the input image
image = cv2.imread('/home/damian/Workspace/GitHub_Repos/pyimagegurus_course/02__Object_Detectors/02.03-Piramids_and_sliding_windows/florida_trip.png')

scale_value = 1.5



# loop over the layers of the image pyramid and display them
for (i, layer) in enumerate(pyramid(image, scale=scale_value)):

    cv2.imshow("Window", layer)
    cv2.waitKey(0)