"""
42.input fun('abc') output: [[],[a],[b],[c],[a,b],[b,c],[c,a],[a,b,c]]
"""
import itertools
def fun(l):
    list2=[]
    for L in range(0, len(l)+1):
        for subset in itertools.combinations(l, L):
            list2.append(subset)
    return list2
string=raw_input("Enter a string:")
list1=list(string)
x=fun(list1)
output=[]
for i in x:
    if type(i)==tuple:
        output.append(list(i))
print x
