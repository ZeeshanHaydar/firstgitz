# How to save the video 
import cv2 as cv
from cv2 import cvtColor
cap = cv.VideoCapture('resources/rice.mp4')
#writing format, codec, video writer onject and file output
frame_widthe = int(cap.get(3))
frame_height = int(cap.get(4))
out= cv.VideoWriter("resources/output_vidoe.avi", cv.VideoWriter_fourcc('M','J','P', 'G'), 10, (frame_widthe, frame_height), isColor= False)

#indicator
if (cap.isOpened() == False):
    print("error in uploading")
#Reading and Playing
while (True):
    (ret, frame) = cap.read()
    grayframe= cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    (thersh, binary)= cv.threshold(grayframe, 127, 255, cv.THRESH_BINARY)
    #To show in player
    if ret == True:
        out.write(grayframe)
        cv.imshow("Vidoe", binary)
        #To quit with q
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release( )
cv.destroyAllWindows()
