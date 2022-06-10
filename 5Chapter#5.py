#image into Black and white
import cv2 as cv
from cv2 import cvtColor
from cv2 import imshow
from cv2 import imwrite
img= cv.imread("resources/harvester.png")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
(thersh, binary)= cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
imwrite("image_gray.png", gray)
#cv.waitKey(0)
#cv.destroyAllWindows