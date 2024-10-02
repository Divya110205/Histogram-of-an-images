![Screenshot 2024-10-02 170606](https://github.com/user-attachments/assets/3dc716a9-d9e9-45d6-b94c-ab8ee6d2054c)# Histogram-of-an-images
## Aim
To obtain a histogram for finding the frequency of pixels in an Image with pixel values ranging from 0 to 255. Also write the code using OpenCV to perform histogram equalization.

## Software Required:
Anaconda - Python 3.7

## Algorithm:
### Step1:
Read the gray and color image using imread()

### Step2:
Print the image using imshow().



### Step3:
Use calcHist() function to mark the image in graph frequency for gray and color image.

### step4:
Use calcHist() function to mark the image in graph frequency for gray and color image.

### Step5:
The Histogram of gray scale image and color image is shown.


## Program:

### Developed By: DIVYA.A
### Register Number: 212222230034

### Input Grayscale Image and Color Image
```
import cv2
import matplotlib.pyplot as plt
gray_image = cv2.imread('img1.jpeg')
color_image = cv2.imread('img2.jpeg')
cv2.imshow("Gray image",gray_image)
cv2.imshow("color image",color_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### Histogram of Grayscale Image 
```
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
```
### Histogram of any channel of Color Image
```
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
```
### Histogram Equalization of Grayscale Image.
```
import cv2
gray_image = cv2.imread("img1.jpeg",0)
cv2.imshow('Grey Scale Image',gray_image)
equ = cv2.equalizeHist(gray_image)
cv2.imshow("Equalized Image",equ)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
## Output:
### Input Grayscale Image and Color Image
![Screenshot 2024-10-02 170534](https://github.com/user-attachments/assets/e3d1ae1d-4209-4393-a421-971151e51c2c)


### Histogram of Grayscale Image
![Screenshot 2024-10-02 170606](https://github.com/user-attachments/assets/fed6369d-9f0a-436e-83c8-5d957fa087c8)

### Histogram of any channel of Color Image
![Screenshot 2024-10-02 170635](https://github.com/user-attachments/assets/eacc3ea0-c7e9-426c-9db0-75d960ae8d23)


### Histogram Equalization of Grayscale Image.
![Screenshot 2024-10-02 170737](https://github.com/user-attachments/assets/ab339353-f283-4438-852b-ba5812a51cd1)

## Result: 
Thus the histogram for finding the frequency of pixels in an image with pixel values ranging from 0 to 255 is obtained. Also,histogram equalization is done for the gray scale image using OpenCV.
