#Step1= import Libraries
import cv2 as cv
import numpy as np
#Step_2 Read from Camera
cap= cv.VideoCapture(0)

#read cam untill end
# Disply frame by frame

while(True):
    #capture frame by frame
    ret, frame = cap.read()
    grayframe= cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    (thersh, binary)= cv.threshold(grayframe, 127, 255, cv.THRESH_BINARY)
    #to disply frame
    cv.imshow("frame", frame)
    cv.imshow("Gray_frame", grayframe)
    cv.imshow("Binary", binary)
    if cv.waitKey(1) & 0xFF == ord('q'):
      break

#Release and close the window
cap.release()
cv.destroyAllWindows()

    
