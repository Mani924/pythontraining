"""
38. l=['a','A','b','B','d','D','c','C']  sort the list properly
"""
L=['a','A','b','B','d','D','c','C']
print L
L.sort()
l2=[]
for i in L:
        if i not in l2:
            for k in range(L.count(i)):
                l2.append(i)
        if isinstance(i,str):
               j=i.lower()
               if j in L and j not in l2:
                   for k in range(L.count(j)):
                       l2.append(j)
print l2
