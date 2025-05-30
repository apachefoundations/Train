img=cv2.imread('/content/bird.jpg')
template=cv2.imread('/content/birdeye.jpg')
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray_template=cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)

result=cv2.matchTemplate(gray_img,gray_template,cv2.TM_CCOEFF_NORMED)
_,_,_,top = cv2.minMaxLoc(result)

h,w = gray_template.shape

cv2.rectangle(img,top,(top[0]+w,top[1]+h),(255,0,0),2)

plt.imshow(img)
