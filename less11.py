import cv2

image_cat = "cat.jpeg"
image = cv2.imread(image_cat)
cv2.imshow("Cat", image)
cv2.waitKey()
