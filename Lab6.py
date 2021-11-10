print("=======================================")
print("global vs local variables")
print("=======================================")
def sum(a,b):
    print('a=' + str(a))
    print('b=' + str(b))
    a = 100
    return a+b

a = 5
b = 10
c = sum(a,b)
print(c)

print("=======================================")
print("lists, tuples, dicts, arrays")
print("=======================================")


l1 = []
l2 = [2323, 23324, 24454365,67657, 75775]
print(l2[3])
print(l2[-3:-1])

i=0
for elem in l2:
    print('Element {} at {}'.format(elem,i))
    i += 1

print(l2.index(2323))

l2.insert(0,1)
print(l2)

