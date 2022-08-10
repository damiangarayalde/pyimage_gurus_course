# import the necessary packages
import cv2
import imutils

# load the face detector and detect faces in the image
detector = cv2.CascadeClassifier('11.02-FaceDetection_VJones/cascades/haarcascade_frontalface_default.xml')

vid = cv2.VideoCapture(0)
  
while(True):
      
    # Capture the video frame by frame
	ret, frame = vid.read()
	
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	faceRects = detector.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5,	minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

	print("I found {} face(s)".format(len(faceRects)))

	# loop over the faces and draw a rectangle around each
	for (x, y, w, h) in faceRects:
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

	# show the detected faces
	cv2.imshow("Faces", frame)
	
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


# After the loop release the cap object
vid.release()

# Destroy all the windows
cv2.destroyAllWindows()