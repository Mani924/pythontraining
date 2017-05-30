"""
39. find the start position of the largest block of repeated characters in a given string
"""
s=raw_input("enter a words:")
j=s.split(' ')
k=raw_input("enter a characters:")
l=0
for i in j:
    c=i.count(k)
    h=len(i)
    if c >l:
        l=c
for i in j:
    if l==i.count(k) 
        print "The start position of larget block of repeated characters in a given string:",j.index(i)
