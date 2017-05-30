#with class modifying the existing  function in dict class
class dictdef(dict):
    def __init__(self,data):
        super(dictdef,self).__init__(data)
    def __add__(d1,d2):
        d={}
        for i in d1.keys():
            print d2.get(i,0)
            d.update({i:d1[i]+d2.get(i,0)})
        return d
    def __sub__(d1,d2):
        d={}
        for i in d1.keys():
            d.update({i:d1[i]-d2.get(i,0)})
        return d
    def __mul__(d1,d2):
        d={}
        for i in d1.keys():
            d.update({i:d1[i]*d2.get(i,0)})
        return d
m1=dictdef({'a': 10, 'b': 9, 'c': 8, 'd': 7})
m2=dictdef({'a': 1, 'b': 2, 'c': 3, 'e': 2})
add=m1+m2
sub=m1-m2
mul=m1*m2
print "program with class started"
print "sum of dict:",add
print "sub of dict:",sub
print "mul of dict:",mul
print "program with class ended"


#without class using dictornary comprehension
d1 = {'a': 10, 'b': 9, 'c': 8, 'd': 7}
d2 = {'a': 1, 'b': 2, 'c': 3, 'e': 2}
d3 = {key: d1[key] - d2.get(key, 0) for key in d1.keys()}
d4={key: d1[key]+d2.get(key, 0) for key in d1.keys()}
d5={key: d1[key]* d2.get(key, 0) for key in d1.keys()}
print "sub of dict:",d3
print "add of dict:",d4
print "mul of dict:",d5


