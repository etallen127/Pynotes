import numpy as np
import cv2
"""
a = np.matrix([
    [1 , 4, 17],
    [16, -14, 19],
])

A = np.array([
    [17, 8, 3 ],
    [0, -3, 10],
    [7, 100, 8]])

print(a) * (A)
"""

"""
if img is None:
    print"Image not loaded"
else:
    print"image is loaded"
"""
img = cv2.imread('test.jpeg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
bc_img = cv2.addWeighted(img,4,np.zeros(img.shape, dtype=img.dtype), 0,-150)
K = np.array([ 
  [0,1,0],
  [1,-3,1],
  [0,1,0]
])
L= np.array([ 
  [1,-1,1],
  [-1,0,-1],
  [1,-1,1]
])
'''[-1,-1,-1], # cool space background generator
    [2,2,2],
    [-1,-1,-1]
'''
convolved = cv2.filter2D(img, -1,K)
convolved2 =cv2.filter2D(convolved, -1,L)
'''
pixelNew = c * pixel old + b   0 <= pixelNew <= 255
Iout = c * Iin + B   B :matrix with same dim as Iin all values are b
with open cv you can use a zero matrix with original img.shape and data type to cancle out beta, if only working with one image
Convolution: Kernel:filter is a small square matrix with odd dim convolve with an image/apply to greate an image effect
small: 3x3 5x5 13x13
square row = col

[1,  2, 1]  this kernal detects top-bottom edges(horizantal edges)   other kernals can be used for sharpening, blurring, edge detection embossing. ect
[0,  0, 0]
[-1,-2,-1]

[0,0,0], this is an identity kernel, should be obious by all values should come out to be the same rendering the same image
[0,1,0],
[0,0,0]

convolution: is a math operation to apply a kernel to an image, applys effect to a group of pixels vs indivdual pixels (like contract and brightness)

Multiply the kernal off of the anchor point then add up the sum of the kernel influence. Then set the new anchor point = to the new value
Can create a kernal to detect edges and create a lasso using if statement allow user to isolate different layers of an image
'''

cv2.imshow("convolved", convolved)
cv2.imshow("convolved2", convolved2)
# cv2.imshow("bc",bc_img)
# cv2.imshow("screen",gray)
cv2.imshow("color",img)
cv2.waitKey(0)
cv2.destroyAllWindows()