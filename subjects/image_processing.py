import numpy as np
import cv2 as cv


global img 

img = cv.imread('images/mario.png')

def updateImage(value):
    #multiply the image by the scalar
    img_ = img * value
    #show the image
    cv.imshow('image', img_)


#add a slider to change the scalar value and multiply the image
cv.namedWindow('image')
cv.createTrackbar('scalar', 'image', 1, 255, updateImage)


#show the image
cv.imshow('image', img)
cv.waitKey(0)
