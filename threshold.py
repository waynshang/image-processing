import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("pip20.jpg",0)
ret,thresh1 = cv2.threshold(img,75,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
titles = ['Original Image','BINARY','BINARY_INV','TRUNC']
images = [img, thresh1, th2, th3]
for i in range(4):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
