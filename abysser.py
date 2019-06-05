# import the necessary packages
import numpy as np
import cv2
from matplotlib import pyplot as plt
import pytesseract
import os
import sys

## get image you want to load // no validity checking yet
relative_path = sys.argv[1];

# load image using opencv
img = cv2.imread(os.path.abspath(relative_path))

# smooth image
img = cv2.bilateralFilter(img,9,75,75)

# other smoothing ways
# kernel = np.ones((1,1),np.float32)/25
# img = cv2.filter2D(img,-1,kernel)
# img = cv2.blur(img,(1,2))
# img = cv2.GaussianBlur(img,(1,1),0)
# img = cv2.medianBlur(img,3)
# img = cv2.bilateralFilter(img,9,75,75)

# convert to grayscale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# inverse color
img = cv2.bitwise_not(img)

# Denoise
lower = np.array(200)  #-- Lower range --
upper = np.array(1000)  #-- Upper range --
mask = cv2.inRange(img, lower, upper)
res = cv2.bitwise_and(img, img, mask= mask)  #-- Contains pixels having the gray color--
t2 = cv2.bitwise_not(img)
res2 = cv2.subtract(t2, res);
res2 = cv2.bitwise_not(res2);


# get text from image using tesseract OCR (google OCR)
print(pytesseract.image_to_string(res2, lang="eng"))

# cv2.imshow('image',res2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()