import cv2
import numpy as np
from oct2py import octave
import oct2py
import glob
import os
from matplotlib import pyplot as plt
import getHSVvalues
import getRGBpercentage


print glob.glob("/home/sani/Documents/icdar2015/icdar/*.*")
oc = oct2py.Oct2Py()

print("this works!")
img = cv2.imread('/home/sani/Desktop/pythonprograms/batman.jpg',1)
img1 = cv2.imread('/home/sani/Desktop/pythonprograms/img_11.png',1)
img2 = cv2.imread('/home/sani/Desktop/pythonprograms/img_9.png',1)
hist0 = cv2.calcHist([img1],[0],None,[256],[0,256])
hist1 = cv2.calcHist([img1],[1],None,[256],[0,256])
hist2 = cv2.calcHist([img1],[2],None,[256],[0,256])
sum = sum(cv2.mean(hist0) + cv2.mean(hist1) +cv2.mean(hist2))
print(hist0)
hist0 = cv2.mean(hist0)[0]/sum
hist1 = cv2.mean(hist1)[0]/sum
hist2 = cv2.mean(hist2)[0]/sum
cv2.waitKey(0)

hue,saturation,value = getHSVvalues.hsvMEAN(img1)
R,G,B = getRGBpercentage.rgbPercentage(img2)


hue,saturation,value = getHSVvalues.hsvMEAN(img)
R,G,B = getRGBpercentage.rgbPercentage(img)
print(R)
print(G)
print(B)


#ret,thresh = cv2.threshold(img,127,255,0)
#im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(img, contours, -1, (0,255,0), 3)

#vis = img.copy()
#cv2.imshow('img1.jpg',img1)
#cv2.waitKey(0)

mser = cv2.MSER()
mser1 = cv2.MSER()
mser2 = cv2.MSER()
regions = mser.detect(img, None)
regions1 = mser1.detect(img1, None)
regions2 = mser2.detect(img2, None)


edges = cv2.Canny(img1,100,200)

plt.subplot(121),plt.imshow(img1,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.savefig('foo.png')
plt.show()

#cv2.waitKey(0)

edges = cv2.Canny(img2,100,200)
plt.subplot(121),plt.imshow(img2,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.savefig('foo1.png')
plt.show()

#cv2.waitKey(0)


hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]
#for row in regions:
    #roi = (octave.max(regions(row)), octave.min(regions(row)) )
    #print row
hulls1 = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions1]
hulls2 = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions2]
cv2.polylines(img, hulls, 2, (33, 255, 0))
print(regions[1])
cv2.polylines(img1, hulls1, 2, (33, 255, 0))
cv2.polylines(img2, hulls2, 2, (33, 255, 0))
ret,thresh = cv2.threshold(img2,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow('img', img)
cv2.imshow('img3', img1)
cv2.imshow('img4', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()