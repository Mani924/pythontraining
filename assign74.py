class c1(object):
    obj=False
    def __new_(cls,a,b):
        if not cls.obj:
            cls.obj=super(c1,cls).__new__(cls)
        return cls.obj
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def get(self):
        return self.a,self.b
o1=c1(10,20)
print "first instance {0} and id {1}" .format(o1.get(),id(o1))
o2=c1(100,200)
print "second instance {0} and id {1}" .format(o2.get(),id(o1))
o3=c1(1000,2000)
print "thrid instance {0} and id {1}" .format(o3.get(),id(o1))
        
