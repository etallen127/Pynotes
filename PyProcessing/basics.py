import cv2

img = cv2.imread('test.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY_INV)
thresh = cv2.GaussianBlur(thresh, (7,7), 0)

contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contour = contours[len(contours)-1]

epsilon = 0.1*cv2.arcLength(contour, True)
approx = cv2.approxPolyDP(contour, epsilon, True)

cv2.drawContours(img, [approx], -1, (0,255,0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

