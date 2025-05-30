import cv2
import numpy as np

bg = cv2.imread('background.jpg')
fg = cv2.imread('greenscreen.jpg')
fg = cv2.resize(fg, (bg.shape[1], bg.shape[0]))

hsv = cv2.cvtColor(fg, cv2.COLOR_BGR2HSV)
lower_green = np.array([35, 40, 40])
upper_green = np.array([85, 255, 255])
mask = cv2.inRange(hsv, lower_green, upper_green)

inv_mask = cv2.bitwise_not(mask)
fg_part = cv2.bitwise_and(fg, fg, mask=inv_mask)
bg_part = cv2.bitwise_and(bg, bg, mask=mask)
result = cv2.add(fg_part, bg_part)

cv2.imshow("Green Screen Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
