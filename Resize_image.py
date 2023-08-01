import cv2   # importing cv2 library.
# Creating a variable and reading image.
img = cv2.imread("flower.jpeg", 1)

passport_size = (300, 300)

resized_image = cv2.resize(img, passport_size)

cv2.imshow("WINDOW", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
