"""
32. l=[10,20,30,[40,50,60],70,[80,90,20]]. Convert n dimensional list as sigle dimentiona list
"""
l=[[10,[20,30,[40,50]],60],70,[80,90,20]]
L=[]
def sindm(l):
    for i in l:
        if type(i)==list:
            sindm(i)
        else:
            L.append(i)
    return L
print  sindm(l)
