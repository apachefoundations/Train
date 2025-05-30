import numpy as np
blur=cv2.GaussianBlur(img_resize,(15,15),0)
plt.imshow(blur)
plt.title("blurred Image")
plt.show()
print('\n')
kernal=np.array([[0,-3,0],
                 [-3,15,-3],
                 [0,-3,0]])
sharp=cv2.filter2D(img_resize,-1,kernal)
plt.imshow(sharp)
plt.title("sharp image")
plt.show()
