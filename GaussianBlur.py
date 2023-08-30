import cv2
p="C:\\Users\\nithi\\Downloads\\DisneyCars.jpg"
i = cv2.imread(p)
b = cv2.GaussianBlur(i, (15, 15), 0)
i=cv2.resize(i,(1200,700))
b=cv2.resize(b,(1200,700))
cv2.imshow('Original Image', i)
cv2.imshow('Blurred Image', b)
cv2.waitKey(0)
cv2.destroyAllWindows()