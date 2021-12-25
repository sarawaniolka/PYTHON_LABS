#Compute the multiplication of the following matrices:

M1 = [[1, 0], [0, 1]]
M2 = [[1, 2], [3, 4]]
print(M1)
print(M2)

#Generate an array of length 3n filled with the cyclic pattern 1, 2, 3.

n = 2
arr = [1,2,3] * n
print(arr)

#Create a 10×10 matrix of zeros and then "frame" it with a border of ones.
import numpy as np
x =  np.zeros((10,10),dtype = int)
rows = len(x)
cols = len(x[0])

for r in range(rows):
    for c in range(cols):
        if r ==0:
            x[r,c]=1
        elif r==9:
            x[r,c]=1
        elif c==0:
            x[r,c]=1
        elif c==9:
            x[r,c]=1

print(x)