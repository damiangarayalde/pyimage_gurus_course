# # import the necessary packages
from pyimagesearch.markers import DistanceFinder2
# from imutils import paths
import imutils
import cv2


ref_width = 10 # mm
ref_dist  = 1000 # mm

df = DistanceFinder2( ref_width, ref_dist )


#------------------------------------------------------
# Capture the reference image for calibration
#
#
# define a video capture object
vid = cv2.VideoCapture(0)
  
ret, frameo = vid.read()
frameo = imutils.resize(frameo, height=400)

while(True):
      
    # Capture the video frame by frame
    ret, frame = vid.read()
  
    cv2.waitKey(0)
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    # load the reference image and resize it
    refImage = frame
    refImage = imutils.resize(refImage, height=400)

    # initialize the distance finder, find the marker in the image, and calibrate the distance finder

    refMarker,edgedd = DistanceFinder2.findSquareMarker(cv2.subtract(refImage,frameo))
    #df.calibrate(refMarker[2])

    # visualize the results on the reference image and display it
    # refImage = df.draw(refImage, refMarker, df.distance(refMarker[2]))
    cv2.imshow("Reference", refImage)
    cv2.imshow("s", edgedd)

    frameo = refImage


#-----------------------------------------------------------------------------
# Dinamically calculate and show distance to object

# while(True):

#     # Capture the video frame by frame
#     ret, frame = vid.read()

# 	# extract the filename, load the image, and resize it
#     image = imutils.resize(frame, height=700)

# 	# find the marker in the image
#     marker = DistanceFinder.findSquareMarker(image)

# 	# if the marker is None, then the square marker could not be found in the image
#     if marker is None:
#         print("[INFO] could not find marker")
#         continue

# 	# determine the distance to the marker
#     distance = df.distance(marker[2])

# 	# visualize the results on the image and display it
#     image = df.draw(image, marker, distance)
    
#     cv2.imshow("Image", image)

#     # the 'q' button is set as the
#     # quitting button you may use any
#     # desired button of your choice
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


# # 
# After the loop release the cap object
vid.release()

# Destroy all the windows
cv2.destroyAllWindows()