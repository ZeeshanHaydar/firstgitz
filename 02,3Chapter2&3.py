#Reading the image and display it
#librart import
import cv2 as cv
from cv2 import cvtColor
img= cv.imread("resources/Zeeshan.jpg")
img= cv.resize(img, (500,400))

#conversion
gray_img= cvtColor(img, cv.COLOR_BGR2GRAY)
#display image
cv.imshow("First image", img)
cv.imshow("Second image",gray_img)

cv.waitKey(0)
cv.destroyAllWindows()

