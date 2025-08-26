Subject =["Maths","Tamil","English"]
#Subject [3]="IT"

Subject.append("IT")
print(Subject)

Subject.insert(2,"Bio")
print(Subject)

Subject.extend(["Chemistry","Science"])
print(Subject)

Subject.pop(2)
print(Subject)

Subject.pop()
print(Subject)

Subject.remove("Tamil")
print(Subject)

if "Tamil" in Subject :
   Subject.remove("tamil")
print(Subject)

#Subject.clear()
#print(Subject)

print(Subject.index("IT"))
#print(Subject.index("Science")

#print(Subject.find("IT")

Subject.sort()
print (Subject)

Subject.reverse()
print (Subject)

Subject.sort(reverse=True)
print (Subject)

marks=[50,45,23,78]
print(max(marks))
print(min(marks))
print(sum(marks))

marksD=marks.copy()
print(marksD)

marksD[2]=67
print(marksD)
print(marks)
