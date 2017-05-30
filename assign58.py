"""
58. WAP to remove n occurances of specified element from a list
"""
s=[1,2,3,1,2,4,2]
k=2
l=[]
j=0
if k in s:
        for i in s:
                if i==k:
                        i=s.index(k,j)
                        l.append(i)
                j=i+1
        print s
else:
        print "The specified element is not present in list"
 
