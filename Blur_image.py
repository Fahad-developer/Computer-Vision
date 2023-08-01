# Importing cv2 library
import cv2
# Create variable to store image using imread() function.
image = cv2.imread("flower.jpeg")
# Creating Variable to store image blurred by GaussianBlur function.
blurred = cv2.GaussianBlur(image, (5,5), 0)
# Showing image using imshow function.
cv2.imshow("Original image", image)
# Showing Blurred image using imshow function.
cv2.imshow("Blurred image", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()