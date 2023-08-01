import cv2

# Load the image
image = cv2.imread('flower.jpeg')

Passport_size = (200, 200)
resize_image = cv2.resize(image, Passport_size)
# Apply Box filter
box_filtered = cv2.boxFilter(resize_image, -1, (3, 3))

# Display the box filtered images
cv2.imshow('Box Filtered Image', box_filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()
