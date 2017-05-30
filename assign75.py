class class_meth_des(object):
    def instance_method(self,x):
        print "executing instancemethod(%s,%s)"%(self,x)

    @classmethod
    def class_method(cls,x):
        print "executing classmethod(%s,%s)"%(cls,x)

    @staticmethod
    def static_method(x):
        print "executing staticmethod(%s)"%x    

a=class_meth_des()
a.class_method(1)
class_meth_des.class_method('hi')
a.static_method(1)
class_meth_des.static_method('hi')
class_meth_des.instance_method(a,1)
a.instance_method('hi')

"""
@classmethod:
-------------
In classmethods, the class of the object instance is implicitly passed as the first argument instead of self. We can call class method with instance
or using class name

@staticmethod:
--------------
In staticmethods, neither self (the object instance) nor  cls (the class) is implicitly passed as the first argument.
They are like plain functions except that you can call them from an instance or the class

instancemethod:
--------------
An instance method requires an instance in order to call it, and requires no decorator. This is a common method.
The first parameter is  self and it is passed hiddenly when calling an instance method and this represents the instance calling the method.

"""

 
