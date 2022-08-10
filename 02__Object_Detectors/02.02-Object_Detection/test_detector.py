# import the necessary packages
from matplotlib import pyplot as plt
from imutils import paths
import dlib
import cv2


# load the detector
detector = dlib.simple_object_detector('/home/damian/Workspace/GitHub_Repos/pyimagegurus_course/02__Object_Detectors/02.02-Object_Detection/output/stop_sign_detector.svm')

# loop over the testing images
for testingPath in paths.list_images('/home/damian/Workspace/GitHub_Repos/pyimagegurus_course/02__Object_Detectors/02.02-Object_Detection/stop_sign_testing'):

    # load the image and make predictions
    image = cv2.imread(testingPath)
    boxes = detector(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # loop over the bounding boxes and draw them
    for b in boxes:
        (x, y, w, h) = (b.left(), b.top(), b.right(), b.bottom())
        cv2.rectangle(image, (x, y), (w, h), (0, 255, 0), 2)

    # show the image
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.show()
