num1=[56,67,45,89]
num2=(set(num1))
print(num2)

a={1,2,3,4}
b={3,5,6,4}
c=a|b
print(c)

c=a.union(b)
print(c)

d=a&b
print(d)

d=a.intersection(b)
print(d)

e=a-b
print(e)

f=a^b 
f=a.Symmetric_difference(b) 
print(f) 

a={1,2,3,4}
b={1,2,3,4,5}
c={4,5,6}

d=a|b|c
e=a&b&c

print(a>=b)
print(a.issuperset(b))
print(b.issuperset(a))
print(b>=a)

