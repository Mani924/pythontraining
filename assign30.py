"""
30.Take actuual string, soucrce string, destination string. replce first nth occurances of soucestring with destination string of actual string
"""
ms=raw_input("enter the actual string:")
ss=raw_input("Enter the sub string:")
ds=raw_input("Enter the destination string:")
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
        ms=ms[:index]+d+ms[index+1:]
        print "The %s occurance of string is at index %s:",(n,index)
        print "After replacement of string:",ms
   else:
        print "The substring occurance in main string is less than given occurance"
else:
    print "The substring is not in main string"
