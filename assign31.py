"""
27,31 Taake some single digit numbers from the user and findout min, maximum, sum, average
"""
num=input("Enter total numbers of digits:")
l=[]
for i in num:
        x=input("Enter digit")
        l.append(i)
print "Minimum of given values:",min(l)
print "Maximum of given values:",max(l)
print "Sum of given values:",sum(l)
avg=sum(l)/len(l)
print "Avg of given numbers:",avg
