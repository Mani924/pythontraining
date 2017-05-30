"""
37. l=['a','A','b','B','d','D','c','C'] WAP to find out case insensitive count and case insensitive search for an element
"""
l=['a','A','b','B','d','D','c','C']
n=raw_input("enter a character to find:")
count=0
Flag=False
for i in l:
    if i.lower()==n.lower():
         count=count+1
if count>=1:
    print "count of given character is :",count
else:
    print "The given character is not present"
for i in l:
    if i.lower()==n.lower():
        Flag=True
        break
    else:
         Flag
if Flag:
    print "the given character is found"
else:
    print "the give character is not found"
