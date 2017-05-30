"""
53. Sort the list marks = [("mohan", 80), ("satish", 90), ("purnesh", 40), ("venkat", 30)] acording to descending order of marks
"""
marks=[("mohan", 80), ("satish", 90), ("purnesh", 40), ("venkat", 30)]
d=dict((y,x) for x,y in tuple(marks))
s=[]
for i in sorted(d.keys(), reverse=False):
       m=(i,d[i])
       s.append(m)
print "Descending order list according to marks:",s
