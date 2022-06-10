#Step1= import Libraries
import cv2 as cv
import numpy as np
#Step_2 Read from Camera
cap= cv.VideoCapture(0)

#read cam untill end
# Disply frame by frame

while(cap.isOpened()):
    #capture frame by frame
    ret, frame = cap.read()
    if ret == True:
        #to disply frame
        cv.imshow("frame", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

#Release and close the window
cap.release()
cv.destroyAllWindows()

    
