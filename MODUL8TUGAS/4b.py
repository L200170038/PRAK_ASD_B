class Queue(object):
    def __init__(self):
        self.qlist=[]
    def isEmpty(self):
        return len(self)==0
    def __len__(self):
        return len(self.qlist)
    def enqueue(self, data):
        self.qlist.append(data)
    def dequeue(self):
        assert not self.isEmpty(), 'Antrian sedang Kosaosng'
        return self.qlist.pop(0)
    def getRearMost(self):
        return self.qlist[-1]
a = Queue()
a.enqueue(10)
a.enqueue(32)
a.enqueue(28)
a.enqueue(59)
a.enqueue(33)
print ('item paling belakang = ', a.getRearMost())
print (a.dequeue())
print (a.dequeue())
print (a.dequeue())
print (a.dequeue())
print (a.dequeue())
