"""
57. WAP to do all queue operations using lists
"""
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
s=Queue()
print "To know whether queue is empty or not:",s.isEmpty()
s.enqueue('process1')
s.enqueue('process2')
print "The size of queue:", s.size()
print "To remove the element from the queue:",s.dequeue()
