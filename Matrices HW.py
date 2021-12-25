import numpy as np

# Compute the multiplication of the following matrices:

M1 = [[1, 0], [0, 1]]
M2 = [[1, 2], [3, 4]]
print(M1)
print(M2)

# Generate an array of length 3n filled with the cyclic pattern 1, 2, 3.

n: int = 2
arr = [1, 2, 3] * n
print(arr)

# Create a 10×10 matrix of zeros and then "frame" it with a border of ones.


x = np.zeros((10, 10), dtype=int)
rows = len(x)
cols = len(x[0])

for r in range(rows):
    for c in range(cols):
        if r == 0:
            x[r, c] = 1
        elif r == 9:
            x[r, c] = 1
        elif c == 0:
            x[r, c] = 1
        elif c == 9:
            x[r, c] = 1

print(x)

# Create a random 3×5 array using the np.random.rand(3, 5) function and compute:

y = np.random.rand(3, 5)
print(y)

# the sum of all the entries:
SumAll = np.concatenate(y).sum()
print("The sum of all entries: {}".format(SumAll))

# the sum of the rows:
sumRow = np.sum(y, axis=1)
print('The sum of all the rows: {}'.format(sumRow))

# the sum of the columns:
sumCol = np.sum(y, axis=0)
print('The sum of all the columns: {}'.format(sumCol))

# Given the following arrays representing logical values (0 = False, 1 = True)
# compute the logical AND and logical OR operations for every pair of values of the two arrays:

A1 = np.array([1, 1, 0, 0], dtype=bool)
A2 = np.array([1, 0, 1, 0], dtype=bool)
print(A1)
print(A2)

for i in range(0, len(A1)):
    value_and = A1[i] and A2[i]
    value_or = A1[i] or A2[i]
    print('{} and {}: {}'.format(A1[i], A2[i], value_and))
    print('{} or {}: {}'.format(A1[i], A2[i], value_or))

# Find indices of non-zero elements from [1, 2, 0, 0, 4, 0]
M = [1, 2, 0, 0, 4, 0]
indices = []
for i in range(0, len(M)):
    if M[i] != 0:
        indices.append(i)
print('The indices of non-zero elements: {}'.format(indices))

# Create an 8×8 array with random values and find minimum and maximum value
X = np.random.randn(8, 8)
print(X)
print('The min value: {}'.format(np.amin(X)))
print('The max value: {}'.format(np.amax(X)))

# Create a 8×8 array with random natural values from the range (1-100) on the diagonal,
# other values should be 0.
A = np.zeros((8, 8), int)
v = np.random.random_integers(1, high=100, size=8)
A = np.diag(v)
print(A)


# Write a function which creates an n×n matrix with (i,j)-entry equal to i+j.
def create_matrix(n):
    A = np.random.rand(n, n)
    rows = len(A)
    cols = len(A[0])
    print(A)
    for r in range(0, rows):
        for c in range(0, cols):
            A[r, c] = r + c
    print(A)


create_matrix(5)

# Write a function which creates an n×n matrix with rows having subsequent values multiplied by the row's number.

def multiplied_rows(n):
    vector = np.arange(n)
    A = np.asmatrix([vector,]*n)
    for r in range(0,n):
        for c in range(0,n):
            A[r,c]=A[r,c]*(r+1)
    print(A)

multiplied_rows(4)
