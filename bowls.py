n = 100000000
sum = (n *(n+1)) / 2
print(sum)

#recursion
def sum_bowls_recursion(r):
    if r == 1:
        return 1
    else:
        return r + sum_bowls_recursion(r-1)

print(sum_bowls_recursion(998))