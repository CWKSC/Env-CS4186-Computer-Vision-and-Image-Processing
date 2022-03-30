import os

import cv2
import matplotlib.pyplot as plt

image = cv2.imread(os.path.dirname(__file__) + "\image.jpg")

colors = ("b", "g", "r")
for i, color in enumerate(colors):
    histr = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(histr, color=color)
    plt.xlim([0, 256])
plt.show()
