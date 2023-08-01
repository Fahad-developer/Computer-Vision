import cv2
import numpy as np
#import matplotlib.pyplot as plt

# Read the image in grayscale
img = cv2.imread("flower.jpeg", 0)
img = cv2.resize(img , (100,150))

# Define the kernels
box = np.ones((3, 3), dtype=np.float32) / 9.0
edge_kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float32)
edge_ky = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]], dtype=np.float32)

# Perform image smoothing and edge detection
smooth = cv2.filter2D(img, -1, box)
edges_x = cv2.filter2D(smooth, -1, edge_kx)
edges_y = cv2.filter2D(smooth, -1, edge_ky)
img_edges = cv2.filter2D(smooth, -1, edge_kx)

# Display the images
cv2.imshow("ORIGINAL", img)
cv2.imshow("SMOOTH", smooth)
cv2.imshow("EDGES X", edges_x)
cv2.imshow("EDGES Y", edges_y)
cv2.waitKey(0)
cv2.destroyAllWindows()
