"""
55. find out all perfect numbers in given range
"""
n = input(" Please Enter any Number: ")
for c in xrange(1,n):
    if sum(x for x in xrange(1,c) if not c%x) == c:
        print c
