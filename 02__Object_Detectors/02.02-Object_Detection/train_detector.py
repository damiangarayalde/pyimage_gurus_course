# import the necessary packages
#from __future__ import print_function
from imutils import paths
from scipy.io import loadmat
from skimage import io
import os
import dlib
import sys
import cv2

cwd = os.getcwd()

# grab the default training options for our HOG + Linear SVM detector, 
# then initialize the list of images and bounding boxes used to train the classifier

print("[INFO] gathering images and bounding boxes...")

options = dlib.simple_object_detector_training_options()

images  = []
boxes   = []

# loop over the image paths
#for imagePath in paths.list_images('/home/damian/Workspace/GitHub_Repos/pyimagegurus_course/02__Object_Detectors/02.02-Object_Detection/stop_sign_images'):

#for imagePath in paths.list_images(cwd+'/stop_sign_images'):
print(os.path.abspath() )
print( cwd + '/stop_sign_images')

# 	# extract the image ID from the image path and load the annotations file
# 	imageID = imagePath[imagePath.rfind("/") + 1:].split("_")[1]
# 	imageID = imageID.replace(".jpg", "")

# 	p = "{}/annotation_{}.mat".format('/home/damian/Workspace/GitHub_Repos/pyimagegurus_course/02__Object_Detectors/02.02-Object_Detection/stop_sign_annotations', imageID)

# 	annotations = loadmat(p)["box_coord"]

# 	# loop over the annotations and add each annotation to the list of bounding boxes
# 	bb = [ dlib.rectangle(   left=int(x), top=int(y), right=int(w), bottom=int(h)   )	for (y, h, x, w) in annotations]

# 	boxes.append(bb)

# 	# add the image to the list of images
# 	images.append(io.imread(imagePath))


# # train the object detector
# print("[INFO] training detector...")
# detector = dlib.train_simple_object_detector(images, boxes, options)

# # dump the classifier to file
# print("[INFO] dumping classifier to file...")
# detector.save('/home/damian/Workspace/GitHub_Repos/pyimagegurus_course/02__Object_Detectors/02.02-Object_Detection/output/stop_sign_detector.svm')
# #detector.save('/home/damian/Workspace/GitHub_Repos/pyimagegurus_course/02__Object_Detectors/02.02-Object_Detection/output/stop_sign_detector.svm')

# # visualize the results of the detector
# win = dlib.image_window()
# win.set_image(detector)
# dlib.hit_enter_to_continue()