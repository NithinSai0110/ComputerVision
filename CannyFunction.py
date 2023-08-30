import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)
print(kernel)
p="C:\\Users\\nithi\\Downloads\\DisneyCars.jpg"
img =cv2.imread(p)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(imgBlur,100,200)
desired_width = 800
desired_height = 600
img_resized = cv2.resize(imgCanny, (desired_width, desired_height))
cv2.imshow("Img Canny",img_resized)
cv2.waitKey(0)
