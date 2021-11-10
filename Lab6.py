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
l2 = [1,2323, 23324, 24454365,67657, 75775]
print(l2[3])
print(l2[-3:-1])

i=0
for elem in l2:
    print('Element {} at {}'.format(elem,i))
    i += 1

print(l2.index(2323))

l2.insert(0,1)
print(l2)

s1=set(l2)
print(s1)

print("=======================================")

l4 = [25,12,654,67]
l5= [23,66]
l6 = l4+l5
print(l6)

l7 = [x*2 for x in l6]
print(l7)

print("=======================================")
print('tuples')
print("=======================================")
# u cant modify a tuple


t1= (12,13,42)
print(t1)

print("=======================================")
print("dicts")
print("======================================= \n")

d1 = {"a" : 525, "a": 646, "c":4242}
print(d1)
print(d1['a'])
#second one overwrites the first a

for k,v in d1.items():
    print('{} : {}'.format(k,v))
