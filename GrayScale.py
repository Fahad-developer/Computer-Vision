import cv2

# Load the image
image = cv2.imread('flower.jpeg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
passport_size = (200, 200)
# Changing the size of image to passport size.
resized_image = cv2.resize(gray_image, passport_size)
# Display the original and grayscale images
cv2.imshow('Grayscale Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
