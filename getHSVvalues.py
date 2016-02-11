import cv2
import numpy as np



def hsvMEAN( n ):
    hsv = cv2.cvtColor(n, cv2.COLOR_BGR2HSV)
    hue = sum(hsv[:, :, 0])
    saturation = sum(hsv[:, :, 1])
    value = sum(hsv[:, :, 2])
    return hue,saturation,value