"""
46.Find third max value of element in a list with soring and without sorting a list.
"""
l=[30,10,20,50,80,100]
l1=[]
for i in range(3):
    l1.append(max(l))
    l.remove((max(l)))
print "third max value in list is:",l1[2]

l=[30,10,20,50,80,100]
l.sort(reverse=True)
print l[2]
