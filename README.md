# Histogram-of-an-images
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


## Program and Output:

# Developed By: DIVYA.A
# Register Number: 212222230034
### Input Grayscale Image and Color Image
```
import cv2
import matplotlib.pyplot as plt
gray_image=cv2.imread('img1.jpeg')
grey=cv2.cvtColor(gray_image,cv2.COLOR_BGR2GRAY)
plt.imshow(grey)
plt.axis('on')
plt.show()
```
![Screenshot 2024-09-30 153601](https://github.com/user-attachments/assets/71bc39e7-4052-4e6e-ad46-d420d8c41a35)
```
color_image=cv2.imread('img2.jpeg')
plt.imshow(color_image)
plt.axis('on')
plt.show()
```
![Screenshot 2024-09-30 153606](https://github.com/user-attachments/assets/619536e8-4c97-4919-9c7c-ba3f6fa75500)

### Histogram of Grayscale Image and any channel of Color Image
```
import numpy as np
Gray_image = cv2.imread("img1.jpeg")
Color_image = cv2.imread("img2.jpeg")
grey=cv2.cvtColor(gray_image,cv2.COLOR_BGR2GRAY)
gray_hist = cv2.calcHist([grey],[0],None,[1100],[0,1100])
plt.figure()
plt.imshow(grey)
plt.show()
plt.title("Histogram")
plt.xlabel("Grayscale Value")
plt.ylabel("Pixel Count")
plt.stem(gray_hist)
plt.show()
```

![Screenshot 2024-09-30 153611](https://github.com/user-attachments/assets/1e2cddd9-097a-4c39-8b14-384a8ac71525)

![Screenshot 2024-09-30 153617](https://github.com/user-attachments/assets/6c4dd3fe-e3eb-4f2a-9d2c-d362c4ae724d)

```
color_hist = cv2.calcHist([Color_image],[0],None,[2600],[0,2600])
plt.figure() 
plt.imshow(color_image)
plt.show()
plt.title("Histogram")
plt.xlabel("Grayscale Value")
plt.ylabel("Pixel Count")
plt.stem(color_hist)
plt.show()
```

![Screenshot 2024-09-30 153622](https://github.com/user-attachments/assets/30c55d76-237e-4587-9f34-441769e644f6)

![Screenshot 2024-09-30 153632](https://github.com/user-attachments/assets/22483169-d151-4694-9aa4-d5e05340842d)

### Histogram Equalization of Grayscale Image.
```
gray_image = cv2.imread("img1.jpeg")
grey=cv2.cvtColor(gray_image,cv2.COLOR_BGR2GRAY)
plt.imshow(grey)
plt.show()
```

![Screenshot 2024-09-30 153637](https://github.com/user-attachments/assets/708c588e-027c-4775-9906-fe133794f357)
```
equ = cv2.equalizeHist(grey)
plt.imshow(equ)
plt.show()
```

![Screenshot 2024-09-30 153642](https://github.com/user-attachments/assets/0bcae091-ce26-4b60-b2f9-708e4c24099c)
```
color_image=cv2.imread('img2.jpeg')
grey=cv2.cvtColor(color_image,cv2.COLOR_BGR2GRAY)
plt.imshow(color_image)
plt.show()
```

![Screenshot 2024-09-30 153647](https://github.com/user-attachments/assets/768fc05c-a68b-4c01-9137-29dd63d664de)
```
eq = cv2.equalizeHist(grey)
plt.imshow(eq)
plt.show()
```

![Screenshot 2024-09-30 153651](https://github.com/user-attachments/assets/5982893c-51c2-45fb-832c-f58b7f5f97a1)

## Result: 
Thus the histogram for finding the frequency of pixels in an image with pixel values ranging from 0 to 255 is obtained. Also,histogram equalization is done for the gray scale image using OpenCV.
