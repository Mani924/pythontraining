"""
81. take two lists keys, values and form a dictionary
"""
d={'k1':'v1','k2':'v2','k3':'v3','k4':'v4','k5':'v5'}
keys=[]
values=[]
for i in d.keys():
        keys.append(i),values.append(d[i])
print "The list of keys:",keys
print "The list of values:",values
