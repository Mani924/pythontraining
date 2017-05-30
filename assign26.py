"""
26. findout nth occurance of given substring
"""
ms=raw_input("Enter main string:")
ss=raw_input("Enter sub string:")
n=input("Enter the number of ocuurance u want to find:")
def string_occurance(ms, ss, n):
        occ= ms.find(ss)
        while occ >= 0 and n > 1:
            occ=ms.find(ss, occ+1)
            n -= 1
        return occ
if ss in ms:
   if ms.count(ss)>=n:
        index=string_occurance(ms,ss,n)
        print "The %s occurance of string is at index %s:",(n,index)
   else:
        print "The substring occurance in main string is less than given occurance"
else:
    print "The substring is not in main string"


"""
another method
"""

l=[]
k=0
for char in ms:
   if char==ss:
      i=ms.index(ss,k)
      l.append(i)
      k=i+1
print "The nth occurance of given string is",l[len(l)-1]
