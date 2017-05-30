"""
43. Remove duplicates from the list: a=[1,2,3,2,3,4,1,3,4]
"""
a=[1,2,3,2,3,4,1,3,4]
b=[]
for i in a:
        if i not in b:
                b.append(i)
print b
