"""
56. WAP to do all stack operations using lists
"""
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

s=Stack()
print s.isEmpty()
s.push(4)
s.push('dog')
print s.peek()
s.push(True)
print "The size of stack:" ,s.size()
print "To know whether stack is empty or not:", s.isEmpty()
s.push(8.4)
print "Remove the elemnet from the stack",s.pop()
print "Removed element from the stack:", s.pop()
print "size of the stack :" s.size()
