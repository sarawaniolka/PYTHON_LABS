primeNums = []
x = 27

for i in range (2, x+1):
    c=0
    for j in range (2,x+1):
        if i%j == 0:
            c+=1
    if c==1:
        primeNums.append(i)
print(primeNums)
