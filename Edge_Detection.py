import cv2

# Load the image
image = cv2.imread('flower.jpeg')

# Resize the image to 200x200 pixels
resized_image = cv2.resize(image, (200, 200))

# Convert the resized image to grayscale
gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(gray, 100, 200)
# Resize the original image to 200x200 pixels
resized_original = cv2.resize(image, (200, 200))
# Display the resized original image, resized image, and the detected edges
cv2.imshow('Original Image', resized_original)
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
