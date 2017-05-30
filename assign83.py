"""
83.find out intersection, union, difference of two list without/with using set
"""
#without using set
list1 = [1,2,3]
list2 = [3,4,5]
Intersection_List = []
Union_List = []
difference_List=[]
for i in list1:
	if i in list2:
		Intersection_List.append(i)
print "Intersection List:",Intersection_List
for j in list2:
    if j not in list1:
        Union_List.append(j)
print "Union List:",Union_List
for i in list1:
        if i not in list2:
                difference_List.append(i)
print "Difference list:",difference_List

#with using set
a = [1,2,3]
b = [3,4,5]
def intersect(a, b):
        return list(set(a) & set(b))
def union(a, b):
        return list(set(a) | set(b))
def difference(a,b):
        l=[]
        for i in a:
                if i not in b:
                        l.append(i)
        return l
                
                
print "intersection of lists" ,intersect(a, b)
print "union of lists",union(a, b)
print "difference of lists",difference(a,b)
