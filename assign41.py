"""
41.input: fun(5) output: [1,2,3,4,3,2,1]
"""
def fun(n):
        l = []
        c = 0
        for i in range(1,2*n):
                if i>n:
                        c=c+1
                        l.append(n-c)
                else:
                        l.append(i)
                
        return l
print fun(5)
