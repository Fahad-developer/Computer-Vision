import cv2

# Load the image
image = cv2.imread('flower.jpeg')

# Split the image into its RGB channels
b, g, r = cv2.split(image)

# Resize each channel to 200x200 pixels
resized_b = cv2.resize(b, (200, 200))
resized_g = cv2.resize(g, (200, 200))
resized_r = cv2.resize(r, (200, 200))

# Merge the resized channels back into an RGB image
resized_image = cv2.merge((resized_b, resized_g, resized_r))

# Display the resized RGB image
cv2.imshow('Resized RGB Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
