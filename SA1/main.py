# import required libraries
import cv2


# Capture the camera feed and set the resolution
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Loop to display video
while True:
    try:
        check,cameraFeedImg=cap.read()
        cameraFeedImg=cv2.flip(cameraFeedImg,1)
        # Get a single capture from the camera
    except Exception as e:
        print(e)
    cv2.imshow("Image",cameraFeedImg)
    cv2.waitKey(1)        

    
    # Show the camera feed image
   
