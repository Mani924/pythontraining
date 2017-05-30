"""
82.delete more than one key value pair at a time
"""
d={'k1':'v1','k2':'v2','k3':'v3','k4':'v4','k5':'v5'}
rd={'k2':'v2','k3':'v3'}
for i in d.keys():
        if i in rd:
                del d[i]
print d
