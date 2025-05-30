import cv2
import numpy as np
import matplotlib.pyplot as plt

hsv = cv2.cvtColor(img_resize, cv2.COLOR_BGR2HSV)

lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])
mask = cv2.inRange(hsv, lower_red, upper_red)

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img_resize, cv2.COLOR_BGR2RGB)) 
plt.title("Original")

plt.subplot(1, 2, 2) 
plt.imshow(mask, cmap='gray') 
plt.title("Red Mask")

plt.tight_layout() 
plt.show()
