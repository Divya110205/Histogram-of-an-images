#!/usr/bin/env python
# coding: utf-8

# In[1]:Write your code to find the histogram of gray scale image and color image channels
import cv2
import matplotlib.pyplot as plt
gray_image = cv2.imread('img1.jpeg')
color_image = cv2.imread('img2.jpeg')
cv2.imshow("Gray image",gray_image)
cv2.imshow("color image",color_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# In[2]:Display the histogram of gray scale image and any one channel histogram from color image
import numpy as np
gray_image=cv2.imread('img1.jpeg')
import matplotlib.pyplot as plt 
gray_hist=cv2.calcHist(gray_image,[0],None,[255],[0,255])
plt.figure(figsize=(10,6))
plt.subplot(1,2,1)
plt.imshow(gray_image)
plt.subplot(1,2,2)
plt.title("Histogram")
plt.xlabel("Grayscale value")
plt.ylabel("pixel count")
plt.stem(gray_hist)
plt.show()

import numpy as np
color_image=cv2.imread('img2.jpeg')
color_img=cv2.cvtColor(color_image,cv2.COLOR_BGR2RGB)
import matplotlib.pyplot as plt 
color_hist=cv2.calcHist(color_img,[0],None,[255],[0,255])
plt.figure(figsize=(8,4))
plt.subplot(1,2,1)
plt.imshow(color_img)
plt.subplot(1,2,2)
plt.title("Histogram")
plt.xlabel("Colorscale value")
plt.ylabel("pixel count")
plt.stem(color_hist)
plt.show()

# In[3]:Write the code to perform histogram equalization of the image. 
import cv2
gray_image = cv2.imread("img1.jpeg",0)
cv2.imshow('Grey Scale Image',gray_image)
equ = cv2.equalizeHist(gray_image)
cv2.imshow("Equalized Image",equ)
cv2.waitKey(0)
cv2.destroyAllWindows()





