"""
Image Segmentation

Thresholding: Simple form of segmentation, using matrixes to create a numaric value to remove images foreground, background, or objects that fall above or below a set value.
Often done in GrayScale.

"""

import cv2

img1 = cv2.imread('contours.png', 0 # the 0 is used to set the image to gray scale for the processing
img2 = cv2.imread('example.jpg', 0)

_, thresh1 = cv2.threshold(img1, 135, 255, cv2.THRESH_BINARY_INV)
_, thresh2 = cv2.threshold(img2, 235, 255, cv2.THRESH_BINARY)

cv2.imshow('thresh2', thresh2)
cv2.imshow('thresh1', thresh1)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
                        Contour Detection
    
    Contour: is a closed curve along a boundary of color or intensity
    list of points/ coordnates that define the curve

                        Chain Approximation: 
    Simple approx: Use corners coordnates to define where line segments start and end
    No approx: Define every point of the contour

                        Retrieval Mode:
    List: In no particular order and grabs all contours
    External: Only retrieves contours that are not inside another contour, unordered
    Tree: Returns a full hierarchy of contours 

"""