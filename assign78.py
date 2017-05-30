"""
78. WAP to replace perticular number of substings with a given destination string
"""
s=raw_input("Enter main string:")
m=raw_input("Enter substring :")
d=raw_input("Enter destination string:")
if m in s:
        for i in range(s.count(m)):
                print s.replace(m,d)
else:
        print "substring is not present in main string"
