# Takes an image and returns if it's blurred
# pip install opencv-python

import cv2
import numpy as np

def is_blurred (image, threshold=90):
    imagecv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    graycv = cv2.cvtColor(imagecv, cv2.COLOR_BGR2GRAY)
    edgescv = cv2.Laplacian(graycv, cv2.CV_64F)
    variance = edgescv.var()
    return (variance<threshold, variance)

if __name__ == '__main__':
    sourceimage = cv2.imread('../../statics/imgs/storm_trooper.jpeg')
    print(is_blurred(sourceimage))