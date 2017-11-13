import numpy as np
import cv2

def dummy(val):
    pass

identity_kernel = np.array(# [0]
    [[0,0,0],
    [0,1,0],
    [0,0,0]
    ])
sharpness_kernel = np.array([# [1]
    [0,-1, 0],
    [-1,5,-1],
    [0,-1,0]
    ])
blur_kernel = np.array([# [2]
    [0,1,0],
    [1,-3,1],
    [0,1,0]])
detaildark_kernel = np.array([# [3]
    [0,1,2],
    [1,-2,-1],
    [-2,1,0]
    ])
test = np.array([# [3]
    [2,1,2],
    [1,-4,-1],
    [-1,1,-1]
    ])
test2 = np.array([# [3]
    [0,1,4],
    [1,-2,-1],
    [-4,1,0]
    ])
test3 = np.array([# [3]
    [-2,1,0],
    [1,-2,-1],
    [0,1,2]
    ])
blur2_kernel = np.array(# [4]
    [[3,3,3],
    [-3,-3,-3],
    [3,3,3]],
     np.float32)/ 9
nightmode_kernel = np.array([# [5]
    [3,0,3],
    [0,0,0],
    [-3,0,-3]])
nightmode2_kernel = np.array([# [6]
    [1,1,1,1,1],
    [0,1,-5,-1,0],
    [-1,-5,14,-5,-1],
    [0,-1,-5,-1,0],
    [1,1,1,1,1]
    ])
test3_kernel = np.array([# [7]
    [1,-1,1,-1,1,-1],
    [1,-1,1,-1,1,-1],
    [1,-1,1,-1,1,-1],
    [1,-1,1,-1,1,-1],
    [1,-1,1,-1,1,-1],
    [1,-1,1,-1,1,-1],
    [1,-1,1,-1,1,-1],
    ])
test4_kernel = np.array([# [7]
    [-8,8],
    [4,-4]
    ])
epic_dark_kernel = np.array([# [7]
    [-1,-1,-1,-1,-1,-1],
    [-1,-2,2,-1,-1,-1],
    [-1,-1,2,-2,-1,-1],
    [-1, 2,25, 2,-1,-1],
    [-1,-1,2,-1,-1,-1],
    [-1,-2,2,-2,-1,-1],
    [-1,-1,-1,-1,-1,-1],
    ])
test4 = np.array([# [7]
    [8,-8],
    [-4,4]
])
test9 = np.array([# [7]
    [-1,0],
    [3,-1]
])
test7 = np.array([# [7]
    [-2,2],
    [3,-3]
])

kernels =[identity_kernel,test7,test9,test4, test4_kernel, sharpness_kernel, blur_kernel, blur2_kernel, detaildark_kernel, test, test2, test3, nightmode_kernel, 
nightmode2_kernel ,test3_kernel,epic_dark_kernel]

color_original = cv2.imread('test2.png')
color_modified = color_original.copy()

gray_original = cv2.cvtColor(color_original, cv2.COLOR_BGR2GRAY)
gray_modified = gray_original.copy()

cv2.namedWindow('app')
cv2.createTrackbar ('Filters:', 'app', 0, len(kernels)-1, dummy)
cv2.createTrackbar ('Contrast:', 'app', 1, 3, dummy)
cv2.createTrackbar ('Brightness:', 'app', 50, 100, dummy)
# cv2.createTrackbar ('Temperature:', 'app', 50, 100, dummy)
cv2.createTrackbar ('Grayscale:', 'app', 0, 1, dummy)

edits = 0

while True:
    
    grayscale = cv2.getTrackbarPos('Grayscale:', 'app')
    if grayscale == 0:
        cv2.imshow('app', color_modified)
    else:
        cv2.imshow('app', gray_modified)
    
    k = cv2.waitKey(1) & 0xFF
    if k == ord("q"):
        break
    elif k == ord('s'):
        if grayscale ==0:
            edits += 1
            cv2.imwrite('%dedit2.png'%edits,color_modified)
            print('file saved')
        else:
            edits += 1
            cv2.imwrite('%dedit2.png' % edits,gray_modified)
            print('file saved')
    
    contrast = cv2.getTrackbarPos('Contrast:', 'app')
    brightness = cv2.getTrackbarPos('Brightness:', 'app')
    kernel = cv2.getTrackbarPos('Filters:','app')
    grayscale = cv2.getTrackbarPos('Grayscale:', 'app')
    # temperature = cv2.getTrackbarPos('Temperature:', 'app')
    
    color_modified = cv2.filter2D(color_original, -1, kernels[kernel])
    gray_modified = cv2.filter2D(gray_original, -1, kernels[kernel])

    color_modified = cv2.addWeighted(color_modified, contrast, np.zeros(color_original.shape, dtype=color_original.dtype), 0, brightness-50)
    gray_modified = cv2.addWeighted(gray_modified, contrast, np.zeros(gray_original.shape, dtype=gray_original.dtype), 0, brightness-50)

cv2.destroyAllWindows()