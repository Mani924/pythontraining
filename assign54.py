"""
54. write a function to get dynamic list for floating numbers also based on strat and end and step parameters
"""
def dynamic_list(start, step, length):
    l=[]
    for i in range(length):
           x=start + i * step
           l.append(x)
    return l
print dynamic_list(0,0.4,10)
