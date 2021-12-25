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

#Create a random 3×5 array using the np.random.rand(3, 5) function and compute:

y = np.random.rand(3,5)
print(y)

# the sum of all the entries:
SumAll = np.concatenate(y).sum()
print("The sum of all entries: {}".format(SumAll))

# the sum of the rows:
sumRow = np.sum(y,axis=1)
print('The sum of all the rows: {}'.format(sumRow))

# the sum of the columns:
sumCol = np.sum(y, axis=0)
print('The sum of all the columns: {}'.format(sumCol))

# Given the following arrays representing logical values (0 = False, 1 = True)
# compute the logical AND and logical OR operations for every pair of values of the two arrays:

A1 =np.array([1, 1, 0, 0], dtype = bool)
A2 = np.array([1, 0, 1, 0], dtype = bool)
print(A1)
print(A2)

