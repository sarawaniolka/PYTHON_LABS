primeNums = []
N = 11

for i in range (2, N+1):
    c=0
    for j in range (2,N+1):
        if i%j == 0:
            c+=1
    if c==1:
        primeNums.append(i)
print(primeNums)