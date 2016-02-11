import cv2
import numpy as np



def rgbPercentage( n ):

    B = sum(cv2.mean(n[:, :, 0]))
    G = sum(cv2.mean(n[:, :, 1]))
    R = sum(cv2.mean(n[:, :, 2]))
    total_sum = R+B+G
    B = B / total_sum
    G = G / total_sum
    R = R / total_sum

    return R,G,B