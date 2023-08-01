import matplotlib
matplotlib.use('TkAgg')  # Set the backend to TkAgg

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("jhon.jpg", 0)
plt.plot(img[0, :])
plt.show()
plt.waitforbuttonpress()
cv2.destroyAllWindows()
