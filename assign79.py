"""
79.WAP top remove substring form the given string without using replace function
"""
s=raw_input("Enter main string:")
m=raw_input("Enter substring :")
l = list(s)
if m in s:
        for i in l:
                for i in l:
                        if i in m:
                                del l[l.index(i)]
        s="".join(l)
        print s
else:
     print "substring is not found in main string"
