# write 
import cv2 as cv
import numpy as np
 
cap = cv.VideoCapture(0)
#writing format, codec, video writer onject and file output
frame_widthe = int(cap.get(3))
frame_height = int(cap.get(4))
out= cv.VideoWriter("resources/cam_vidoe.avi", cv.VideoWriter_fourcc('M','J','P', 'G'), 25, (frame_widthe, frame_height))

#indicator
if (cap.isOpened() == False):
    print("error in uploading")
#Reading and Playing
while (True):
    (ret, frame) = cap.read()
    #To show in player
    if ret == True:
        out.write(frame)
        cv.imshow("Vidoe", frame)
        #To quit with q
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release( )
cv.destroyAllWindows()
