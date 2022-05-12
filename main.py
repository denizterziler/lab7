import cv2 as cv
import numpy
img = cv.imread('/Users/denizterziler/Desktop/batmanvjoker.jpeg')
(B, G, R) = cv.split(img)
cv.imshow("Red",R)
cv.imshow("Blue",B)
cv.imshow("Green",G)

print(img.shape)
for i in range(0,956):
    for a in range(0,1300):
        if R[i,a] > 100:
            R[i,a] = 10

merged = cv.merge([B, G, R])
cv.imshow("Merged", merged)


cv.waitKey(0)
