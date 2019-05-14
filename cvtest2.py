#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 20:00:04 2019

@author: siddharth
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

data = cv2.imread('/home/siddharth/Desktop/OpenCV/Images/google.jpg')
cv2.imshow('Google' ,data)
cv2.destroyAllWindows()

img = np.zeros((512,512,3))
img_bw = np.zeros((512,512))

cv2.imshow('black', img)
cv2.imshow('BW' , img_bw)
cv2.destroyAllWindows()


#line across the image
cv2.line(img ,(1,9),(510,510),(100,100,0),5)
cv2.imshow('Line', img)
cv2.destroyAllWindows()


#rectangle across the image
cv2.rectangle(img,(100,100),(200,200),(0,0,100),5)
cv2.imshow('Rectangle', img)
cv2.destroyAllWindows()

#circle now
cv2.circle(img , (100,100),50,(100,0,0),5)
cv2.imshow('Circle',img)
cv2.destroyAllWindows()

#insert text
cv2.putText(img,"This is text we are inserting",(15,250),cv2.FONT_HERSHEY_PLAIN,2,(100,0,0),1)
cv2.imshow('Text in image.png', img)

