"""
49. input = 1,2,3,4,5,6,8,10 output = odd,even,odd,even,odd,even,even,even
"""
l=[1,2,3,4,5,6,8,10]
l1=[]
for i in l:
        if i%2==0:
                out="even"
                l1.append(out)
        else:
                out="odd"
                l1.append(out)
print l1
