class PriorityQueue(object):
    def __init__(self):
        self.qlist=[]
    def __len__(self):
        return len(self.qlist)
    def isEmpty(self):
        return len(self)==0
    def enqueue(self, data, priority):
        entry=_PriorityQEntry(data, priority)
        self.qlist.append(entry)
    def dequeue(self):
        assert not self.isEmpty()
        x=[]
        for i in self.qlist:
            x.append(i.priority)
        a=x.index(min(x))
        return self.qlist.pop(a).item
class _PriorityQEntry(object):
    def __init__(self, data, priority):
        self.item=data
        self.priority=priority
b=PriorityQueue()
b.enqueue("susi", 3)
b.enqueue("wati", 1)
b.enqueue("triana", 2)
print (b.dequeue())
print (b.dequeue())
print (b.dequeue())
