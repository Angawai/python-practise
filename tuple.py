
t=(90,70,26,90,55)
print(t)
print(type (t))

print(t[2])
##t[2]=36
print(t)

##t.append(45)
print(t)

marks=[45,56,67,89,78]
t=(marks)
print(t)

t=tuple(marks)
print(t)
print(type (t))

marks1=(67,87,87)
marks2=(56,87,65)
marks3=marks1+marks2
print(marks3)

student=("Seelan",38,"23/02/1987")
fname,age,dob=student
print(fname)
print(age)
print(dob)


marks=[45,56,67,89,78]
a,*b,c=marks
print(a)
print(b)
print(c)

marks=[45,56,67,89,78]
a,b,*c=marks
print(a)
print(b)
print(c)

