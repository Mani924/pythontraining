"""
28.WAP> 10 -> 000010
       100 ->  000100
      1000 ->  001000
  2345678  ->  2345678
"""


l=[10,100,1000,23456789]
len1=0
for i in l:
    x=str(max(l))
for i in x:
    len1=len1+1
y=len1-1
for k in l:
    print "%0{0}d".format(y)%k


"""
second method
"""
s = input("Enter a number:")
print "%06d"%s
