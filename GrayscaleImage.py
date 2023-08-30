import cv2
p="C:\\Users\\nithi\\Downloads\\DisneyCars.jpg"
i=cv2.imread(p)
g=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
i1=cv2.resize(i,(1300,720))
cv2.imshow("Original image",i1)
g1=cv2.resize(g,(1300,720))
cv2.imshow("Grayscale image",g1)
cv2.waitKey(0)
cv2.destroyAllWindows()