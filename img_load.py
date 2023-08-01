import cv2   # Importing cv2 library.
# Creating a variable and reading the image.
img = cv2.imread("flower.jpeg", 1)
img = cv2.resize(img, (200,250))
# Printing the shape of the image.
print(img.shape)

# Displaying the image in a window.
cv2.imshow("WINDOW", img)
cv2.waitKey(0)
