"""
40. WAP to find union and intersection of lists
"""
a = [0,1,2,0,1,2,3,4,5,6,7,8,9]
b = [5,6,7,8,9,10,11,12,13,14]
def unique(a):
    """ return the list with duplicate elements removed """
    return list(set(a))
def intersect(a, b):
    """ return the intersection of two lists """
    return list(set(a) & set(b))
def union(a, b):
    """ return the union of two lists """
    return list(set(a) | set(b))
print "unique elemnets in lists",unique(a)
print "intersection of lists" ,intersect(a, b)
print "union of lists",union(a, b)
