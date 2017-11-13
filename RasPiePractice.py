import numpy as np
import matplotlib.pyplot as plt 
 
#A =np.ones((3,3))
s = 0 
""" short hand how to calculate matrix's sum
for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        s = s + A[i,j]

print s
"""

# numpy has a short cut to make it way easier
# A.sum()

# Image Similarity 

"""
A and B are matrixes that represent images pixels
A = ([
    [0,230,75],
    [0,210,60],
    [0,200,50]
    ])
B = ([
    [0,225,70],
    [0,210,65],
    [0,200,55]
    ])
|A - B| if 0 then images are the same
"""
# long way v short way
'''
A = np.array([[0,230,75],[0,210,60],[0,200,50]])
B = np.array([[0,225,70],[0,210,65],[0,200,55]])

s = 0
for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        s = s + abs(A[i,j] - B[i,j])

print(s)
# short way
print abs(A - B).sum()
'''
# pervents errors by squaring elements 
'''
for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        s = s + (A[i,j] - B[i,j]) ** 2
print(s)

print ((A - B) ** 2).sum()
'''
# Mean Squared Error
"""
sse = sum squared error
mse = mean squared error    divide by the total number of pixels

A = np.zeros((3,3))
B = np.ones((3,3))
sse = 9
sse  / 9(totalpixels) = mse
mse = 1

C = np.zeros((10,10))
D = np.ones((10,10))
sse = 100 
sse  / 100(totalpixels) = mse
mse = 1

However they have the same error but one is just larger so the error seems much larger
So by taking an average it remove the variable of size from the equation

"""
# long way mean squared error
'''
A = np.zeros((3,3))
B = np.ones((3,3))

for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        s = s + (A[i,j] - B[i,j]) ** 2
s = s / float(A.shape[0]*A.shape[1])

print(s)
'''
# numpy short cut 
'''
C = np.zeros((10,10))
D = np.ones((10,10))

print ((A - B) ** 2).mean()
'''

# Structuaral Similarity SSIM
"""
mse/sse: look at pixels individually 
where as SSIM: looks at groups/structures of pixels, most like humans

SSIM(A,B)= L(A,B) * C(A,B) * S(A*B)
       luminance, constrast, structure

-1 <= SSIM <= 1
-1 = perfectly imperfect  
 1 = perfect
"""
